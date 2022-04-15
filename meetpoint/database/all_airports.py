from sqlalchemy import Column, String, Float, Integer, Table
from sqlalchemy import insert
import requests
import csv

from .base import metadata, Base


'''Create table with dataset of all airports'''
class Airport(Base):
    __tablename__ = 'airports'
    
    airport_id = Column(Integer, primary_key = True)
    name = Column(String)
    latitude_deg = Column(Float)
    longitude_deg = Column(Float)
    elevation_ft = Column(String)
    continent = Column(String)
    iso_country = Column(String)
    municipality = Column(String)
    gps_code = Column(String)
    iata_code = Column(String)
    wiki_link = Column(String)
    
    def __init__(self, airport_id, name, latitude_deg, longitude_deg, elevation_ft, continent, iso_country, municipality, gps_code, iata_code, wiki_link):
        self.airport_id = airport_id
        self.name = name
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.elevation_ft = elevation_ft
        self.continent = continent
        self.iso_country = iso_country
        self.municipality = municipality
        self.gps_code = gps_code
        self.iata_code = iata_code
        self.wiki_link = wiki_link
        
    #def __repr__(self):
        #info: str = f'{name} ({iata_code}/n{gps_code} {continent} {municipality} {wiki_link})'
        #returt info
