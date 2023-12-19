from dataclasses import dataclass


@dataclass
class Person:
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
