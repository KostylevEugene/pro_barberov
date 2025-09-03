from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.connection import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, comment="ID пользователя"
    )
    name: Mapped[str] = mapped_column(
        nullable=False, unique=True, comment="Название роли"
    )

    users: Mapped[list["User"]] = relationship(back_populates="role")


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, comment="ID пользователя"
    )
    name: Mapped[str] = mapped_column(comment="Имя")
    second_name: Mapped[str] = mapped_column(comment="Отчество")
    surname: Mapped[str] = mapped_column(comment="Фамилия")
    login: Mapped[str] = mapped_column(comment="Логин")
    password: Mapped[str] = mapped_column(comment="Пароль")
    phone: Mapped[str] = mapped_column(comment="Телефон")
    email: Mapped[str] = mapped_column(comment="Электронная почта")
    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"), comment="Роль пользователя"
    )
    active: Mapped[bool] = mapped_column(
        server_default="true", comment="Активен ли пользователь"
    )

    role: Mapped["Role"] = relationship(back_populates="users")
    company: Mapped["Company"] = relationship(back_populates="user")
    master: Mapped["Master"] = relationship(back_populates="user")


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, comment="ID компании"
    )
    name: Mapped[str] = mapped_column(comment="Название")
    address: Mapped[str] = mapped_column(comment="Адрес")
    description: Mapped[str] = mapped_column(comment="Описание")
    main_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), comment="ID главного пользователя"
    )

    user: Mapped["User"] = relationship(back_populates="company")
    departments: Mapped[list["Department"]] = relationship(
        back_populates="company"
    )
    masters: Mapped[list["Master"]] = relationship(back_populates="company")


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, comment="ID компании"
    )
    name: Mapped[str] = mapped_column(comment="Название")
    address: Mapped[str] = mapped_column(comment="Адрес")
    description: Mapped[str] = mapped_column(comment="Описание")
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"), comment="ID компании"
    )

    company: Mapped["Company"] = relationship(back_populates="departments")
    masters: Mapped[list["Master"]] = relationship(
        back_populates="departments"
    )


class Master(Base):
    __tablename__ = "masters"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, comment="ID мастера"
    )
    name: Mapped[str] = mapped_column(comment="Имя или псевдоним мастера")
    description: Mapped[str] = mapped_column(comment="Описание")
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), comment="ID пользователя"
    )
    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"), comment="ID компании"
    )
    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"), comment="ID подразделения"
    )

    user: Mapped["User"] = relationship(back_populates="master")
    company: Mapped["Company"] = relationship(back_populates="masters")
    departments: Mapped["Department"] = relationship(back_populates="masters")
