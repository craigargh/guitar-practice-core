import random
from functools import partial

from guitarpractice.models import Beat, GuitarShape, FretPosition
from guitarpractice.pickpatterns import fixed_order_pattern, adjust_length
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes import major_scale_shapes
from guitarpractice.shapes.fixed_order_patterns import level_one_picked_metal_patterns


def metal_picked_riffs(variation=None):
    """
    0-0-0-0-n-n-n-n-

    n-n-0-0-0-0-0-0-|n-n-0-0-0-0-0-0-
    n-0-0-0-n-0-0-0-|n-0-0-0-n-0-0-0-
    n-0-n-0-n-0-n-0-



    n-n-n-n-n-n-n-n-
    n-0-n-0-n-0-n-0-|n-0-n-0-n-0-n-0-
    0-n-0-n-0-n-0-n-|0-n-0-n-0-n-0-n-
    n-n-0-0-n-n-0-0-|n-n-0-0-n-n-0-0-

    triplet chugs

    """
    shape_choices = [
        major_scale_shapes.c_ionian(),
        major_scale_shapes.a_aeolian(),
    ]
    shape = random.choice(shape_choices)

    combos = [
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 2,
            'in_between_beats': 0,
            'length': 8,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 0.5,
            'length': 8,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0.5,
            'in_between_beats': 0.5,
            'length': 8,
        },
    ]
    combo = random.choice(combos)

    preset_pattern = random.choice(combo['preset_patterns'])
    pick_pattern = partial(fixed_order_pattern, pattern=preset_pattern)

    chug_pattern = partial(
        chug,
        length=combo['length'],
        order=pick_pattern,
        preceding_beats=combo['preceding_beats'],
        in_between_beats=combo['in_between_beats'],
    )

    rhythm = [Beat(1, 8)]

    return make_sequence(
        [shape],
        pick_pattern=chug_pattern,
        rhythm=rhythm,
    )


def chug(shape: GuitarShape, length: int = None, order: callable = None, preceding_beats=0, in_between_beats=0,
         notes_per_chug=2):
    pick_pattern = order(shape)
    chug_position = [FretPosition(fret=0, string=6)]

    if in_between_beats > 0:
        new_pattern = []
        for item in pick_pattern:
            new_pattern.append(item)
            new_pattern.extend([chug_position] * int(notes_per_chug * in_between_beats))

        pick_pattern = new_pattern

    if preceding_beats > 0:
        pick_pattern = ([chug_position] * int(preceding_beats * notes_per_chug)) + pick_pattern

    pick_pattern = adjust_length(pick_pattern, length=length)
    return pick_pattern
