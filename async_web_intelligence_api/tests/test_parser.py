import pytest

from src.crawler.crawler import is_waf_challenge
from src.processing.normalizer import (
    normalize_api_result,
    normalize_crawl_result,
    normalize_movie_data,
    summarize_results,
)
from src.processing.parser import (
    parse_movie,
    parse_omdb_movie,
)


def test_parse_movie_extracts_required_fields_from_json_ld():
    html = """
    <html>
        <head>
            <title>Interstellar - IMDb</title>

            <script type="application/ld+json">
            {
                "@type": "Movie",
                "name": "Interstellar",
                "genre": ["Adventure", "Drama", "Sci-Fi"],
                "datePublished": "2014-11-07",
                "aggregateRating": {
                    "ratingValue": "8.7"
                }
            }
            </script>
        </head>
    </html>
    """

    result = parse_movie(
        html,
        "https://www.imdb.com/title/tt0816692/",
    )

    assert result["title"] == "Interstellar"
    assert result["genre"] == "Adventure, Drama, Sci-Fi"
    assert result["rating"] == "8.7"
    assert result["release_date"] == "2014-11-07"
    assert result["url"] == (
        "https://www.imdb.com/title/tt0816692/"
    )


def test_parse_movie_handles_missing_fields():

    html = """
    <html>
        <head>
            <title>Interstellar - IMDb</title>
        </head>
    </html>
    """

    result = parse_movie(
        html,
        "https://www.imdb.com/title/tt0816692/",
    )

    assert result["title"] == "Interstellar"
    assert result["genre"] is None
    assert result["rating"] is None
    assert result["release_date"] is None
    assert result["url"] == (
        "https://www.imdb.com/title/tt0816692/"
    )


def test_parse_omdb_movie_uses_required_fields():

    content = """
    {
        "Response": "True",
        "Title": "Interstellar",
        "Genre": "Adventure, Drama, Sci-Fi",
        "imdbRating": "8.7",
        "Released": "07 Nov 2014"
    }
    """

    movie = parse_omdb_movie(
        content,
        "https://www.imdb.com/title/tt0816692/",
    )

    assert movie["title"] == "Interstellar"
    assert movie["genre"] == "Adventure, Drama, Sci-Fi"
    assert movie["rating"] == "8.7"
    assert movie["release_date"] == "07 Nov 2014"
    assert movie["url"] == (
        "https://www.imdb.com/title/tt0816692/"
    )


def test_parse_omdb_movie_rejects_unsuccessful_response():

    content = """
    {
        "Response": "False",
        "Error": "Movie not found!"
    }
    """

    with pytest.raises(ValueError, match="Movie not found"):
        parse_omdb_movie(
            content,
            "https://www.imdb.com/title/tt0816692/",
        )


def test_normalize_movie_data():

    parsed_data = {
        "title": " Interstellar ",
        "genre": ["Adventure", "Drama", "Sci-Fi"],
        "rating": "8.7",
        "release_date": "07 Nov 2014",
        "url": " https://www.imdb.com/title/tt0816692/ ",
    }

    result = normalize_movie_data(parsed_data)

    assert result["movie_name"] == "Interstellar"
    assert result["genre"] == "Adventure, Drama, Sci-Fi"
    assert result["rating"] == 8.7
    assert result["release_date"] == "07 Nov 2014"
    assert result["movie_url"] == (
        "https://www.imdb.com/title/tt0816692/"
    )


def test_normalize_crawl_result_success():

    raw_result = {
        "url": "https://example.test/title",
        "success": True,
        "html": """
        <title>Interstellar - IMDb</title>
        <script type="application/ld+json">
        {
            "@type": "Movie",
            "name": "Interstellar",
            "genre": ["Adventure", "Drama"],
            "datePublished": "2014-11-07",
            "aggregateRating": {
                "ratingValue": "8.7"
            }
        }
        </script>
        """,
    }

    result = normalize_crawl_result(raw_result)

    assert result["status"] == "success"
    assert result["title"] == "Interstellar"
    assert result["data"]["genre"] == "Adventure, Drama"
    assert result["data"]["rating"] == 8.7
    assert result["data"]["release_date"] == "2014-11-07"
    assert result["data"]["url"] == "https://example.test/title"


def test_normalize_crawl_result_failure():

    raw_result = {
        "url": "https://example.test/title",
        "success": False,
        "error": "HTTP 404",
    }

    result = normalize_crawl_result(raw_result)

    assert result["status"] == "failed"
    assert result["url"] == "https://example.test/title"
    assert result["data"] == {}
    assert result["error"] == "HTTP 404"


def test_normalize_api_result_success():

    http_result = {
        "status": "success",
        "content": """
        {
            "Response": "True",
            "Title": "Interstellar",
            "Genre": "Adventure, Drama, Sci-Fi",
            "imdbRating": "8.7",
            "Released": "07 Nov 2014"
        }
        """,
    }

    result = normalize_api_result(
        http_result,
        "https://www.imdb.com/title/tt0816692/",
    )

    assert result["status"] == "success"
    assert result["title"] == "Interstellar"
    assert result["data"]["genre"] == (
        "Adventure, Drama, Sci-Fi"
    )
    assert result["data"]["rating"] == 8.7
    assert result["data"]["release_date"] == "07 Nov 2014"
    assert result["data"]["url"] == (
        "https://www.imdb.com/title/tt0816692/"
    )


def test_normalize_api_result_reports_api_error():

    http_result = {
        "status": "success",
        "content": """
        {
            "Response": "False",
            "Error": "Movie not found!"
        }
        """,
    }

    result = normalize_api_result(
        http_result,
        "https://www.imdb.com/title/tt0816692/",
    )

    assert result["status"] == "failed"
    assert "Movie not found" in result["error"]


def test_normalize_and_summarize_partial_failure():

    success = normalize_crawl_result(
        {
            "url": "https://example.test/one",
            "success": True,
            "html": """
            <title>One - IMDb</title>
            <script type="application/ld+json">
            {
                "@type": "Movie",
                "name": "One",
                "genre": ["Drama"],
                "datePublished": "2020-01-01",
                "aggregateRating": {
                    "ratingValue": "7.0"
                }
            }
            </script>
            """,
        }
    )

    failure = normalize_crawl_result(
        {
            "url": "https://example.test/two",
            "success": False,
            "error": "HTTP 404",
        }
    )

    summary = summarize_results(
        [success, failure]
    )

    assert summary["total_urls"] == 2
    assert summary["successful"] == 1
    assert summary["failed"] == 1
    assert failure["error"] == "HTTP 404"


def test_waf_challenge_detection():

    assert is_waf_challenge(
        "AWS WAF: verify you are human"
    )

    assert is_waf_challenge(
        '<div id="challenge-container"></div>'
    )

    assert not is_waf_challenge(
        "<title>Interstellar - IMDb</title>"
    )