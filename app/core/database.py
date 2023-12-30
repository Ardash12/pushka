import mysql.connector
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session


# DATABASE_URL = mysql.connector.connect(
#     host="127.0.0.1",
#     port=3306,
#     user="rms2022",
#     password="kjghaHH8HYds56jH9",
#     database="fastapi_db"
# )
DATABASE_URL = "sqlite:///./test.db"

# async_engine = create_async_engine(
#     DATABASE_URL, 
#     echo=False,
# )

sync_engine = create_engine(
    DATABASE_URL, 
    echo=False,
)

# async_session = sessionmaker(async_engine)

sync_session = sessionmaker(sync_engine)

# async def get_session() -> AsyncSession:
#     async with async_session() as session:
#         yield session

def get_session() -> Session:
    with sync_session() as session:
        return session
