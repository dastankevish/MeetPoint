from bs4 import BeautifulSoup
import lxml
import aiohttp
import asyncio


async def get_all_routes(origin_iatas, date) -> dict:
    async with aiohttp.ClientSession() as session:
        
        tasks = []
        for origin_iata in origin_iatas:
            task = asyncio.create_task(request_routes(session, origin_iata, date))
            tasks.append(task)
        
        routes = await asyncio.gather(*tasks)
    
    routes = {}
    for _ in range(len(routes)):
        routes[list(routes[_].keys())[0]] = list(routes[_].values())[0]
            
    return routes


async def request_routes(session, origin_iata, date) -> dict:
    url = f'https://www.flightsfrom.com/{origin_iata}/destinations?dateMethod=day&dateFrom={date}&dateTo={date}'
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191'}
    async with session.get(url=url, headers=headers) as response:
        response = await response.text()
        
        soup = BeautifulSoup(response, 'lxml')
        response = soup.find_all('span', class_ = 'airport-font-midheader')
        
        for _ in range(len(response)):
            response[_] = response[_].text.split()
            response[_] = {'city': response[_][0], 'destination_iata': response[_][1]}
        
        routes = {}
        routes[origin_iata] = response
        
    return routes


def get_joint_destination_iatas(routes):
    origin_iatas = list(routes.keys())
    destination_iatas = [i['destination_iata'] for i in routes[origin_iatas[0]]]
    joint_destination_iatas = [None for elem in range(len(destination_iatas))]

    for origin_iata in origin_iatas:
        for destination_iata in range(len(destination_iatas)):
            if str(routes[origin_iata]).find(destination_iatas[destination_iata]) != -1 and joint_destination_iatas[destination_iata] != '':
                joint_destination_iatas[destination_iata] = destination_iatas[destination_iata]
            else:
                joint_destination_iatas[destination_iata] = ''
            
    joint_destination_iatas = [elem for elem in joint_destination_iatas if elem != '']
    
    print(origin_iatas)
    print(destination_iatas)
    print(joint_destination_iatas)
    
    return joint_destination_iatas
