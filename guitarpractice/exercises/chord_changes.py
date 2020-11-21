import random
from functools import partial

from guitarpractice.models import Sequence
from guitarpractice.pickpatterns import strum
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes.chord_collections import c_major_scale_triad_chords


def chord_changes(variation) -> Sequence:
    chords = random.sample(c_major_scale_triad_chords(), 2)
    pick_pattern = partial(strum, length=4)

    return make_sequence(
        shapes=chords,
        pick_pattern=pick_pattern,
    )
