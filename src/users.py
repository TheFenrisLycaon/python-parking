from dataclasses import dataclass, field
from itertools import count
from .vehicle import type
from datetime import datetime
from .reservations import Reservation


@dataclass
class User:
    id: int = field(default_factory=count().__next__, init=False)
    first_name: str
    last_name: str
    email: str
    username: str
    password: str

    def book_ticket(
        vehicle_type: type, start_time: datetime, end_time: datetime, garage_id: int
    ):
        new = Reservation()

    def pay():
        pass

    def cancel():
        pass

    def show_ticket():
        pass
