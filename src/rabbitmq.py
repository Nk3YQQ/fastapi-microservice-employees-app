import os
from typing import AsyncGenerator

import aio_pika
from dotenv import load_dotenv

from src.services import make_pika_url

load_dotenv()

PIKA_PARAMS = {
    'protocol': 'amqp',
    'user': os.getenv('PIKA_USER'),
    'password': os.getenv('PIKA_PASSWORD'),
    'host': os.getenv('PIKA_HOST'),
    'port': os.getenv('PIKA_PORT')
}

url = make_pika_url(PIKA_PARAMS)


async def get_rabbitmq_connector() -> AsyncGenerator[aio_pika.Connection, None]:
    connection = await aio_pika.connect_robust(url)
    try:
        yield connection

    finally:
        await connection.close()


async def get_rabbitmq_channel(connection: aio_pika.Connection):
    return await connection.channel()
