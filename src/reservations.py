from datetime import datetime
from dataclasses import dataclass, field
from itertools import count


@dataclass
class Reservation:
    garage_id: int
    spot_id: int
    id: int = field(default_factory=count().__next__, init=False)
    amount: float
    paid: bool
    start_time: datetime
    end_time: datetime

    def __repr__(self) -> str:
        return f"Reservation booked at Garage/Spot :: {self.garage_id}/{self.spot_id} from {self.start_time} till {self.end_time}."
