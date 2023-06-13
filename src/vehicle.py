from enum import Enum
from dataclasses import dataclass
from src.users import User


class type(Enum):
    COMPACT = -1
    REGULAR = 0
    LARGE = 1


class Vehicle:
    user_id: User.id
    license_num: str
    type: type
