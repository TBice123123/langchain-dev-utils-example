from dataclasses import dataclass
from typing import Optional


@dataclass
class UserInput:
    image_url: Optional[str] = None
