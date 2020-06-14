from typing import List, Callable

from guitarpractice.models import GuitarShape, FretPosition


def strum(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    validate_length(length)

    repeats = 1 if length is None else length
    return [shape.positions] * repeats


def asc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return [[]]


def desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return [[]]


def asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def bass_and_asc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def bass_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def bass_asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def alternating_bass_and_asc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def alternating_bass_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def alternating_bass_asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def stepped_asc(shape: GuitarShape, step: int = 2, length: int = None) -> List[List[FretPosition]]:
    pass


def stepped_desc(shape: GuitarShape, step: int = 2, length: int = None) -> List[List[FretPosition]]:
    pass


def randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def root_and_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def alternating_root_and_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def each_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def root_and_each_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def alternating_root_and_each_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
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
