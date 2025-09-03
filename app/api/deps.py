from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.services.roles import RoleService
from app.repositories.roles import RoleRepository
from app.db.connection import AsyncSessionLocal


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db


def role_service(session: async_sessionmaker = Depends(get_db)):
    role_repo = RoleRepository(session)
    return RoleService(role_repo)
