from math import floor
from typing import List, Callable

from .models import GuitarShape, Sequence, Note, FretPosition, Beat


def make_sequence(
        shapes: List[GuitarShape],
        shape_shifters: List[Callable] = None,
        pick_pattern: Callable = None,
        rhythm: List[Beat] = None,
        add_final_rest=False,
) -> Sequence:
    pattern = [
        [position]
        for position in positions_generator(shapes)
    ]

    if rhythm is None:
        rhythm = [Beat(duration=1)] * len(pattern)

    notes = apply_rhythm(pattern, rhythm, add_final_rest=add_final_rest)
    return Sequence(notes=notes, shapes=shapes)


def positions_generator(shapes: List[GuitarShape]) -> List[FretPosition]:
    for shape in shapes:
        for position in shape.positions:
            yield position


def apply_rhythm(pattern: List[List[FretPosition]], rhythm: List[Beat], add_final_rest=False) -> List[Note]:
    notes = []
    elapsed_beats = Beat(0)

    for position_group, beat in zip(pattern, rhythm):
        elapsed_beats += beat

        for position in position_group:
            note = Note(position=position, duration=beat, start_beat=elapsed_beats)
            notes.append(note)

    return notes
