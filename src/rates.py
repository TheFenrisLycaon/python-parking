from enum import Enum

from vehicle import type


class Rate(Enum):
    COMPACT: int = 25
    REGULAR: int = 50
    LARGE: int = 75
