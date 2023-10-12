from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if isinstance(value, str) and member.value == value.upper():
                return member

    @classmethod
    def keys(cls):
        return cls._member_names_

    @classmethod
    def values(cls):
        return list(cls._value2member_map_.keys())
