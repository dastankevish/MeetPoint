from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.configs import DATABASE_URL

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL, echo=True)
session = sessionmaker(bind=engine)
Base = declarative_base()
