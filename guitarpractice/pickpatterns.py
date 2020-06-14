from typing import List, Callable

from guitarpractice.models import GuitarShape, FretPosition


def strum(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    validate_length(length)

    repeats = 1 if length is None else length
    return [shape.positions] * repeats


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


def sequential_patterns(patterns: List[Callable], strip_end_positions=False) -> List[List[FretPosition]]:
    """
    Sequences multiple pick patterns to be applied to the same shape sequentially.
    For example strum a chord shape and then pick it as an arpeggio.
    """
    pass


def validate_length(length):
    if length is not None and length < 1:
        raise ValueError(f'Length of {length} is not allowed. Must be greater than 0.')
