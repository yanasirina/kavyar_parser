from dataclasses import dataclass


@dataclass
class User:
    slug: str
    email: str
    instagram: str
