import pytest
import httpx

from src.http.httpx_client import (
    fetch_page,
    get_status_category
)


@pytest.mark.asyncio
async def test_successful_request(monkeypatch):

    class MockResponse:

        status_code = 200
        text = "<html>Test Page</html>"

        def raise_for_status(self):
            pass

    async def mock_get(self, url):
        return MockResponse()

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get
    )

    result = await fetch_page("https://example.com")

    assert result["status"] == "success"
    assert result["status_code"] == 200
    assert result["category"] == "2xx - Success"
    assert result["content"] == "<html>Test Page</html>"


@pytest.mark.asyncio
async def test_404_error(monkeypatch):

    class MockResponse:

        status_code = 404
        text = ""

        def raise_for_status(self):
            raise httpx.HTTPStatusError(
                "404 Client Error",
                request=httpx.Request(
                    "GET",
                    "https://example.com/not-found"
                ),
                response=httpx.Response(
                    404
                )
            )

    async def mock_get(self, url):
        return MockResponse()

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get
    )

    result = await fetch_page(
        "https://example.com/not-found"
    )

    assert result["status"] == "failed"
    assert result["status_code"] == 404
    assert result["category"] == "4xx - Client Error"
    assert result["meaning"] == "The requested resource was not found"


@pytest.mark.asyncio
async def test_500_error(monkeypatch):

    class MockResponse:

        status_code = 500
        text = ""

        def raise_for_status(self):
            raise httpx.HTTPStatusError(
                "500 Server Error",
                request=httpx.Request(
                    "GET",
                    "https://example.com/server-error"
                ),
                response=httpx.Response(
                    500
                )
            )

    async def mock_get(self, url):
        return MockResponse()

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get
    )

    result = await fetch_page(
        "https://example.com/server-error"
    )

    assert result["status"] == "failed"
    assert result["status_code"] == 500
    assert result["category"] == "5xx - Server Error"
    assert result["meaning"] == "The server encountered an internal error"


@pytest.mark.asyncio
async def test_timeout(monkeypatch):

    async def mock_get(self, url):
        raise httpx.TimeoutException(
            "Request timed out"
        )

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get
    )

    result = await fetch_page(
        "https://example.com"
    )

    assert result["status"] == "failed"
    assert result["error_type"] == "Timeout"


@pytest.mark.asyncio
async def test_connection_error(monkeypatch):

    async def mock_get(self, url):
        raise httpx.ConnectError(
            "Connection failed"
        )

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get
    )

    result = await fetch_page(
        "https://example.com"
    )

    assert result["status"] == "failed"
    assert result["error_type"] == "Connection Error"


def test_status_category_2xx():

    assert get_status_category(200) == "2xx - Success"
    assert get_status_category(201) == "2xx - Success"
    assert get_status_category(204) == "2xx - Success"


def test_status_category_4xx():

    assert get_status_category(400) == "4xx - Client Error"
    assert get_status_category(403) == "4xx - Client Error"
    assert get_status_category(404) == "4xx - Client Error"


def test_status_category_5xx():

    assert get_status_category(500) == "5xx - Server Error"
    assert get_status_category(502) == "5xx - Server Error"
    assert get_status_category(503) == "5xx - Server Error"


def test_unknown_status_category():

    assert get_status_category(700) == "Unknown Status"

@pytest.mark.asyncio
async def test_5xx_retries_then_succeeds(monkeypatch):
    attempts = {"count": 0}

    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code
            self.text = "success"

        def raise_for_status(self):
            if 400 <= self.status_code:
                raise httpx.HTTPStatusError(
                    f"{self.status_code} Server Error",
                    request=httpx.Request(
                        "GET",
                        "https://example.com",
                    ),
                    response=httpx.Response(
                        self.status_code
                    ),
                )

    async def mock_get(self, url):
        attempts["count"] += 1

        if attempts["count"] < 3:
            return MockResponse(503)

        return MockResponse(200)

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get,
    )

    result = await fetch_page(
        "https://example.com",
        max_retries=3,
        backoff_factor=0,
    )

    assert attempts["count"] == 3
    assert result["status"] == "success"
    assert result["status_code"] == 200


@pytest.mark.asyncio
async def test_4xx_is_not_retried(monkeypatch):
    attempts = {"count": 0}

    class MockResponse:

        status_code = 404
        text = ""

        def raise_for_status(self):
            raise httpx.HTTPStatusError(
                "404 Client Error",
                request=httpx.Request(
                    "GET",
                    "https://example.com/not-found",
                ),
                response=httpx.Response(404),
            )

    async def mock_get(self, url):
        attempts["count"] += 1
        return MockResponse()

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get,
    )

    result = await fetch_page(
        "https://example.com/not-found",
        max_retries=3,
        backoff_factor=0,
    )

    assert attempts["count"] == 1
    assert result["status"] == "failed"
    assert result["status_code"] == 404


@pytest.mark.asyncio
async def test_timeout_retries_then_fails(monkeypatch):
    attempts = {"count": 0}

    async def mock_get(self, url):
        attempts["count"] += 1
        raise httpx.TimeoutException(
            "Request timed out"
        )

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get,
    )

    result = await fetch_page(
        "https://example.com",
        max_retries=2,
        backoff_factor=0,
    )

    assert attempts["count"] == 3
    assert result["status"] == "failed"
    assert result["error_type"] == "Timeout"