import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession

from src.engine import EngineHandler

load_dotenv()

DATABASE_PARAMS = {
    'database': 'postgresql.asyncpg',
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT', '5432'),
    'db_name': os.getenv('DB_NAME')
}

engine_handler = EngineHandler(DATABASE_PARAMS)

database_url = engine_handler.get_url()

engine = engine_handler.get_url()

async_session = engine_handler.get_session()


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
