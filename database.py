from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:' \
                          f'{settings.database_password}@{settings.database_hostname}:' \
                          f'{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# try:
#     conn =psycopg2.connect(host='localhost', database="fastAPI", user='postgres',
#                            password="tarzanid123", cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database connection was SUCCESSFUL!")
# except Exception as err:
#     print('Database connection was FAILED')
#     print(f"Error: {err}")
