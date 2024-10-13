from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


async def create(db: AsyncSession, model, requested_data: BaseModel):
    try:
        instance = model(**requested_data.dict())
        db.add(instance)

        return instance

    except Exception as e:
        await db.rollback()
        raise ValueError(f'Ошибка в добавлении сущности: {e}')

    finally:
        await db.commit()


async def read_all(db: AsyncSession, model, skip: int = 0, limit: int = 10, mode: str = 'roles'):
    try:
        if mode == 'users':
            stmt = select(model).options(joinedload(model.role)).offset(skip).limit(limit)
        else:
            stmt = select(model).offset(skip).limit(limit)
        result = await db.execute(stmt)

        return result.scalars().all()

    except Exception as e:
        await db.rollback()
        raise ValueError(f'Ошибка в чтении сущностей: {e}')


async def read(db: AsyncSession, model, instance_id: int, mode: str = 'roles'):
    try:
        if mode == 'users':
            stmt = select(model).options(joinedload(model.role)).where(model.id == instance_id)
        else:
            stmt = select(model).where(model.id == instance_id)
        result = await db.execute(stmt)

        return result.scalars().first()

    except Exception as e:
        await db.rollback()
        raise ValueError(f'Ошибка в добавлении сущности: {e}')


async def update(db: AsyncSession, instance, requested_data: BaseModel):
    try:
        for key, value in requested_data.dict():
            if hasattr(instance, key) and value:
                setattr(instance, key, value)

        db.add(instance)

        return instance

    except Exception as e:
        await db.rollback()
        raise ValueError(f'Ошибка в обновлении сущности: {e}')

    finally:
        await db.commit()


async def delete(db: AsyncSession, instance):
    try:
        await db.delete(instance)

    except Exception as e:
        await db.rollback()
        raise ValueError(f'Ошибка в удалении сущности: {e}')
