from dataclasses import dataclass
from src.vehicle import type


@dataclass
class Spot:
    id: str
    type: type
    booking_status: bool = False
