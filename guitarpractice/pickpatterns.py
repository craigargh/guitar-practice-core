from typing import List, Callable

from guitarpractice.models import GuitarShape, FretPosition


def strum(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return [GuitarShape.positions]


def pick_asc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return [[]]


def pick_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return [[]]


def pick_asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_bass_and_asc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_bass_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_bass_asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_alternating_bass_and_asc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_alternating_bass_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_alternating_bass_asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_each_once_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_stepped_asc(shape: GuitarShape, step: int = 2, length: int = None) -> List[List[FretPosition]]:
    pass


def pick_stepped_desc(shape: GuitarShape, step: int = 2, length: int = None) -> List[List[FretPosition]]:
    pass


def alternate_patterns(patterns: List[Callable]) -> List[List[FretPosition]]:
    """
    Sequences multiple pick patterns to be applied to shapes alternatively.
    For example strum the first shape, then pick the second shape.
    """
    pass


def sequential_patterns(patterns: List[Callable]) -> List[List[FretPosition]]:
    """
    Sequences multiple pick patterns to be applied to the same shape sequentially.
    For example strum a chord shape and then pick it as an arpeggio.
    """
    pass
