import asyncio

from src.crawler.crawler import (
    crawl_all_pages,
    IMDB_URLS,
)


async def main():
    results = await crawl_all_pages(IMDB_URLS)

    for result in results:

        print("\n" + "=" * 70)
        print("URL:", result["url"])
        print("Success:", result.get("success"))

        if result.get("success"):

            html = result.get("html") or ""
            markdown = result.get("markdown") or ""
            links = result.get("links") or []
            metadata = result.get("metadata") or {}

            print("HTML length:", len(html))
            print("Markdown length:", len(markdown))
            print("Number of links:", len(links))
            print("Metadata:", metadata)

        else:

            print("Error Type:", result.get("error_type"))
            print("Error:", result.get("error"))

        print("=" * 70)


if __name__ == "__main__":
    asyncio.run(main())