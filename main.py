import asyncio

import aiohttp

urls = [
    'https://api.monobank.ua/bank/currency?currencyCodeA=840',
    'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json',
    'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
]


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, urls[0])
        avg_mono = (html[0]['rateBuy'] + html[0]['rateSell']) / 2

        html = await fetch(session, urls[1])
        nac_bank = html[26]['rate']

        html = await fetch(session, urls[2])
        privat_bank = (float(html[0]['buy']) + float(html[0]['sale']))/2

        print(f' средний курс USD/ГРН за 1 USD = {round((avg_mono + nac_bank + privat_bank)/3, 2)} грн')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
