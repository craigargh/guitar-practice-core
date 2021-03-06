from itertools import cycle
from operator import attrgetter
from typing import List, Callable

from .endings import fill_remaining_bar_with_rests
from .models import GuitarShape, Sequence, Note, FretPosition, Beat
from .pickpatterns import asc


def make_sequence(
        shapes: List[GuitarShape],
        shape_shifters: List[Callable] = None,
        pick_pattern: Callable = asc,
        annotators: List[Callable] = None,
        rhythm: List[Beat] = None,
        ending: Callable = fill_remaining_bar_with_rests,
        shape_labels: bool = False,
        tab_labels: bool = False,
        recalculate_shape: bool = False,
) -> Sequence:
    adjusted_shapes = []

    for shape in shapes:
        adjusted_shape = shape

        if shape_shifters:
            for shape_shifter in shape_shifters:
                adjusted_shape = shape_shifter(adjusted_shape)

        adjusted_shapes.append(adjusted_shape)

    pattern = []
    label_map = {}
    for shape in adjusted_shapes:
        if tab_labels:
            index = len(pattern)
            label = shape.short_name
            label_map[index] = label

        pattern.extend(pick_pattern(shape))

    if rhythm is None:
        rhythm = [Beat(duration=1)] * len(pattern)

    notes = apply_rhythm(pattern, rhythm)

    if tab_labels:
        notes = apply_tab_labels(notes, label_map)

    if annotators:
        for annotator in annotators:
            notes = annotator(notes, shapes)

    notes = ending(notes)

    sorted_shapes = []
    if not recalculate_shape:
        for shape in adjusted_shapes:
            if shape not in sorted_shapes:
                sorted_shapes.append(shape)
    else:
        positions = [note.position for note in notes if note.position is not None]
        shape = GuitarShape('Shape', 'shape', positions=positions)
        sorted_shapes.append(shape)

    return Sequence(notes=notes, shapes=sorted_shapes, shape_labels=shape_labels)


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


def apply_tab_labels(notes, label_map):
    prev_label = ""

    for index, label in label_map.items():
        if label == prev_label or label is None:
            continue

        rest_count = 0
        for note in notes:
            if note.duration.rest:
                rest_count += 1
                continue

            if note.order == index + rest_count:
                note.annotations.append(f'label:{label}')

        prev_label = label

    return notes
