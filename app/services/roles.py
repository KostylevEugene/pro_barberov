from app.repositories.general import AbstractRepository


class RoleService:
    def __init__(self, role_repo: AbstractRepository):
        self.repo = role_repo

    async def add_role(self, name):
        return await self.repo.add(name=name)
    
    async def get_role(self, id):
        return await self.repo.get_by_id(id=id)
