from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    slug: str
    email: Optional[str]
    instagram: Optional[str]
