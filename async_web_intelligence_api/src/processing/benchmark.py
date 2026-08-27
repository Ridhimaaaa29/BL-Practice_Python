"""Benchmark synchronous and asynchronous URL fetching for Task 7."""

import asyncio
import time

from src.http.requests_client import fetch_page as sync_fetch_page
from src.http.httpx_client import async_fetch_many


IMDB_URLS = [
    "https://www.imdb.com/title/tt0816692/",  # Interstellar
    "https://www.imdb.com/title/tt1375666/",  # Inception
    "https://www.imdb.com/title/tt0133093/",  # The Matrix
]


def fetch_sequential(urls):
    """
    Fetch URLs sequentially using the synchronous Requests client.

    Args:
        urls (list): URLs to fetch.

    Returns:
        dict: Results and total execution time.
    """

    start_time = time.perf_counter()

    results = [
        sync_fetch_page(url)
        for url in urls
    ]

    elapsed_time = time.perf_counter() - start_time

    return {
        "results": results,
        "elapsed_time": elapsed_time,
    }


async def fetch_concurrent(urls, max_concurrency=5):
    """
    Fetch URLs concurrently using the asynchronous HTTPX client.

    Args:
        urls (list): URLs to fetch.
        max_concurrency (int): Maximum number of concurrent requests.

    Returns:
        dict: Results and total execution time.
    """

    start_time = time.perf_counter()

    results = await async_fetch_many(
        urls,
        max_concurrency=max_concurrency,
    )

    elapsed_time = time.perf_counter() - start_time

    return {
        "results": results,
        "elapsed_time": elapsed_time,
    }


def compare(urls):
    """
    Compare sequential and concurrent execution.

    Args:
        urls (list): URLs to benchmark.

    Returns:
        dict: Sequential results, concurrent results,
        and percentage improvement.
    """

    sequential = fetch_sequential(urls)

    concurrent = asyncio.run(
        fetch_concurrent(urls)
    )

    sequential_time = sequential["elapsed_time"]
    concurrent_time = concurrent["elapsed_time"]

    improvement_percent = (
        (sequential_time - concurrent_time)
        / sequential_time
        * 100
        if sequential_time > 0
        else 0
    )

    return {
        "sequential": sequential,
        "concurrent": concurrent,
        "improvement_percent": improvement_percent,
    }


def print_report(comparison):
    """Display the benchmark results."""

    sequential = comparison["sequential"]
    concurrent = comparison["concurrent"]

    print("\n" + "=" * 60)
    print("ASYNC WEB INTELLIGENCE COLLECTOR - BENCHMARK")
    print("=" * 60)

    print("\nWebsite:")
    print("https://www.imdb.com")

    print(f"\nURLs processed : {len(IMDB_URLS)}")

    print("\nExecution")
    print("-" * 60)

    print(
        f"Sequential     : "
        f"{sequential['elapsed_time']:.4f} sec"
    )

    print(
        f"Async          : "
        f"{concurrent['elapsed_time']:.4f} sec"
    )

    print(
        f"Improvement    : "
        f"{comparison['improvement_percent']:.2f}%"
    )

    print("\nSequential Results")
    print("-" * 60)

    for result in sequential["results"]:
        print(f"\nURL: {result['url']}")
        print(f"Status: {result['status']}")

        if "status_code" in result:
            print(f"HTTP Code: {result['status_code']}")
            print(f"Category: {result['category']}")

    print("\nConcurrent Results")
    print("-" * 60)

    for result in concurrent["results"]:
        print(f"\nURL: {result['url']}")
        print(f"Status: {result['status']}")

        if "status_code" in result:
            print(f"HTTP Code: {result['status_code']}")
            print(f"Category: {result['category']}")

    print("\n" + "=" * 60)


def main():
    """Run the benchmark for the selected IMDb URLs."""

    comparison = compare(IMDB_URLS)

    print_report(comparison)

    return comparison


if __name__ == "__main__":
    main()