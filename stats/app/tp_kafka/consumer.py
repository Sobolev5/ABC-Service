import orjson
from aiokafka import AIOKafkaConsumer
from functools import wraps
from pydantic import ValidationError

from app.db.session import async_session
from app.settings import KAFKA_URI
from app.settings import logger
from app.tp_kafka import handlers
from app.utils.base_schema import BaseSchema


consumer = AIOKafkaConsumer("user", bootstrap_servers=KAFKA_URI)


async def consume():
    await consumer.start()      
    try:
        async for msg in consumer:
            if msg.topic == "user":
                await handlers.upsert_user(msg.value)
    finally:
        logger.info("consumer stopped")
        await consumer.stop()


def topic_msg_decode(schema: BaseSchema):
    def wrap(func):
        @wraps(func)
        async def wrapped(msg_bytes: bytes, *args, **kwargs):
            try:
                msg_decoded = orjson.loads(msg_bytes.decode())
                msg = schema.validate(msg_decoded).dict()
                async with async_session() as get_db:
                    response = await func(msg, get_db, *args, **kwargs)
                return response                              
            except ValidationError as error_message:
                logger.error(error_message)
            except Exception as error_message:
                logger.error(error_message)           
        return wrapped
    return wrap