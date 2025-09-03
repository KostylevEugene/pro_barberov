from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.api.deps import role_service
from app.services.exceptions import RoleAlreadyExists
from services.roles import RoleService
from schemas.roles import CreateUserRole, UserRole

router = APIRouter(prefix="/roles", tags=["roles"])


@router.post("/", response_model=UserRole)
async def create_roles(
    role_data: CreateUserRole,
    role_service: Annotated[RoleService, Depends(role_service)],
):
    try:
        return await role_service.add_role(role_data.name)
    except RoleAlreadyExists as e:
        raise HTTPException(status_code=409, detail=e.msg)


@router.get("/{role_id}", response_model=UserRole)
async def get_role(
    role_id: int, role_service: Annotated[RoleService, Depends(role_service)]
):
    return await role_service.get_role(role_id=role_id)


@router.put("/{role_id}")
async def update_role():
    pass


@router.delete("/{role_id}")
async def delete_role(
    role_id: int, role_service: Annotated[RoleService, Depends(role_service)]
):
    return await role_service.delete_role(role_id=role_id)


@router.get("/all")
async def get_all_roles():
    pass
