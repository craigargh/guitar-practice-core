from dataclasses import dataclass
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
class Note:
    position: FretPosition
    start_beat: float
    duration: float
    division: int = None


@dataclass()
class Annotation:
    category: str
    start_beat: float
    duration: float


@dataclass()
class Sequence:
    notes: List[Note]
    annotations: List[Annotation]
    shapes: List[GuitarShape]
