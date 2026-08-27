"""OMDb API client for approved movie-data access."""

import os

import httpx


OMDB_BASE_URL = "https://www.omdbapi.com/"


async def fetch_movie_by_imdb_id(imdb_id, timeout=10):
    """
    Fetch movie information from OMDb using an IMDb ID.

    Args:
        imdb_id (str): IMDb title ID, for example ``xxxxxxxxxx``.
        timeout (int): Maximum time to wait for the API response.

    Returns:
        dict: Raw OMDb API response information.
    """

    api_key = os.getenv("OMDB_API_KEY")

    if not api_key:
        return {
            "status": "failed",
            "error_type": "ConfigurationError",
            "meaning": "OMDB_API_KEY environment variable is not set.",
        }

    params = {
        "apikey": api_key,
        "i": imdb_id,
        "r": "json",
        "plot": "short",
    }

    try:
        async with httpx.AsyncClient(timeout=timeout) as client:

            response = await client.get(
                OMDB_BASE_URL,
                params=params,
            )

        response.raise_for_status()

        return {
            "status": "success",
            "status_code": response.status_code,
            "content": response.text,
        }

    except httpx.HTTPStatusError as error:
        return {
            "status": "failed",
            "status_code": error.response.status_code,
            "error_type": "HTTPStatusError",
            "error": str(error),
        }

    except httpx.TimeoutException:
        return {
            "status": "failed",
            "error_type": "Timeout",
            "meaning": f"The OMDb API did not respond within {timeout} seconds.",
        }

    except httpx.ConnectError:
        return {
            "status": "failed",
            "error_type": "ConnectionError",
            "meaning": "Could not establish a connection to the OMDb API.",
        }

    except httpx.RequestError as error:
        return {
            "status": "failed",
            "error_type": "RequestError",
            "error": str(error),
        }