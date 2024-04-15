import aiohttp
import asyncio

from settings import ACCESS_TOKEN


class VKClient:
    def __init__(self, access_token: str):
        self.access_token = access_token
        self.base_url = 'https://api.vk.com/method/'
        self.lang = "ru"
        self.v = "5.199"

    async def get_user_info(self, user_id: str):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_url}users.get"
            params = {
                "user_ids": user_id,
                "access_token": self.access_token,
                "fields": "city, bdate",
                "lang": self.lang,
                "v": self.v,
            }
            async with session.get(url, params=params) as response:
                data = await response.json()
                return data["response"][0]


async def print_user_info(user_info: dict):
    print(
        f"Имя: {user_info["first_name"]}\n"
        f"Фамилия: {user_info["last_name"]}\n"
        f"Город: {user_info["city"]["title"]}\n"
        f"День Рождения: {user_info["bdate"]}\n"
    )


async def main():
    vk_client = VKClient(ACCESS_TOKEN)
    user_ids = [
        "vzlombn",
        "letxga",
        "aloxiy",
    ]

    tasks = [asyncio.create_task(vk_client.get_user_info(user_id)) for user_id in user_ids]
    users_info = await asyncio.gather(*tasks)

    tasks = [asyncio.create_task(print_user_info(users_info)) for users_info in users_info]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
