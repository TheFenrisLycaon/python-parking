from dataclasses import dataclass
import datetime


@dataclass
class Reservation:
    garage_id: str
    spot_id: str
    amount: float
    paid: bool
    start_time: datetime.datetime
    end_time: datetime.datetime

    def __repr__(self) -> str:
        return f"Reservation booked at Garage/Spot :: {self.garage_id}/{self.spot_id} from {self.start_time} till {self.end_time}."
