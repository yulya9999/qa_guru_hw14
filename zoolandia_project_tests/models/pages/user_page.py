from dataclasses import dataclass


@dataclass
class User:
    login: str
    password: str
    name: str
