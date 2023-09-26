"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "http://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "http://jsonplaceholder.typicode.com/posts/"


async def fetch_json(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def fetch_users():
    users = await fetch_json(USERS_DATA_URL)
    return users


async def fetch_posts():
    posts = await fetch_json(POSTS_DATA_URL)
    return posts
