"""Crawl4AI integration for Task 5."""

import asyncio

from crawl4ai import AsyncWebCrawler


IMDB_URLS = [
    "https://www.imdb.com/title/tt0816692/",  # Interstellar
    "https://www.imdb.com/title/tt1375666/",  # Inception
    "https://www.imdb.com/title/tt0133093/",  # The Matrix
]


def is_waf_challenge(html):
    """
    Detect an IMDb bot-verification/WAF challenge page.

    The function only detects the challenge and does not attempt
    to bypass it.
    """

    page_text = (html or "").lower()

    challenge_markers = (
        "challenge-container",
        "awswafintegration",
        "aws waf",
        "verify that you're not a robot",
        "not a robot",
        "bot verification",
        "captcha",
    )

    return any(
        marker in page_text
        for marker in challenge_markers
    )


async def crawl_page(url):
    """
    Crawl a single webpage using Crawl4AI.

    Returns:
        dict: Crawl result containing URL, success status,
              HTML, Markdown, links, metadata, and errors if any.
    """

    try:
        async with AsyncWebCrawler() as crawler:

            result = await crawler.arun(url=url)

            html = result.html or ""
            waf_challenge = is_waf_challenge(html)

            if waf_challenge:
                return {
                    "url": url,
                    "success": False,
                    "html": html,
                    "markdown": result.markdown,
                    "links": result.links,
                    "metadata": result.metadata,
                    "error_type": "BotVerificationChallenge",
                    "error": (
                        "IMDb returned a bot-verification challenge "
                        "instead of the requested movie content."
                    ),
                }

            return {
                "url": url,
                "success": result.success,
                "html": html,
                "markdown": result.markdown,
                "links": result.links,
                "metadata": result.metadata,
            }

    except Exception as error:
        return {
            "url": url,
            "success": False,
            "error_type": type(error).__name__,
            "error": str(error),
        }


async def crawl_all_pages(urls):
    """
    Crawl multiple webpages concurrently using Crawl4AI.

    Results remain in the same order as the input URLs.
    Individual failures do not stop the remaining crawls.
    """

    results = await asyncio.gather(
        *(crawl_page(url) for url in urls),
        return_exceptions=True,
    )

    processed_results = []

    for url, result in zip(urls, results):

        if isinstance(result, Exception):
            processed_results.append({
                "url": url,
                "success": False,
                "error_type": type(result).__name__,
                "error": str(result),
            })

        else:
            processed_results.append(result)

    return processed_results