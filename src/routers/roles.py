from typing import Annotated, List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.models import Role
from src.schemas import Role as RoleSchema, RoleCreate
from src.session import create, read_all, read

router = APIRouter()


@router.post('/', response_model=RoleSchema, status_code=status.HTTP_201_CREATED)
async def create_role(db: Annotated[AsyncSession, Depends(get_db)], requested_data: RoleCreate):
    instance = await create(db, Role, requested_data)

    return instance


@router.get('/', response_model=List[RoleSchema], status_code=status.HTTP_200_OK)
async def get_roles(db: Annotated[AsyncSession, Depends(get_db)], skip: int = 0, limit: int = 10):
    instances = await read_all(db, Role, skip, limit)

    return instances


@router.get('/{instance_id}', response_model=RoleSchema, status_code=status.HTTP_200_OK)
async def get_role(db: Annotated[AsyncSession, Depends(get_db)], instance_id: int):
    instance = await read(db, Role, instance_id)

    if not instance:
        raise HTTPException(detail='такой роли не существует', status_code=status.HTTP_404_NOT_FOUND)

    return instance
