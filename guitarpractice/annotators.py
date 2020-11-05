from typing import List

from guitarpractice.constants import HAMMER_ON, PULL_OFF, DOWN_PICK, UP_PICK
from guitarpractice.models import GuitarShape, Note, Annotation, Beat


def hammer_on_asc(notes: List[Note]) -> List[Note]:
    prev_note = None
    for note in notes:
        if prev_note and note.position > prev_note.position and note.position.string == prev_note.position.string:
            if not (UP_PICK in note.annotations or DOWN_PICK in note.annotations):
                note.tie = HAMMER_ON

        prev_note = note

    return notes


def pull_off_desc(notes: List[Note]) -> List[Note]:
    prev_note = None
    for note in notes:
        if prev_note and note.position < prev_note.position and note.position.string == prev_note.position.string:
            if not (UP_PICK in note.annotations or DOWN_PICK in note.annotations):
                note.tie = PULL_OFF

        prev_note = note

    return notes


def down_pick_on_the_beat(notes: List[Note]) -> List[Note]:
    prev_elapsed_beat = Beat(0, 1)

    for note in notes:
        beat_division = (prev_elapsed_beat + Beat(1, 1)).division
        if beat_division == 4 or beat_division == 2 or beat_division == 1:
            note.annotations.append(DOWN_PICK)

        prev_elapsed_beat = note.elapsed_beats

    return notes


def shape_name(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def hammer_on(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def pull_off(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def slide_up(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def slide_down(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def bend_up(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def bend_down(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def vibrato(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def palm_mute(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass


def finger_pick(shapes: List[GuitarShape], shapes_lengths: List[int], pattern: List[Note]) -> List[Annotation]:
    pass
