import os

from utils.configs import DATABASE_NAME
from .base import metadata, Base, engine, session

import database.all_airports
import database.all_international_airports

from database.fill_tables import fill_airports_table
#from database.fill_tables import fill_international_airports_table


db_is_created = os.path.exists(DATABASE_NAME)
if not db_is_created:
    Base.metadata.create_all(bind=engine)
    fill_airports_table(session())
    #fill_international_airports_table(session())
    session.close()
else:
    os.remove(DATABASE_NAME)
    Base.metadata.create_all(bind=engine)
    fill_airports_table(session())
    #fill_international_airports_table(session())
    session.close()
