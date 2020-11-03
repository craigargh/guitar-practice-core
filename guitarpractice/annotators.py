from typing import List

from guitarpractice.constants import HAMMER_ON, PULL_OFF
from guitarpractice.models import GuitarShape, Note, Annotation


def hammer_on_asc(notes: List[Note]) -> List[Note]:
    prev_note = None
    for note in notes:
        if prev_note and note.position > prev_note.position and note.position.string == prev_note.position.string:
            note.tie = HAMMER_ON

        prev_note = note

    return notes


def pull_off_desc(notes: List[Note]) -> List[Note]:
    prev_note = None
    for note in notes:
        if prev_note and note.position < prev_note.position and note.position.string == prev_note.position.string:
            note.tie = PULL_OFF

        prev_note = note

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
