from pydantic import BaseModel, Field


class CreateUserRole(BaseModel):
    name: str = Field(description="Название роли пользователя")


class UserRole(CreateUserRole):
    id: int
