import random
from functools import partial

from guitarpractice import pickpatterns
from guitarpractice.models import Sequence, Beat
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes.scale_collections import c_major_pentatonic_modes, c_major_modes
from guitarpractice.shapeshifters import shift_vertically


def scale_shapes(variation: str):
    variations = {
        'major': major_scale,
        'major-pentatonic': major_pentatonic_scale,
    }
    variation_function = variations[variation]
    return variation_function()


def major_pentatonic_scale() -> Sequence:
    shape = random.choice(c_major_pentatonic_modes())
    pattern = random.choice([
        pickpatterns.asc,
        pickpatterns.desc,
        pickpatterns.asc_and_desc,
        partial(pickpatterns.alternating_bass_and_asc, length=10)
    ])
    rhythm = [Beat(duration=1, division=8)]
    lowest_fret = random.randrange(1, 13)

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        pick_pattern=pattern,
        shape_shifters=[partial(shift_vertically, lowest_fret=lowest_fret)],
        shape_labels=True,
    )


def major_scale() -> Sequence:
    shape = random.choice(c_major_modes())
    pattern = random.choice([
        pickpatterns.asc,
        pickpatterns.desc,
        pickpatterns.asc_and_desc,
        partial(pickpatterns.alternating_bass_and_asc, length=14)
    ])
    rhythm = [Beat(duration=1, division=8)]
    lowest_fret = random.randrange(1, 13)

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        pick_pattern=pattern,
        shape_shifters=[partial(shift_vertically, lowest_fret=lowest_fret)],
        shape_labels=True,
    )
