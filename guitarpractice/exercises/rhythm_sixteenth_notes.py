import random
from functools import partial

from guitarpractice.models import Sequence, FretPosition, GuitarShape, Beat
from guitarpractice.sequencer import make_sequence
from guitarpractice.sequenceshifters import repeat_each_position


def rhythm_sixteenth_notes(variation: str) -> Sequence:
    return level_one()


def level_one() -> Sequence:
    fret_choice = random.choice(list(range(0, 13)))
    string_choice = random.choice([6, 6, 6, 5, 5, 4, 3, 2, 1])

    position = FretPosition(fret=fret_choice, string=string_choice)
    shape = GuitarShape('Fifth fret', 'note', positions=[position])
    repeater = partial(repeat_each_position, repeats=32)

    rhythm = [Beat(duration=1, division=16)]

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        sequence_shifters=[repeater],
    )
