# Async Web Intelligence Collector

## 1. Problem Understanding

### What

This project is a client-side Python application for collecting information from selected web pages and converting the responses into a consistent movie-data structure. It demonstrates synchronous HTTP communication with Requests, asynchronous HTTP communication with HTTPX, `asyncio`-based concurrency, Crawl4AI web-page crawling, parsing, normalization, an OpenAPI contract, testing, and error handling.

### Why

Fetching several external pages sequentially makes the client wait for each network operation before starting the next one. External access can also fail because of HTTP errors, timeouts, connection problems, or automated-access restrictions. The application therefore needs both an efficient I/O model and result-level failure handling so that one failed URL does not unnecessarily discard the rest of a batch.

### How

Requests provides the sequential baseline. HTTPX's `AsyncClient`, `asyncio.gather()`, and a semaphore provide asynchronous, bounded concurrent fetching. Crawl4AI is isolated as the dedicated browser-based crawler. The processing layer parses IMDb HTML or OMDb JSON and normalizes movie name, genre, rating, release date, and URL fields. The OpenAPI file describes how a future API layer could expose the client behavior; it is not a running server.

The selected IMDb pages returned AWS WAF/bot-verification responses during automated access. The crawler detects this condition as `BotVerificationChallenge`; it does not bypass or circumvent the WAF. With instructor approval, OMDb is used as a separate data-access adapter, addressed with the same IMDb IDs, to obtain the required metadata. Normalized results retain the corresponding IMDb page as the source/reference URL.

## 2. Selected Website

IMDb was selected because its title pages are a suitable, publicly accessible source/reference for movie metadata. The project uses these three predefined titles:

| Movie | IMDb ID | Required fields |
| --- | --- | --- |
| Interstellar | `tt0816692` | Movie Name, Genre, Rating, Release Date, Movie URL |
| Inception | `tt1375666` | Movie Name, Genre, Rating, Release Date, Movie URL |
| The Matrix | `tt0133093` | Movie Name, Genre, Rating, Release Date, Movie URL |

The IMDb URLs remain associated with the normalized results even when metadata is obtained through OMDb.

## 3. Selected Crawler

Crawl4AI is the selected crawler and is isolated in `src/crawler/crawler.py`. The module uses `AsyncWebCrawler` and its asynchronous `arun()` method to crawl a page. A crawl result exposes the HTML, Markdown, links, metadata, and success/failure state used by the project.

The module also provides `crawl_all_pages()`, which crawls several URLs concurrently and keeps results in input order. The helper `is_waf_challenge()` examines returned HTML for known bot-verification markers. A detected challenge is returned as an unsuccessful result with `error_type` set to `BotVerificationChallenge`.

## 4. Reason for Crawler Selection

Crawl4AI was chosen because its asynchronous `AsyncWebCrawler` interface fits the project's `asyncio` architecture while providing more crawler-oriented output than a basic HTTP client. Its `arun()` result includes HTML and Markdown extraction, links, metadata, and crawl status. The crawler remains an independent layer, so the Requests and HTTPX clients can be benchmarked without pretending that all three paths form one automatic pipeline.

The central usage pattern is:

```python
async with AsyncWebCrawler() as crawler:
    result = await crawler.arun(url=url)
```

This supports concurrent page work through the surrounding async code and gives the processing layer content that can be parsed when access is permitted.

## 5. Architecture

The repository uses separate, focused paths rather than a single application server:

```text
IMDb URLs
   ├── requests_client.py ── sequential HTTP results
   ├── httpx_client.py ──── async HTTP results
   ├── crawler.py ────────── HTML/Markdown/links/metadata
   └── movie_service.py ─── OMDb responses by IMDb ID
                                  │
                       parser.py + normalizer.py
                                  │
                         structured movie results
```

| Component | Responsibility |
| --- | --- |
| `src/http/requests_client.py` | Synchronous `requests.get()` calls, status categorization, transient retries, and structured results. |
| `src/http/httpx_client.py` | Async HTTPX requests, `asyncio.gather()`, semaphore-bounded concurrency, ordering, and structured failures. |
| `src/crawler/crawler.py` | Crawl4AI integration, crawl output collection, concurrent crawling, and WAF challenge detection. |
| `src/processing/parser.py` | Extracts movie data from IMDb JSON-LD/HTML or OMDb JSON. |
| `src/processing/normalizer.py` | Converts parsed values to the common movie format and summarizes batch results. |
| `src/omdb/omdb_client.py` | Async OMDb adapter using `OMDB_API_KEY` and an IMDb ID. |
| `src/omdb/movie_service.py` | Fetches the three selected movies concurrently, then parses and normalizes them. |
| `src/benchmark.py` | Measures sequential Requests versus concurrent HTTPX fetching. |
| `openapi.yaml` | OpenAPI 3.1.1 contract for a possible API layer. |
| `tests/` | Unit and contract tests for HTTP, async behavior, processing, OMDb, crawler detection, and OpenAPI. |

The OMDb path is the approved fallback data-access path. It is not silently coupled to the direct IMDb crawler, and the benchmark measures HTTP client behavior only.

## 6. Installation Instructions

From the `async_web_intelligence_api` directory, install the dependencies listed in `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

The requirements include Requests, HTTPX, pytest, pytest-asyncio, Crawl4AI, and PyYAML. Crawl4AI may require its own browser/runtime setup depending on the local environment; the project itself does not add another installer or server configuration.

The OMDb service reads its credential from an environment variable. In PowerShell, set a local value before using the service:

```powershell
$env:OMDB_API_KEY = "your_omdb_api_key"
```

Do not commit, print, or place a real key in source control or documentation.

## 7. Execution Instructions

Run these commands from `BL-Practice_Python/async_web_intelligence_api`:

```powershell
# Automated tests
python -m pytest -v

# Sequential Requests demonstration
python tests/test_requests_manually.py

# Crawl4AI demonstration
python -m tests.test_crawler_manually

# Approved OMDb collection and normalization
python -m src.omdb.movie_service

# Requests versus HTTPX benchmark
python -m src.benchmark
```

The manual Requests file executes its demonstration at module load, while the crawler, movie service, and benchmark have executable module entry points. Live commands depend on network access, IMDb/OMDb availability, and the OMDb environment variable where applicable.

## 8. OpenAPI Explanation

`openapi.yaml` is an OpenAPI 3.1.1 API contract only. It does not start a FastAPI, Flask, Django, or other HTTP server. The contract describes how a downstream API layer could expose this client:

| Endpoint | Contract purpose |
| --- | --- |
| `POST /crawl` | Accepts a required `urls` array and returns collection results. Individual URLs may fail. |
| `GET /health` | Returns a health object containing `status`. |
| `GET /results` | Returns a result count and an array of collected results. |

The main schemas are `CrawlResponse`, `CrawlResult`, and `MovieData`. `CrawlResult` contains a URL, optional title, `success` or `failed` status, movie data, and an optional error. `MovieData` describes genre, rating, release date, and URL. The contract gives a future API consumer a stable shape without claiming that an API server currently exists.

## 9. Requests vs HTTPX Comparison

| Aspect | Requests | HTTPX |
| --- | --- | --- |
| Execution model | Synchronous | Asynchronous through `httpx.AsyncClient` |
| Behavior here | One request completes before the next starts | Multiple requests can progress concurrently |
| Concurrency | Sequential in `fetch_sequential()` | `async_fetch_many()` uses `asyncio.gather()` and a semaphore |
| Project use | Baseline client and error-handling tests | Async client, concurrency tests, and benchmark comparison |
| Suitable workload | Simple sequential calls or blocking code | I/O-bound batches where bounded concurrency is useful |

HTTPX is not assumed to be universally faster. Its benefit in this project comes from allowing network waits to overlap for the selected batch.

## 10. asyncio Explanation

`asyncio` supplies the event loop that runs coroutine functions. `async` and `await` let the program yield while a network operation is waiting, allowing other scheduled network operations to make progress. `asyncio.gather()` starts the batch and returns the corresponding results. `asyncio.Semaphore(max_concurrency)` bounds the number of active HTTPX requests, preventing unbounded concurrency.

Both `async_fetch_many()` and `crawl_all_pages()` associate results with the original URL order by processing gathered results alongside the input URLs. This is concurrency for network I/O, not CPU parallelism: the code does not create multiple CPU processes or threads for computation.

## 11. Benchmark Results

The recorded benchmark result for the three selected IMDb URLs is:

| Mode | Time |
| --- | ---: |
| Sequential | 1.0405 sec |
| Async | 0.6791 sec |
| Improvement | 34.74% |

URLs processed: `3`.

These values demonstrate the benefit of overlapping I/O for this workload, but timings vary with network conditions. The direct IMDb requests returned HTTP 403 because of access restrictions, so this run measures request/concurrency behavior rather than successful IMDb extraction.

## 12. Error-Handling Strategy

The Requests and HTTPX clients categorize status codes as 2xx success, 3xx redirection, 4xx client error, or 5xx server error. HTTP errors are returned as structured failed dictionaries rather than being allowed to terminate the whole operation. The clients separately handle timeouts, connection errors, and other request errors.

Requests and HTTPX retry timeouts, connection errors, and HTTP 5xx responses. With the default `max_retries=3`, a failure can receive four total attempts. The delay uses exponential backoff of `backoff_factor * 2**attempt` (one, two, and four seconds with defaults). 4xx responses are not retried. OMDb handles HTTP status, timeout, connection, and request errors, but it does not implement retries or backoff.

Batch functions use `asyncio.gather(..., return_exceptions=True)` and convert unexpected per-task exceptions into failed results. Thus partial failures preserve successful results and input order. The crawler reports Crawl4AI exceptions and detects WAF/bot-verification content as `BotVerificationChallenge`. The OMDb client returns `ConfigurationError` without making a request when `OMDB_API_KEY` is missing; unsuccessful OMDb payloads are rejected during JSON parsing/normalization.

## 13. Testing Strategy

The repository contains 48 pytest test functions across the automated test modules. Tests use pytest and pytest-asyncio, with mocked external HTTP calls so client behavior can be checked without relying on live services. Coverage includes:

- synchronous Requests status, timeout, connection, generic error, and retry behavior;
- HTTPX behavior, async concurrency, partial failures, and input ordering;
- parser and normalizer behavior for movie data;
- WAF challenge detection and crawler result handling;
- OMDb success, configuration, response, and network failures; and
- OpenAPI file existence, validity, endpoints, and required schemas.

`test_crawler_manually.py` is a live/manual demonstration; the automated crawler coverage focuses on the detection and result logic rather than requiring a real Crawl4AI browser crawl.

## 14. Limitations

- IMDb may return a WAF or bot-verification challenge, preventing direct extraction.
- The approved fallback depends on OMDb and requires `OMDB_API_KEY`.
- Live behavior depends on external network services and their availability.
- Benchmark timings vary by network and service conditions.
- This is a client-side project, not a running API server.
- The implementation targets three predefined URLs and a limited movie-field set.
- Website structure, response formats, or access policies may change and affect crawling or parsing.

## 15. Ethical and Legal Considerations

Use this project only with publicly accessible or otherwise permitted data. Respect `robots.txt`, website Terms of Service, access policies, and applicable rate limits. Do not bypass CAPTCHA, WAF, authentication, or other access controls, and do not overwhelm target websites with requests. This project treats the IMDb WAF challenge as a restriction to report, not a mechanism to circumvent. The OMDb fallback was used with instructor approval and should likewise be operated according to its service terms and applicable law.
