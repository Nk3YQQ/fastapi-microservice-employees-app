import enum
from datetime import date
from typing import Annotated, List

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

int_pk = Annotated[int, mapped_column(primary_key=True)]
str_150 = Annotated[str, mapped_column(String(150), nullable=False)]
str_100_unique = Annotated[str, mapped_column(String(100), unique=True, nullable=False)]
role_id = Annotated[int, mapped_column(ForeignKey('roles.id'))]


class Base(DeclarativeBase):
    """ Базовая модель """

    pass


class Gender(enum.Enum):
    male = 'male'
    female = 'female'


class Role(Base):
    """ Модель роли """

    __tablename__ = 'roles'

    id: Mapped[int_pk]
    title: Mapped[str_100_unique]

    employees: Mapped[List['Employee']] = relationship(back_populates='role')


class Employee(Base):
    """ Модель сотрудника """

    __tablename__ = 'employees'

    id: Mapped[int_pk]
    first_name: Mapped[str_150]
    last_name: Mapped[str_150]
    birth_date: Mapped[date]
    gender: Mapped[Gender]
    email: Mapped[str_100_unique]
    role_id: Mapped[role_id]

    role: Mapped['Role'] = relationship(back_populates='employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'<Employee(id={self.id}, email={self.email}, role={self.role.title})>'
