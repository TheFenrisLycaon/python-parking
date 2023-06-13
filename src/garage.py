from dataclasses import dataclass
from src.spot import Spot


@dataclass
class Garage:
    name: str
    id: str
    spots: list[Spot]
    zipcode: str
