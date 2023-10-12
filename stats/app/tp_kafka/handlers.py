from app.src import views
from app.tp_http import schema
from app.tp_kafka.consumer import topic_msg_decode


@topic_msg_decode(schema.RateCodeRQ)
async def upsert_user(item, db) -> None:
    await views.upsert_user(item, db)
