import typing as t
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import UserModel


async def upsert_user(item: dict, db: AsyncSession) -> \
    t.Tuple[t.Optional[UserModel], t.Optional[Exception]]:
    user, error = await UserModel.create_user(item, db)
    return user, error


