from dataclasses import dataclass
from math import gcd
from typing import List


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
    frets_movable: bool = False
    strings_movable: bool = False


@dataclass()
class Beat:
    duration: int
    division: int = 4
    rest: bool = False

    def __add__(self, other):
        if self.duration == 0 and self.division == 0:
            return other

        total_duration = (self.duration * other.division) + (other.duration * self.division)
        total_division = self.division * other.division

        common_divisible = gcd(total_duration, total_division)
        duration = int(total_duration / common_divisible)
        division = int(total_division / common_divisible)

        return Beat(duration=duration, division=division)

    def __eq__(self, other):
        if self.division == other.division and self.duration == other.duration:
            return True

        return self.duration * other.division == other.duration * self.division



    @property
    def whole_beats(self):
        return self.duration // self.division

    @property
    def sub_beats(self):
        return Beat(self.duration % self.division, self.division)


@dataclass()
class Note:
    position: FretPosition
    duration: Beat
    elapsed_beats: Beat
    order: int


@dataclass()
class Annotation:
    category: str
    order: int
    duration: Beat


@dataclass()
class Sequence:
    notes: List[Note]
    shapes: List[GuitarShape]
    annotations: List[Annotation] = None
