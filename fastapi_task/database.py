from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import asyncio

SQLALCHEMY_URL = 'sqlite+aiosqlite:///./sql_app.db'

# Создаем асинхронный движок
async_engine = create_async_engine(SQLALCHEMY_URL, echo=True, future=True)
async_session = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

# Создаем базу данных
Base = declarative_base()


async def create_async_db():
    async with async_engine.begin() as conn:
        await asyncio.run(conn.run_sync(Base.metadata.create_all))


async def get_async_db():
    async with async_session() as session:
        yield session
