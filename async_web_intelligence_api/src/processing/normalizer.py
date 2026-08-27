"""Normalize parsed movie data into a consistent format."""

from .parser import parse_movie, parse_omdb_movie


def _normalize_text(value):
    """Normalize a text value."""

    if value is None:
        return None

    value = str(value).strip()

    return value or None


def _normalize_genre(value):
    """Normalize genre values into a comma-separated string."""

    if value is None:
        return None

    if isinstance(value, list):
        value = ", ".join(
            str(item).strip()
            for item in value
            if str(item).strip()
        )

    value = str(value).strip()

    return value or None


def _normalize_rating(value):
    """Convert rating to float when possible."""

    if value is None:
        return None

    try:
        return float(value)

    except (TypeError, ValueError):
        return None


def _normalize_release_date(value):
    """Normalize the release-date value."""

    return _normalize_text(value)


def normalize_movie_data(data):
    """
    Convert parsed movie data into the public movie format.

    Returns:
        dict: Normalized movie information.
    """

    return {
        "movie_name": _normalize_text(
            data.get("title")
        ),
        "genre": _normalize_genre(
            data.get("genre")
        ),
        "rating": _normalize_rating(
            data.get("rating")
        ),
        "release_date": _normalize_release_date(
            data.get("release_date")
        ),
        "movie_url": _normalize_text(
            data.get("url")
        ),
    }


def normalize_crawl_result(raw_result):
    """
    Normalize a Crawl4AI result.
    """

    url = raw_result.get("url")

    if not raw_result.get("success"):
        return {
            "url": url,
            "status": "failed",
            "data": {},
            "error": raw_result.get(
                "error",
                "Crawl failed.",
            ),
        }

    parsed_data = parse_movie(
        raw_result.get("html", ""),
        url,
    )

    normalized_data = normalize_movie_data(
        parsed_data
    )

    return {
        "url": url,
        "title": normalized_data["movie_name"],
        "status": "success",
        "data": {
            "genre": normalized_data["genre"],
            "rating": normalized_data["rating"],
            "release_date": normalized_data[
                "release_date"
            ],
            "url": normalized_data["movie_url"],
        },
    }


def normalize_api_result(http_result, movie_url):
    """
    Normalize an OMDb API result while preserving
    the selected IMDb URL.
    """

    if http_result.get("status") != "success":
        return {
            "url": movie_url,
            "title": None,
            "status": "failed",
            "data": {},
            "error": (
                http_result.get("error_type")
                or http_result.get("meaning")
                or "OMDb API request failed."
            ),
        }

    try:
        parsed_data = parse_omdb_movie(
            http_result.get("content", ""),
            movie_url,
        )

    except ValueError as error:
        return {
            "url": movie_url,
            "title": None,
            "status": "failed",
            "data": {},
            "error": str(error),
        }

    normalized_data = normalize_movie_data(
        parsed_data
    )

    return {
        "url": movie_url,
        "title": normalized_data["movie_name"],
        "status": "success",
        "data": {
            "genre": normalized_data["genre"],
            "rating": normalized_data["rating"],
            "release_date": normalized_data[
                "release_date"
            ],
            "url": normalized_data["movie_url"],
        },
    }


def summarize_results(results):
    """Summarize successful and failed results."""

    successful = sum(
        item.get("status") == "success"
        for item in results
    )

    return {
        "total_urls": len(results),
        "successful": successful,
        "failed": len(results) - successful,
        "results": results,
    }