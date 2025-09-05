from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.deps import role_service
from app.services.exceptions import RoleAlreadyExists
from services.roles import RoleService
from schemas.roles import CreateUserRole, EditUserRole, UserRole

router = APIRouter(prefix="/roles", tags=["roles"])


@router.post("/", response_model=UserRole, status_code=status.HTTP_201_CREATED)
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
    if result := await role_service.get_role(role_id=role_id):
        return result
    else:
        raise HTTPException(
            status_code=404, detail=f"Роли с id = {role_id} не существует"
        )


@router.put("/{role_id}", response_model=UserRole)
async def edit_role(
    role_id: int,
    role_data: EditUserRole,
    role_service: Annotated[RoleService, Depends(role_service)],
):
    if result := await role_service.edit_role(
        role_id=role_id, name=role_data.name
    ):
        return result
    else:
        raise HTTPException(
            status_code=404, detail=f"Роли с id = {role_id} не существует"
        )


@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_role(
    role_id: int, role_service: Annotated[RoleService, Depends(role_service)]
):
    return await role_service.delete_role(role_id=role_id)


@router.get("/all")
async def get_all_roles():
    pass
