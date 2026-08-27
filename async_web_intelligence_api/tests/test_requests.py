import pytest
import requests

from src.http.requests_client import (
    fetch_page,
    get_status_category
)


def test_successful_request(monkeypatch):

    class MockResponse:

        status_code = 200
        text = "<html>Test Page</html>"

        def raise_for_status(self):
            pass

    def mock_get(url, timeout):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_page("https://example.com")

    assert result["status"] == "success"
    assert result["status_code"] == 200
    assert result["category"] == "2xx - Success"
    assert result["content"] == "<html>Test Page</html>"


def test_404_error(monkeypatch):

    class MockResponse:

        status_code = 404
        text = ""

        def raise_for_status(self):
            raise requests.exceptions.HTTPError(
                "404 Client Error"
            )

    def mock_get(url, timeout):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_page("https://example.com/not-found")

    assert result["status"] == "failed"
    assert result["status_code"] == 404
    assert result["category"] == "4xx - Client Error"
    assert result["meaning"] == "The requested resource was not found"


def test_500_error(monkeypatch):

    class MockResponse:

        status_code = 500
        text = ""

        def raise_for_status(self):
            raise requests.exceptions.HTTPError(
                "500 Server Error"
            )

    def mock_get(url, timeout):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_page("https://example.com/server-error")

    assert result["status"] == "failed"
    assert result["status_code"] == 500
    assert result["category"] == "5xx - Server Error"
    assert result["meaning"] == "The server encountered an internal error"


def test_timeout(monkeypatch):

    def mock_get(url, timeout):
        raise requests.exceptions.Timeout()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_page("https://example.com")

    assert result["status"] == "failed"
    assert result["error_type"] == "Timeout"


def test_connection_error(monkeypatch):

    def mock_get(url, timeout):
        raise requests.exceptions.ConnectionError()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_page("https://example.com")

    assert result["status"] == "failed"
    assert result["error_type"] == "Connection Error"


def test_status_category_2xx():

    assert get_status_category(200) == "2xx - Success"
    assert get_status_category(201) == "2xx - Success"
    assert get_status_category(204) == "2xx - Success"


def test_status_category_4xx():

    assert get_status_category(400) == "4xx - Client Error"
    assert get_status_category(404) == "4xx - Client Error"
    assert get_status_category(429) == "4xx - Client Error"


def test_status_category_5xx():

    assert get_status_category(500) == "5xx - Server Error"
    assert get_status_category(502) == "5xx - Server Error"
    assert get_status_category(503) == "5xx - Server Error"


def test_request_timeout_value(monkeypatch):

    captured_timeout = {}

    class MockResponse:

        status_code = 200
        text = "Test"

        def raise_for_status(self):
            pass

    def mock_get(url, timeout):

        captured_timeout["value"] = timeout

        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    fetch_page("https://example.com")

    assert captured_timeout["value"] == 10


def test_unknown_status_category():

    assert get_status_category(700) == "Unknown Status"

def test_5xx_retries_then_succeeds(monkeypatch):
    attempts = {"count": 0}

    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code
            self.text = "success"

        def raise_for_status(self):
            if 400 <= self.status_code:
                raise requests.exceptions.HTTPError(
                    f"{self.status_code} Server Error"
                )

    def mock_get(url, timeout):
        attempts["count"] += 1

        if attempts["count"] < 3:
            return MockResponse(503)

        return MockResponse(200)

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_page(
        "https://example.com",
        max_retries=3,
        backoff_factor=0,
    )

    assert attempts["count"] == 3
    assert result["status"] == "success"
    assert result["status_code"] == 200


def test_4xx_is_not_retried(monkeypatch):
    attempts = {"count": 0}

    class MockResponse:
        status_code = 404
        text = ""

        def raise_for_status(self):
            raise requests.exceptions.HTTPError(
                "404 Client Error"
            )

    def mock_get(url, timeout):
        attempts["count"] += 1
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_page(
        "https://example.com/not-found",
        max_retries=3,
        backoff_factor=0,
    )

    assert attempts["count"] == 1
    assert result["status"] == "failed"
    assert result["status_code"] == 404


def test_timeout_retries_then_fails(monkeypatch):
    attempts = {"count": 0}

    def mock_get(url, timeout):
        attempts["count"] += 1
        raise requests.exceptions.Timeout()

    monkeypatch.setattr(requests, "get", mock_get)

    result = fetch_page(
        "https://example.com",
        max_retries=2,
        backoff_factor=0,
    )

    assert attempts["count"] == 3
    assert result["status"] == "failed"
    assert result["error_type"] == "Timeout"