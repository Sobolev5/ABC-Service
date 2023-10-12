from ninja import Schema


class Ping_POST_IN(Schema):
    ping: str


class Topic_GET_OUT(Schema):
    id: int
    name: str

