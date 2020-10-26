from itertools import cycle
from typing import List, Callable

from .models import GuitarShape, Sequence, Note, FretPosition, Beat
from .pickpatterns import asc


def make_sequence(
        shapes: List[GuitarShape],
        shape_shifters: List[Callable] = None,
        pick_pattern: Callable = asc,
        annotators: List[Callable] = None,
        sequence_shifters: List[Callable] = None,
        rhythm: List[Beat] = None,
) -> Sequence:
    pattern = []
    for shape in shapes:
        pattern.extend(pick_pattern(shape))

    if sequence_shifters is not None:
        for sequence_shifters in sequence_shifters:
            pattern = sequence_shifters(pattern)

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
        return [Note(position=None, duration=Beat(4, rest=True), order=0)]

    rhythm_cycle = cycle(rhythm)
    elapsed_beats = 0
    notes = []

    for position_group, beat in zip(pattern, rhythm_cycle):

        while beat.rest:
            rest = Note(position=None, duration=beat, order=elapsed_beats)
            notes.append(rest)

            beat = next(rhythm_cycle)
            elapsed_beats += 1

        for position in position_group:
            note = Note(position=position, duration=beat, order=elapsed_beats)
            notes.append(note)

        elapsed_beats += 1

    return notes
