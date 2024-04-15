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
        "https://github.com/",
        "https://gitlab.com/",
    ]

    pages = await fetch_all_pages(urls)

    for url, page in zip(urls, pages):
        print(f"Page from {url}:")
        print(page)
        print("-----------------------------")


if __name__ == "__main__":
    asyncio.run(main())
