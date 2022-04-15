from pyppeteer import launch
from core.engine.parsing.parse_aggregator import request_prices
import asyncio

async def get_prices(iata_starting_airports, iata_finishing_airports, departure_date):
    tasks = []
    browser = await launch()
    context = await browser.createIncognitoBrowserContext()
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    
    for iata_finishing_airport in iata_finishing_airports:
        for iata_starting_airport in iata_starting_airports:
            url = f'https://www.momondo.co.uk/flight-search/{iata_starting_airport}-{iata_finishing_airport}/2022-02-20?sort=bestflight_a'
            task = asyncio.create_task(request_prices(context, user_agent, iata_starting_airport, iata_finishing_airport, departure_date))
            tasks.append(task)
    
    await asyncio.gather(*tasks)
    await browser.close()
