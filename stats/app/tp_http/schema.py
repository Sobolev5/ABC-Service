import typing as t
from pydantic import Field, StrictStr
from app.utils.base_schema import BaseSchema


class HealthRQ(BaseSchema):
    ping: StrictStr


class UserRQ(BaseSchema):
    id: int = Field(ge=0) 
    name: str = Field(max_length=50) 


class DefaultRS(BaseSchema):
    message: t.Optional[str]




