import asyncio
from typing import AsyncGenerator

import pytest
from sqlalchemy import text
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.db.session import get_db
from app.settings import POSTGRES_USER, POSTGRES_PASSWORD
from app.settings import POSTGRES_URI_TEST_ASYNC, POSTGRES_URI_TEST_SYNC
from app.db.models import BaseModel
from app.main import app



@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    # python run.py tests.conftest "create_test_db()"

    engine = create_engine(POSTGRES_URI_TEST_SYNC.replace("test", "postgres"))
    
    conn = engine.connect()
    conn = conn.execution_options(isolation_level="AUTOCOMMIT")
    try:
        conn.execute(text("DROP DATABASE test WITH (FORCE);"))
    except:
        pass
    conn.execute(text(f"CREATE DATABASE test OWNER {POSTGRES_USER}"))
    conn.close()
    
    engine = create_engine(POSTGRES_URI_TEST_SYNC)
    BaseModel.metadata.create_all(engine)
    

@pytest.fixture(scope="session")
async def test_db() -> AsyncGenerator[AsyncSession, None]:
    async_engine = create_async_engine(
        POSTGRES_URI_TEST_ASYNC,
        echo=True,
        future=True,
    )
    async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)
    async with async_session_maker() as session:
        yield session


@pytest.fixture(scope="function")
async def test_client(test_db) -> AsyncGenerator[TestClient, None]:
    app.dependency_overrides[get_db] = test_db
    client = TestClient(app)
    with TestClient(app) as client:
        yield client
