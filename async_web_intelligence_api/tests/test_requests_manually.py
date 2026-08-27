from src.http.requests_client import fetch_page


IMDB_URLS = [
    "https://www.imdb.com/title/tt0816692/",  # Interstellar
    "https://www.imdb.com/title/tt1375666/",  # Inception
    "https://www.imdb.com/title/tt0133093/"   # The Matrix
]


for url in IMDB_URLS:
    print("\n" + "=" * 70)

    result = fetch_page(url)

    print("URL:", result["url"])
    print("Status:", result["status"])

    if "status_code" in result:
        print("HTTP Code:", result["status_code"])
        print("Category:", result["category"])
        print("Meaning:", result["meaning"])

    if result["status"] == "success":
        print("Page fetched successfully.")
        print("Content length:", len(result["content"]))

    else:
        print("Error Type:", result.get("error_type"))
        print("Error:", result.get("error"))

    print("=" * 70)