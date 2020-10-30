import random
from functools import partial

from guitarpractice import pickpatterns
from guitarpractice.models import Sequence, Beat
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes.scale_collections import c_major_pentatonic_modes, c_major_modes


def scale_shapes(variation: str):
    variations = {
        'c-major': c_major,
        'c-major-pentatonic': c_major_pentatonic,
    }
    variation_function = variations[variation]
    return variation_function()


def c_major_pentatonic() -> Sequence:
    shape = random.choice(c_major_pentatonic_modes())
    pattern = random.choice([
        pickpatterns.asc,
        pickpatterns.desc,
        pickpatterns.asc_and_desc,
        partial(pickpatterns.alternating_bass_and_asc, length=10)
    ])
    rhythm = [Beat(duration=1, division=8)]

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        pick_pattern=pattern
    )


def c_major() -> Sequence:
    shape = random.choice(c_major_modes())
    pattern = random.choice([
        pickpatterns.asc,
        pickpatterns.desc,
        pickpatterns.asc_and_desc,
        partial(pickpatterns.alternating_bass_and_asc, length=14)
    ])
    rhythm = [Beat(duration=1, division=8)]

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        pick_pattern=pattern
    )
