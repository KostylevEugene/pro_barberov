import pytest_asyncio

from app.repositories.roles import RoleRepository


@pytest_asyncio.fixture()
async def role_repo(db_session):
    return RoleRepository(db_session)


@pytest_asyncio.fixture()
async def role(role_repo):
    role_name = "test_role"
    return await role_repo.add(name=role_name)
