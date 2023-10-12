from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.settings import POSTGRES_URI


async_engine = create_async_engine(
    POSTGRES_URI,
    future=True,
)


async_session = async_sessionmaker(async_engine, expire_on_commit=False)


# Dependency
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session