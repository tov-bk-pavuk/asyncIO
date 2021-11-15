import aiohttp
import asyncio

url = [
    'http://httpbin.org/get',
    'http://httpbin.org/get',
    'http://httpbin.org/get',
]


def weather_one(session):
    async with session.get(url[0]) as resp:  # менеджер контекста, который создаёт асинхронную сессию coroutine
        text = await resp.json()
        print(text)


def weather_two(session):
    pass


def weather_three(session):
    pass


async def main():
    async with aiohttp.ClientSession() as session:  # менеджер контекста, который создаёт асинхронную сессию coroutine
        weather_one(session)
        weather_two(session)
        weather_three(session)


asyncio.run(main)
