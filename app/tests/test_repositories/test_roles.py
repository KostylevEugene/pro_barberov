import pytest
from app.repositories.exceptions import EntityAlreadyExistError

from app.repositories.roles import RoleRepository


@pytest.mark.asyncio
async def test_add_role(db_session):
    role_name = "test"
    role_repo = RoleRepository(db_session)
    test_role = await role_repo.add(name=role_name)

    assert test_role.id is not None
    assert test_role.name == role_name


@pytest.mark.asyncio
async def test_add_existed_role(db_session):
    role_name = "test"
    role_repo = RoleRepository(db_session)
    await role_repo.add(name=role_name)

    with pytest.raises(EntityAlreadyExistError):
        await role_repo.add(name=role_name)


@pytest.mark.asyncio
async def test_get_by_id(db_session):
    role_ame = "test"
    role_repo = RoleRepository(db_session)
    test_role = await role_repo.add(name=role_ame)
    role = await role_repo.get_by_id(test_role.id)

    assert test_role.name == role.name


@pytest.mark.asyncio
async def test_delete_role(db_session):
    role_ame = "test"
    role_repo = RoleRepository(db_session)
    test_role = await role_repo.add(name=role_ame)
    await role_repo.delete(test_role.id)

    assert await role_repo.get_by_id(test_role.id) is None
