from datetime import date
from enum import Enum
from typing import Optional, Annotated

from pydantic import BaseModel, Field, ConfigDict

str_100 = Annotated[str, Field(max_length=100)]
str_150 = Annotated[str, Field(max_length=150)]


class RoleCreate(BaseModel):
    """ Модель создания роли """

    title: str


class Role(BaseModel):
    """ Модель роли """

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str_100


class RoleUpdate(BaseModel):
    """ Модель обновления роли """

    title: Optional[str] = None


class Gender(str, Enum):
    """ Енум пола """

    male = 'male'
    female = 'female'


class EmployeeCreate(BaseModel):
    """ Модель создания сотрудника """

    first_name: str_150
    last_name: str_150
    birth_date: date
    gender: Gender
    email: str_100
    role_id: int


class Employee(BaseModel):
    """ Модель сотрудника """

    id: int
    first_name: str_150
    last_name: str_150
    birth_date: date
    gender: Gender
    email: str_100
    role: str


class EmployeeUpdate(BaseModel):
    """ Модель обновления сотрудника """

    first_name: Optional[str_150] = None
    last_name: Optional[str_150] = None
    birth_date: Optional[date] = None
    gender: Optional[Gender] = None
    email: Optional[str_100] = None
    role_id: Optional[int] = None
