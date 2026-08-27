import asyncio
import time

import pytest

from src.http.httpx_client import async_fetch_many


@pytest.mark.asyncio
async def test_concurrent_fetching(monkeypatch):

    async def mock_fetch_page(url):

        await asyncio.sleep(1)

        return {
            "url": url,
            "status": "success",
            "status_code": 200,
            "category": "2xx - Success",
            "meaning": "Request completed successfully",
            "content": "test content",
        }

    monkeypatch.setattr(
        "src.http.httpx_client.fetch_page",
        mock_fetch_page,
    )

    urls = [
        "https://example.com/1",
        "https://example.com/2",
        "https://example.com/3",
    ]

    start_time = time.perf_counter()

    results = await async_fetch_many(urls)

    elapsed = time.perf_counter() - start_time

    assert len(results) == 3

    assert all(
        result["status"] == "success"
        for result in results
    )

    # Three 1-second requests should complete concurrently
    # in significantly less than 3 seconds.
    assert elapsed < 2


@pytest.mark.asyncio
async def test_partial_failure(monkeypatch):

    async def mock_fetch_page(url):

        if "failed" in url:
            raise Exception("Simulated request failure")

        return {
            "url": url,
            "status": "success",
            "status_code": 200,
            "category": "2xx - Success",
            "meaning": "Request completed successfully",
            "content": "test content",
        }

    monkeypatch.setattr(
        "src.http.httpx_client.fetch_page",
        mock_fetch_page,
    )

    urls = [
        "https://example.com/success-1",
        "https://example.com/failed",
        "https://example.com/success-2",
    ]

    results = await async_fetch_many(urls)

    assert len(results) == 3

    assert results[0]["status"] == "success"

    assert results[1]["status"] == "failed"
    assert results[1]["error_type"] == "Exception"
    assert results[1]["error"] == "Simulated request failure"

    assert results[2]["status"] == "success"


@pytest.mark.asyncio
async def test_multiple_urls_preserve_order(monkeypatch):

    async def mock_fetch_page(url):

        return {
            "url": url,
            "status": "success",
            "status_code": 200,
            "category": "2xx - Success",
            "meaning": "Request completed successfully",
            "content": "test content",
        }

    monkeypatch.setattr(
        "src.http.httpx_client.fetch_page",
        mock_fetch_page,
    )

    urls = [
        "https://example.com/1",
        "https://example.com/2",
        "https://example.com/3",
    ]

    results = await async_fetch_many(urls)

    returned_urls = [
        result["url"]
        for result in results
    ]

    assert returned_urls == urls


@pytest.mark.asyncio
async def test_empty_url_list():

    results = await async_fetch_many([])

    assert results == []