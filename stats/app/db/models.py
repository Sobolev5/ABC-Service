import typing as t
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.asyncio  import AsyncSession


class BaseModel(AsyncAttrs, DeclarativeBase):
    pass


class UserModel(BaseModel):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    actions: Mapped[t.List["ActionModel"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User ID={self.id!r}, name={self.name!r}"

    @staticmethod
    async def create_user(item: dict, db: AsyncSession) -> \
        t.Tuple[t.Optional[BaseModel], t.Optional[Exception]]:        
        user, error = None, None # TODO convert to schema
        try:
            user = UserModel(**item)
            async with db.begin():
                db.add(user)
                await db.flush()
        except Exception as e:
            error = e
        return user, error
    
    
class ActionModel(BaseModel):
    __tablename__ = "action"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    report: Mapped[str] 

    user_id = mapped_column(ForeignKey("user.id"))
    user: Mapped[UserModel] = relationship(back_populates="actions")

    def __repr__(self) -> str: 
        return f"Action ID={self.id!r}"

