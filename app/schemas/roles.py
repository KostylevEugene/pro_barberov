from pydantic import BaseModel, Field, field_validator


class CreateUserRole(BaseModel):
    name: str = Field(description="Название роли пользователя")

    @field_validator("name", mode="after")
    @classmethod
    def is_not_empty(cls, value: str) -> str:
        if not value:
            raise ValueError("Поле 'name' не должно быть пустым")

        return value


class UserRole(CreateUserRole):
    id: int


class EditUserRole(CreateUserRole):
    pass
