from dataclasses import dataclass
from math import gcd
from typing import List, Optional


@dataclass()
class FretPosition:
    fret: int
    string: int
    finger: int = None

    def __gt__(self, other):
        if self.string == other.string:
            return self.fret > other.fret

        return self.string < other.string


@dataclass()
class GuitarShape:
    name: str
    category: str
    positions: List[FretPosition]
    movable: bool = False


@dataclass()
class Beat:
    duration: int
    division: int = 1
    rest: bool = False

    def __add__(self, other):
        total_duration = (self.duration * other.division) + (other.duration * self.division)
        total_division = self.division * other.division

        common_divisible = gcd(total_duration, total_division)
        duration = int(total_duration/common_divisible)
        division = int(total_division/common_divisible)

        return Beat(duration=duration, division=division)


@dataclass()
class Note:
    position: FretPosition
    duration: Beat
    start_beat: Beat


@dataclass()
class Annotation:
    category: str
    start_beat: float
    duration: float


@dataclass()
class Sequence:
    notes: List[Note]
    shapes: List[GuitarShape]
    annotations: List[Annotation] = None
