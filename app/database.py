from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionaLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db():
    db = SessionaLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         # pass in the host, database name, user, password, cursor_factory

#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Mocalate2006', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successfull!")
#         print("------------------------")
#         break
#     except Exception as error:
#         print("Connection to Database failed")
#         print("Error: ", error)
#         time.sleep(3)
