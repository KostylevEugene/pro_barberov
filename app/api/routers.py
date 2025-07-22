from fastapi import APIRouter

from .endpoints import roles, users


router = APIRouter()

router.include_router(roles.router)
router.include_router(users.router)
