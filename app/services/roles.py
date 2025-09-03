from app.repositories.exceptions import EntityAlreadyExistError
from app.repositories.general import AbstractRepository
from app.services.exceptions import RoleAlreadyExists


class RoleService:
    def __init__(self, role_repo: AbstractRepository):
        self.repo = role_repo

    async def add_role(self, name):
        try:
            return await self.repo.add(name=name)
        except EntityAlreadyExistError:
            raise RoleAlreadyExists(f"Данная роль уже существует - {name}")

    async def get_role(self, role_id):
        return await self.repo.get_by_id(model_id=role_id)

    async def delete_role(self, role_id):
        return await self.repo.delete(model_id=role_id)
