from dataclasses import dataclass, field
from itertools import count

from src.spot import Spot


@dataclass
class Garage:
    id: int = field(default_factory=count().__next__, init=False)
    name: str
    spots: list[Spot]
    zipcode: str
