from dataclasses import dataclass
from typing import List, Any

@dataclass
class OutDTO:
    has_data: str
    date: str
    flares_count_second: int
    flares_second: List[Any]
    status: str
