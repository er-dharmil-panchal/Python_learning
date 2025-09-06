"""
This is user.py for user data and user operation
"""
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json
from Util import load_users

user_schema = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
        "age": {"type": "number", "minimum": 0},
        "bio": {"type": "string"},
        "created_at": {"type": "string"}
    },
    "required": ["username","password","age","bio","created_at"]
}

class User:
    def __init__(self,username,password,age,bio,created_at):
        self.username = username
        self.password = password
        self.age = age
        self.bio = bio
        self.created_at = created_at
        self.valid = False

    @classmethod
    def from_dict(cls, data):
        return cls(
            username=data["username"],
            password=data.get("password", ""),  # empty for safety
            age=data.get("age", None),
            bio=data.get("bio", ""),
            created_at=data.get("created_at", "")
        )

    def login(self):
        self.is_logged_in = True
        print(f"Welcome, {self.username}!")

    # Registration
    def register(self):
        file_data = load_users()
        data = {
            "username": self.username,
            "password": self.password,
            "age": self.age,
            "bio": self.bio,
            "created_at": self.created_at
        }
        try:
            validate(instance=data, schema=user_schema)
            self.valid = True
        except ValidationError as e:
            print(f"❌ Invalid Format: {e.message}")

        if self.valid:
            file_data.append(data)
            with open("Data/users.json", "w") as file:
                json.dump(file_data, file, indent=4)
        else:
            print("There is some problem in formating, please try again.")
