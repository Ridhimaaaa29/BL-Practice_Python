"""Coordinate OMDb access, parsing, and normalization."""

import asyncio

from src.omdb.omdb_client import fetch_movie_by_imdb_id
from src.processing.normalizer import (
    normalize_api_result,
)


IMDB_MOVIES = [
    (
        "Interstellar",
        "tt0816692",
        "https://www.imdb.com/title/tt0816692/",
    ),
    (
        "Inception",
        "tt1375666",
        "https://www.imdb.com/title/tt1375666/",
    ),
    (
        "The Matrix",
        "tt0133093",
        "https://www.imdb.com/title/tt0133093/",
    ),
]


async def collect_movies():
    """
    Fetch, parse, and normalize the selected movies
    through the approved OMDb API.
    """

    responses = await asyncio.gather(
        *(
            fetch_movie_by_imdb_id(imdb_id)
            for _, imdb_id, _ in IMDB_MOVIES
        )
    )

    results = []

    for response, (_, _, movie_url) in zip(
        responses,
        IMDB_MOVIES,
    ):

        results.append(
            normalize_api_result(
                response,
                movie_url,
            )
        )

    return results


async def main():
    results = await collect_movies()

    for result in results:

        print("\n" + "=" * 60)

        print("Movie:", result.get("title"))
        print("Status:", result.get("status"))

        if result.get("status") == "success":

            data = result["data"]

            print(
                "Genre:",
                data.get("genre"),
            )

            print(
                "Rating:",
                data.get("rating"),
            )

            print(
                "Release Date:",
                data.get("release_date"),
            )

            print(
                "Movie URL:",
                data.get("url"),
            )

        else:

            print(
                "Error:",
                result.get("error"),
            )

        print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())