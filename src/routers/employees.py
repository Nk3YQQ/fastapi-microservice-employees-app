from typing import Annotated, List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.models import Role, Employee
from src.schemas import Employee as EmployeeSchema, EmployeeCreate
from src.services import serialize_employee, serialize_employees
from src.session import read, create, read_all

router = APIRouter()


@router.post('/', response_model=EmployeeSchema, status_code=status.HTTP_201_CREATED)
async def create_employee(db: Annotated[AsyncSession, Depends(get_db)], requested_data: EmployeeCreate):
    role_id = requested_data.role_id
    role = await read(db, Role, role_id)

    if not role:
        raise HTTPException(detail='Роль не найдена', status_code=status.HTTP_404_NOT_FOUND)

    instance = await create(db, Employee, requested_data)
    instance.role = role

    return serialize_employee(instance)


@router.get('/', response_model=List[EmployeeSchema], status_code=status.HTTP_200_OK)
async def get_employees(db: Annotated[AsyncSession, Depends(get_db)], skip: int = 0, limit: int = 10):
    employees = await read_all(db, Employee, skip, limit, mode='users')

    return serialize_employees(employees)


@router.get('/{instance_id}', response_model=EmployeeSchema, status_code=status.HTTP_200_OK)
async def get_employee(db: Annotated[AsyncSession, Depends(get_db)], instance_id: int):
    employees = await read(db, Employee, instance_id, mode='users')

    return serialize_employee(employees)
