from simple_print import sprint
from app.src import views
from app.db.session import async_session


async def upsert_user():
    # python run.py app.src.cli "upsert_user()"

    item = {
        "name": "test"
    }

    async with async_session() as get_db:
        user, error = await views.upsert_user(item, get_db)

    sprint(user, error)

