from settings import POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER, DB_PORT, DB_HOST
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Integer, Date, String, Column, select, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager


DB_URL = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}'
# engine = create_engine(DB_URL)
engine = create_async_engine(DB_URL, echo=True)
Base = declarative_base()
# async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Генератор сессии
def async_session_generator():
    return sessionmaker(engine, class_=AsyncSession)


#Асинхронный контекстный менеджер
@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()

        async with async_session() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.commit()
        await session.close()


# Модель БД
class Users(Base):
    __tablename__ = 'Users'
    ID = Column(Integer(), primary_key=True, autoincrement=True)
    UUID = Column(Integer(), unique=True, nullable=False)
    UserName = Column(String(length=100), nullable=False)
    RegisterDate = Column(Date())


users_table = Users.__table__
