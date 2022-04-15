import asyncio
from pyppeteer import launch


async def request_prices(context, user_agent, iata_starting_airport, iata_finishing_airport, departure_data) -> dict:
    price = {}
    url = f'https://www.ua.kayak.com/flights/{iata_starting_airport}-{iata_finishing_airport}/{departure_data}?sort=bestflight_a'
    page = await context.newPage()
    await page.setUserAgent(user_agent)
    await page.goto(url)
    print(url)
    await page.waitForSelector('span[class=price-text]', timeout = 60000)
    price = await page.querySelector('span[class=price-text]').jsonValue()
    await page.close()
    print(price)
    #return price
