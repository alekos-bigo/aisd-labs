import asyncio
from aiohttp import ClientSession


async def fetch_page(session: ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


async def fetch_all_pages(urls: list[str]):
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch_page(session, url)) for url in urls]
        pages = await asyncio.gather(*tasks)
        return pages


async def main():
    urls = [
        "https://phet-dev.colorado.edu/html/build-an-atom/0.0.0-3/simple-text-only-test-page.html",
        "https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html",
    ]

    pages = await fetch_all_pages(urls)

    for url, page in zip(urls, pages):
        print(f"Страница: {url}:")
        print(page)
        print("-----------------------------")
        print("\n")


if __name__ == "__main__":
    asyncio.run(main())
