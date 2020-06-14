from itertools import cycle
from math import floor
from typing import List, Callable

from .models import GuitarShape, Sequence, Note, FretPosition, Beat


def make_sequence(
        shapes: List[GuitarShape],
        shape_shifters: List[Callable] = None,
        pick_pattern: Callable = None,
        rhythm: List[Beat] = None,
) -> Sequence:
    pattern = [
        [position]
        for position in positions_generator(shapes)
    ]

    if rhythm is None:
        rhythm = [Beat(duration=1)] * len(pattern)

    notes = apply_rhythm(pattern, rhythm)
    return Sequence(notes=notes, shapes=shapes)


def positions_generator(shapes: List[GuitarShape]) -> List[FretPosition]:
    for shape in shapes:
        for position in shape.positions:
            yield position


def apply_rhythm(pattern: List[List[FretPosition]], rhythm: List[Beat]) -> List[Note]:
    only_rests = all(beat.rest for beat in rhythm)
    if only_rests:
        return [Note(position=None, duration=Beat(4, rest=True), start_beat=Beat(1))]

    rhythm_cycle = cycle(rhythm)
    elapsed_beats = Beat(1)
    notes = []

    for position_group, beat in zip(pattern, rhythm_cycle):
        while beat.rest:
            rest = Note(position=None, duration=beat, start_beat=elapsed_beats)
            notes.append(rest)

            elapsed_beats += beat
            beat = next(rhythm_cycle)

        for position in position_group:
            note = Note(position=position, duration=beat, start_beat=elapsed_beats)
            notes.append(note)

        elapsed_beats += beat

    return notes
