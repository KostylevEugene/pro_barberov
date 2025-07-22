from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.db.models import Role
from .general import GeneralRepository


class RoleRepository(GeneralRepository):
    model = Role
