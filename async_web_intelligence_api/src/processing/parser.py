"""Parse movie data from IMDb HTML or approved OMDb JSON."""

import json
import re
from html.parser import HTMLParser


class _TitleParser(HTMLParser):
    """Extract the HTML title."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag.lower() == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


def _extract_json_ld(html):
    """Extract JSON-LD blocks from HTML."""

    scripts = re.findall(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>'
        r'(.*?)'
        r'</script>',
        html or "",
        flags=re.IGNORECASE | re.DOTALL,
    )

    objects = []

    for script in scripts:
        try:
            data = json.loads(script.strip())

            if isinstance(data, list):
                objects.extend(data)
            else:
                objects.append(data)

        except json.JSONDecodeError:
            continue

    return objects


def _find_movie_json_ld(html):
    """Find a Movie object inside JSON-LD data."""

    for item in _extract_json_ld(html):

        if not isinstance(item, dict):
            continue

        item_type = item.get("@type")

        if item_type == "Movie":
            return item

        if isinstance(item_type, list) and "Movie" in item_type:
            return item

        graph = item.get("@graph")

        if isinstance(graph, list):
            for graph_item in graph:

                if not isinstance(graph_item, dict):
                    continue

                graph_type = graph_item.get("@type")

                if graph_type == "Movie":
                    return graph_item

                if (
                    isinstance(graph_type, list)
                    and "Movie" in graph_type
                ):
                    return graph_item

    return None


def parse_movie(html, url):
    """
    Parse movie information from IMDb HTML.

    Missing fields are returned as None.
    """

    html = html or ""

    title_parser = _TitleParser()
    title_parser.feed(html)

    title = re.sub(
        r"\s*-\s*IMDb\s*$",
        "",
        title_parser.title,
        flags=re.IGNORECASE,
    ).strip()

    data = {
        "title": title or None,
        "genre": None,
        "rating": None,
        "release_date": None,
        "url": url,
    }

    movie_data = _find_movie_json_ld(html)

    if movie_data:

        data["title"] = (
            movie_data.get("name")
            or data["title"]
        )

        genre = movie_data.get("genre")

        if isinstance(genre, list):
            data["genre"] = ", ".join(
                str(item) for item in genre
            )
        elif genre:
            data["genre"] = str(genre)

        aggregate_rating = movie_data.get(
            "aggregateRating"
        )

        if isinstance(aggregate_rating, dict):
            data["rating"] = aggregate_rating.get(
                "ratingValue"
            )

        data["release_date"] = (
            movie_data.get("datePublished")
            or movie_data.get("releaseDate")
        )

    # Fallback: rating
    if data["rating"] is None:

        match = re.search(
            r'"ratingValue"\s*:\s*"?([\d.]+)',
            html,
            flags=re.IGNORECASE,
        )

        if match:
            data["rating"] = match.group(1)

    # Fallback: genre
    if data["genre"] is None:

        match = re.search(
            r'"genre"\s*:\s*(\[[^\]]+\]|"[^"]+")',
            html,
            flags=re.IGNORECASE,
        )

        if match:
            try:
                value = json.loads(match.group(1))

                if isinstance(value, list):
                    data["genre"] = ", ".join(
                        str(item) for item in value
                    )
                else:
                    data["genre"] = str(value)

            except json.JSONDecodeError:
                pass

    # Fallback: release date
    if data["release_date"] is None:

        match = re.search(
            r'"(?:datePublished|releaseDate)"\s*:\s*"([^"]+)"',
            html,
            flags=re.IGNORECASE,
        )

        if match:
            data["release_date"] = match.group(1)

    return data


def parse_omdb_movie(content, movie_url):
    """
    Parse an OMDb JSON response into the required movie fields.

    The original IMDb URL is preserved.
    """

    try:
        payload = json.loads(content)

    except json.JSONDecodeError as error:
        raise ValueError(
            "Invalid JSON response from OMDb."
        ) from error

    if payload.get("Response") != "True":
        raise ValueError(
            payload.get(
                "Error",
                "OMDb returned an unsuccessful response.",
            )
        )

    return {
        "title": payload.get("Title"),
        "genre": payload.get("Genre"),
        "rating": payload.get("imdbRating"),
        "release_date": payload.get("Released"),
        "url": movie_url,
    }