from typing import List

from guitarpractice.models import FretPosition


def repeat_each_position(pattern: List[List[FretPosition]], repeats: int = 2) -> List[List[FretPosition]]:
    """
    Play each fret in the sequence two or more times
    """
    new_positions = []
    for positions in pattern:
        new_positions.extend([positions] * repeats)

    return new_positions
