import pytest
from app.repositories.exceptions import EntityAlreadyExistError


@pytest.mark.asyncio
async def test_add_role(role):
    assert role.id is not None
    assert role.name == "test_role"


@pytest.mark.asyncio
async def test_add_existed_role(role_repo, role):
    with pytest.raises(EntityAlreadyExistError):
        await role_repo.add(name="test_role")


@pytest.mark.asyncio
async def test_get_role_by_id(role_repo, role):
    receive_role = await role_repo.get_by_id(role.id)

    assert receive_role.name is not None
    assert role.name == receive_role.name


@pytest.mark.asyncio
async def test_get_not_existed_role_by_id(role_repo):
    receive_role = await role_repo.get_by_id(0)
    assert receive_role is None


@pytest.mark.asyncio
async def test_edit_role(role_repo, role):
    updated_role = await role_repo.update_by_id(
        model_id=role.id, name="new_test_role"
    )
    assert updated_role.id == role.id
    assert updated_role.name == role.name


@pytest.mark.asyncio
async def test_delete_role(role_repo, role):
    await role_repo.delete(role.id)
    assert await role_repo.get_by_id(role.id) is None
