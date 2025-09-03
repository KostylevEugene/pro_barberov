import pytest_asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.db.connection import Base
from app.settings.settings import postgres_db_settings as db_set


async def create_test_db():
    SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_set.user}:{db_set.password}@{db_set.host}:{db_set.port}/{db_set.db_name}"
    engine = create_async_engine(
        SQLALCHEMY_DATABASE_URL, isolation_level="AUTOCOMMIT"
    )

    async with engine.connect() as conn:
        await conn.execute(
            text(f"DROP DATABASE IF EXISTS {db_set.db_name}_test")
        )
        await conn.execute(text(f"CREATE DATABASE {db_set.db_name}_test"))

    await engine.dispose()


@pytest_asyncio.fixture()
async def setup_engine():
    await create_test_db()

    SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_set.user}:{db_set.password}@{db_set.host}:{db_set.port}/{db_set.db_name}_test"
    engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()


@pytest_asyncio.fixture
async def db_session(setup_engine):
    async_session = async_sessionmaker(
        setup_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
