from app.db.models import Role
from .general import GeneralRepository


class RoleRepository(GeneralRepository):
    model = Role
