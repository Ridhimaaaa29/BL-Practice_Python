import time

import requests


HTTP_STATUS_MEANINGS = {
    # 2xx - Success
    200: "Request completed successfully",
    201: "Resource created successfully",
    202: "Request accepted for processing",
    204: "Request successful with no response content",

    # 3xx - Redirection
    301: "Resource permanently redirected",
    302: "Resource temporarily redirected",
    304: "Resource has not been modified",

    # 4xx - Client Error
    400: "The server could not understand the request",
    401: "Authentication is required",
    403: "Access to the requested resource is forbidden",
    404: "The requested resource was not found",
    405: "The HTTP method is not allowed",
    408: "The request timed out",
    409: "The request conflicts with the current state of the resource",
    429: "Too many requests were sent",

    # 5xx - Server Error
    500: "The server encountered an internal error",
    501: "The server does not support the requested functionality",
    502: "The server received an invalid response from another server",
    503: "The server is temporarily unavailable",
    504: "The server did not receive a timely response",
}


def get_status_category(status_code):
    """Determine the HTTP status-code category."""

    if 200 <= status_code < 300:
        return "2xx - Success"

    if 300 <= status_code < 400:
        return "3xx - Redirection"

    if 400 <= status_code < 500:
        return "4xx - Client Error"

    if 500 <= status_code < 600:
        return "5xx - Server Error"

    return "Unknown Status"


def fetch_page(url, timeout=10, max_retries=3, backoff_factor=1):
    """
    Fetch a web page synchronously using requests.

    Retries are attempted only for:
    - Timeout errors
    - Connection errors
    - HTTP 5xx responses

    4xx responses are not retried.

    Args:
        url (str): URL of the page to fetch.
        timeout (int): Maximum time in seconds to wait for a response.
        max_retries (int): Maximum number of retries after the first attempt.
        backoff_factor (int): Base delay used for exponential backoff.

    Returns:
        dict: Response information including status, code, category,
              meaning, and content when successful.
    """

    attempt = 0

    while True:
        try:
            response = requests.get(
                url,
                timeout=timeout,
            )

            status_code = response.status_code
            category = get_status_category(status_code)

            # Retry only server-side 5xx errors.
            if 500 <= status_code < 600:

                if attempt < max_retries:
                    time.sleep(
                        backoff_factor * (2 ** attempt)
                    )
                    attempt += 1
                    continue

            # Raise HTTPError for 4xx and 5xx responses.
            response.raise_for_status()

            return {
                "url": url,
                "status": "success",
                "status_code": status_code,
                "category": category,
                "meaning": HTTP_STATUS_MEANINGS.get(
                    status_code,
                    "Request completed successfully",
                ),
                "content": response.text,
            }

        except requests.exceptions.HTTPError as error:

            status_code = response.status_code

            return {
                "url": url,
                "status": "failed",
                "status_code": status_code,
                "category": get_status_category(status_code),
                "meaning": HTTP_STATUS_MEANINGS.get(
                    status_code,
                    "HTTP error occurred",
                ),
                "error_type": "HTTPError",
                "error": str(error),
            }

        except requests.exceptions.Timeout:

            if attempt < max_retries:
                time.sleep(
                    backoff_factor * (2 ** attempt)
                )
                attempt += 1
                continue

            return {
                "url": url,
                "status": "failed",
                "error_type": "Timeout",
                "meaning": (
                    f"The server did not respond within "
                    f"{timeout} seconds after {max_retries + 1} attempts"
                ),
            }

        except requests.exceptions.ConnectionError as error:

            if attempt < max_retries:
                time.sleep(
                    backoff_factor * (2 ** attempt)
                )
                attempt += 1
                continue

            return {
                "url": url,
                "status": "failed",
                "error_type": "Connection Error",
                "meaning": (
                    "Could not establish a connection to the server "
                    f"after {max_retries + 1} attempts"
                ),
                "error": str(error),
            }

        except requests.exceptions.RequestException as error:

            return {
                "url": url,
                "status": "failed",
                "error_type": "Request Error",
                "meaning": str(error),
            }