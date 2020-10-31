from itertools import cycle
from math import ceil
from typing import List, Callable

from .models import GuitarShape, Sequence, Note, FretPosition, Beat
from .pickpatterns import asc


def make_sequence(
        shapes: List[GuitarShape],
        shape_shifters: List[Callable] = None,
        pick_pattern: Callable = asc,
        annotators: List[Callable] = None,
        rhythm: List[Beat] = None,
) -> Sequence:
    pattern = []
    for shape in shapes:
        pattern.extend(pick_pattern(shape))

    if rhythm is None:
        rhythm = [Beat(duration=1)] * len(pattern)

    notes = apply_rhythm(pattern, rhythm)
    notes = fill_remaining_bar_with_rests(notes)

    return Sequence(notes=notes, shapes=shapes)


def positions_generator(shapes: List[GuitarShape]) -> List[FretPosition]:
    for shape in shapes:
        for position in shape.positions:
            yield position


def apply_rhythm(pattern: List[List[FretPosition]], rhythm: List[Beat]) -> List[Note]:
    only_rests = all(beat.rest for beat in rhythm)
    if only_rests:
        return [Note(position=None, duration=Beat(4, rest=True), order=0, elapsed_beats=Beat(4))]

    rhythm_cycle = cycle(rhythm)
    elapsed_beats = Beat(0)
    count = 0
    notes = []

    for position_group, beat in zip(pattern, rhythm_cycle):
        elapsed_beats += beat

        while beat.rest:
            rest = Note(position=None, duration=beat, elapsed_beats=elapsed_beats, order=count)
            notes.append(rest)

            beat = next(rhythm_cycle)
            elapsed_beats += beat
            count += 1

        for position in position_group:
            note = Note(position=position, duration=beat, elapsed_beats=elapsed_beats, order=count)
            notes.append(note)

        count += 1

    return notes


def fill_remaining_bar_with_rests(notes: List[Note]) -> List[Note]:
    last_beat = notes[-1].elapsed_beats
    next_bar = ceil(last_beat)
    difference = next_bar - last_beat

    remaining_beats = difference.tie_split()
    remaining_beats = sorted(remaining_beats)

    elapsed_beats = last_beat
    order = notes[-1].order

    fill_rests = []
    for beat in remaining_beats:
        beat.rest = True
        elapsed_beats += beat
        order += 1

        rest_note = Note(position=None, duration=beat, elapsed_beats=elapsed_beats, order=order)

        fill_rests.append(rest_note)

    return notes + fill_rests
