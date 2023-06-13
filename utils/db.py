import json
from typing import Any
from src.users import User


class UserEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, User):
            return o.__dict__
        return json.JSONEncoder.default(self, o)


def add_user(data: User) -> int:
    try:
        with open(f"data/Users/{data.username}.json", "w") as f:
            f.write(json.dumps(data, cls=UserEncoder, indent=4))
        return 1
    except:
        print("Writing failed.")
        return 0


def read_from_db():
    pass


def sync_db():
    pass
