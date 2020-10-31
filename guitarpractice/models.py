from dataclasses import dataclass
from fractions import Fraction
from math import ceil
from typing import List, Union


@dataclass()
class FretPosition:
    fret: int
    string: int
    finger: int = None
    highlighted: bool = False

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

    @classmethod
    def from_fraction(cls, fraction):
        return Beat(duration=fraction.numerator, division=fraction.denominator)

    def to_fraction(self) -> Fraction:
        return Fraction(self.duration, self.division)

    def __add__(self, other):
        if self.duration == 0 and self.division == 0:
            return other

        result = self.to_fraction() + other.to_fraction()

        return Beat.from_fraction(result)

    def __sub__(self, other):
        as_fraction = self.to_fraction() - other.to_fraction()

        result = Beat.from_fraction(as_fraction)

        if result.duration < 0:
            raise ValueError('Beat duration cannot be negative')

        return result

    def __eq__(self, other):
        if self.division == other.division and self.duration == other.duration:
            return True

        return self.duration * other.division == other.duration * self.division

    def __gt__(self, other):
        return self.to_fraction() > other.to_fraction()

    def __lt__(self, other):
        return self.to_fraction() < other.to_fraction()

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return self < other or self == other

    def tie_split(self) -> List:
        splits = []

        remainder = self
        even_beats = [
            Beat(1, 1),
            Beat(1, 2),
            Beat(1, 4),
            Beat(1, 8),
            Beat(1, 16),
            Beat(1, 32),
        ]

        while remainder > Beat(1, 1):
            remainder -= Beat(1, 1)
            splits.append(Beat(1, 1))

        for even_beat in even_beats:
            if even_beat <= remainder:
                splits.append(even_beat)
                remainder -= even_beat

            if remainder == Beat(0, 1):
                break

        return splits

    def next_bar(self):
        result = ceil(self.to_fraction())
        return Beat.from_fraction(result)


@dataclass()
class Note:
    position: Union[FretPosition, None]
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
