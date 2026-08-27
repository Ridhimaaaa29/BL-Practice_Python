import httpx
import pytest

from src.omdb.omdb_client import fetch_movie_by_imdb_id


@pytest.mark.asyncio
async def test_fetch_movie_by_imdb_id_success(monkeypatch):
    """Test a successful OMDb API request."""

    class MockResponse:
        status_code = 200
        text = (
            '{"Response":"True",'
            '"Title":"Interstellar",'
            '"Genre":"Adventure, Drama, Sci-Fi",'
            '"imdbRating":"8.7",'
            '"Released":"07 Nov 2014"}'
        )

        def raise_for_status(self):
            pass

    async def mock_get(self, url, params):
        assert url == "https://www.omdbapi.com/"
        assert params["i"] == "tt0816692"
        assert params["r"] == "json"
        assert params["plot"] == "short"
        assert params["apikey"] == "test-api-key"

        return MockResponse()

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get,
    )

    monkeypatch.setenv(
        "OMDB_API_KEY",
        "test-api-key",
    )

    result = await fetch_movie_by_imdb_id(
        "tt0816692"
    )

    assert result["status"] == "success"
    assert result["status_code"] == 200
    assert "Interstellar" in result["content"]


@pytest.mark.asyncio
async def test_missing_api_key(monkeypatch):
    """Test configuration error when the API key is missing."""

    monkeypatch.delenv(
        "OMDB_API_KEY",
        raising=False,
    )

    result = await fetch_movie_by_imdb_id(
        "tt0816692"
    )

    assert result["status"] == "failed"
    assert result["error_type"] == "ConfigurationError"


@pytest.mark.asyncio
async def test_omdb_http_error(monkeypatch):
    """Test HTTP error handling."""

    class MockResponse:

        status_code = 500
        text = ""

        def raise_for_status(self):
            raise httpx.HTTPStatusError(
                "500 Server Error",
                request=httpx.Request(
                    "GET",
                    "https://www.omdbapi.com/",
                ),
                response=httpx.Response(500),
            )

    async def mock_get(self, url, params):
        return MockResponse()

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get,
    )

    monkeypatch.setenv(
        "OMDB_API_KEY",
        "test-api-key",
    )

    result = await fetch_movie_by_imdb_id(
        "tt0816692"
    )

    assert result["status"] == "failed"
    assert result["status_code"] == 500
    assert result["error_type"] == "HTTPStatusError"


@pytest.mark.asyncio
async def test_omdb_timeout(monkeypatch):
    """Test OMDb timeout handling."""

    async def mock_get(self, url, params):
        raise httpx.TimeoutException(
            "Request timed out"
        )

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get,
    )

    monkeypatch.setenv(
        "OMDB_API_KEY",
        "test-api-key",
    )

    result = await fetch_movie_by_imdb_id(
        "tt0816692"
    )

    assert result["status"] == "failed"
    assert result["error_type"] == "Timeout"


@pytest.mark.asyncio
async def test_omdb_connection_error(monkeypatch):
    """Test OMDb connection error handling."""

    async def mock_get(self, url, params):
        raise httpx.ConnectError(
            "Connection failed"
        )

    monkeypatch.setattr(
        httpx.AsyncClient,
        "get",
        mock_get,
    )

    monkeypatch.setenv(
        "OMDB_API_KEY",
        "test-api-key",
    )

    result = await fetch_movie_by_imdb_id(
        "tt0816692"
    )

    assert result["status"] == "failed"
    assert result["error_type"] == "ConnectionError"