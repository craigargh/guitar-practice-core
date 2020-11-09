from dataclasses import dataclass, field
from fractions import Fraction
from math import ceil
from typing import List, Union


@dataclass()
class FretPosition:
    fret: int
    string: int
    finger: Union[int, None] = None
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
            return Beat(other.duration, other.division)

        result = self.to_fraction() + other.to_fraction()

        beat = Beat.from_fraction(result)
        beat.rest = self.rest

        return beat

    def __sub__(self, other):
        as_fraction = self.to_fraction() - other.to_fraction()

        result = Beat.from_fraction(as_fraction)
        result.rest = self.rest

        if result.duration < 0:
            raise ValueError('Beat duration cannot be negative')

        return result

    def __eq__(self, other):
        if self.division == other.division and self.duration == other.duration and self.rest == other.rest:
            return True

        return self.duration * other.division == other.duration * self.division and self.rest == other.rest

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
        if self.division % 3 == 0:
            even_beats = [
                Beat(1, 1, rest=self.rest),
                Beat(1, 3, rest=self.rest),
                Beat(1, 3, rest=self.rest),
                Beat(1, 6, rest=self.rest),
                Beat(1, 12, rest=self.rest),
                Beat(1, 24, rest=self.rest),
            ]
        else:
            even_beats = [
                Beat(1, 1, rest=self.rest),
                Beat(1, 2, rest=self.rest),
                Beat(1, 4, rest=self.rest),
                Beat(1, 8, rest=self.rest),
                Beat(1, 16, rest=self.rest),
                Beat(1, 32, rest=self.rest),
            ]

        while remainder > Beat(1, 1, rest=self.rest):
            remainder -= Beat(1, 1, rest=self.rest)
            splits.append(Beat(1, 1, rest=self.rest))

        for even_beat in even_beats:
            if even_beat <= remainder:
                splits.append(even_beat)
                remainder -= even_beat

            if remainder == Beat(0, 1, rest=self.rest):
                break

        return splits

    def next_bar(self):
        result = ceil(self.to_fraction())
        return Beat.from_fraction(result)

    def is_new_bar(self) -> bool:
        return (self + Beat(1, 1)).division == 1


@dataclass()
class Annotation:
    category: str


@dataclass()
class Note:
    position: Union[FretPosition, None]
    duration: Beat
    elapsed_beats: Beat
    order: int
    annotations: List[str] = field(default_factory=list)
    tie: str = None


@dataclass()
class Sequence:
    notes: List[Note]
    shapes: List[GuitarShape]
