import asyncio
from fastapi import FastAPI

from app.tp_http import handlers as http_handlers
from app.tp_kafka.consumer import consume, consumer
from app.tp_kafka.producer import producer
from app.settings import DEBUG
from app.settings import logger


app = FastAPI(debug=DEBUG, title="stats")
app.include_router(http_handlers.router)


@app.on_event("startup")
async def startup():
    logger.info("Starting KAFKA")
    await producer.start()
    asyncio.create_task(consume())


@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutting down KAFKA")
    await producer.stop()
    await consumer.stop()
