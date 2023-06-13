from dataclasses import dataclass, field
from itertools import count

from src.vehicle import type


@dataclass
class Spot:
    id: int = field(default_factory=count().__next__, init=False)
    type: type
    booking_status: bool = False
