from dataclasses import dataclass
from enum import Enum


class type(Enum):
    COMPACT = -1
    REGULAR = 0
    LARGE = 1


class Vehicle:
    user_id: int
    license_num: str
    type: type
