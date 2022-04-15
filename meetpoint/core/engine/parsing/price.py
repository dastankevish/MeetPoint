import asyncio
import aiohttp
from fake_useragent import UserAgent


async def get_prices(iata_departure_airports, iata_arrival_airports, departure_date):
    month = departure_date[:-3]
    print(month)
    tasks = []
    useragent = UserAgent()
    
    iata_departure_airports = [iata_departure_airports]
    iata_arrival_airports = [iata_arrival_airports]
    
    async with aiohttp.ClientSession() as session:
        for iata_arrival_airport in iata_arrival_airports:
            for iata_departure_airport in iata_departure_airports:
                url = f'https://suggest.travelpayouts.com/uaca/v1/get_data_forward?service=calendar_aviasales_month&origin_iata={iata_departure_airport}&currency=usd&destination_iata={iata_arrival_airport}&one_way=true&min_trip_duration=7&max_trip_duration=14&only_direct=false&month={month}-01&host=bilet.airlines-inform.ru/flights'
              
                headers = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive', 'Host': 'suggest.travelpayouts.com', 'Origin': 'https://www.airlines-inform.ru', 'Referer': 'https://www.airlines-inform.ru/', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'cross-site', 'TE': 'trailers', 'User-Agent': useragent.random}
                
                print(url)
                
                for i in range(200):
                    task = asyncio.create_task(request_price(session, headers, url, departure_date, i))
                    tasks.append(task)
        
        await asyncio.gather(*tasks)


async def request_price(session, headers, url, departure_date, i):
    async with session.get(url=url, headers=headers) as response:
        response = await response.json()
        print(response)
        print(type(response))
        print(i)
        print('_________________________________________')
        print()
