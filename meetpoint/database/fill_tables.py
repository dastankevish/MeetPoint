import requests
import csv

from .base import session
from .all_airports import Airport, InternationalAirport
from .get_international_airports_rowids import get_international_airports_rowids

def fill_airports_table(session):
    response = requests.get('https://davidmegginson.github.io/ourairports-data/airports.csv').text.split('\n')

    reader = list(csv.reader(response, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL))[:-1]
    
    for row in reader:
        if row[2] == 'small_airport' or row[2] == 'medium_airport' or row[2] == 'large_airport':
            #if row[11] != 'no':
            row = row[0:1] + row[3:9] + row[10:11] + row[12:14] + row[-2:-1]
            airport = Airport(*row)
            session.add(airport)
            
    session.commit()


def fill_international_airports_table():
    rowids = asyncio.run(get_international_airports_rowids())

    for rowid in rowids:
        row = session.query(Airport).filter(Airport.rowid(rowid))
        print(row)
        airport = InternationalAirport(row)
        session.add(airport)

    session.commit()
