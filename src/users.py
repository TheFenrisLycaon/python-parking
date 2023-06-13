from dataclasses import dataclass, field
from itertools import count


@dataclass
class User:
    id: int = field(default_factory=count().__next__, init=False)
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
