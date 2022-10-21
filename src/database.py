from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

db_server = os.getenv('DB_URL')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://"+db_user+":"+db_password+"@"+db_server+"?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()