import aiohttp
import asyncio

urls = [
    'https://api.open-meteo.com/v1/forecast?latitude=50.00&longitude=36.10&daily&current_weather=true',
    '//api.opensensemap.org',
    'https://www.metaweather.com/api/location/search/?lattlong=50.00,36.10'
]


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, urls[0])
        print(html)

        html = await fetch(session, urls[1])
        print(html)

        html = await fetch(session, urls[2])
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
