from dataclasses import dataclass

@dataclass
class OutDTO:
    has_data: str
    date: str
    flares_count_second: int
    flares_second: str
