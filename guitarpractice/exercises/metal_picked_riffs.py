import random
from functools import partial

from guitarpractice.pickpatterns import fixed_order_pattern
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes import major_scale_shapes
from guitarpractice.shapes.fixed_order_patterns import level_one_picked_metal_patterns


def metal_picked_riffs():
    shape_choices = [
        major_scale_shapes.c_ionian(),
        major_scale_shapes.a_aeolian(),
    ]
    shape = random.choice(shape_choices)

    preset_pattern = random.choice(level_one_picked_metal_patterns())
    pick_pattern = partial(fixed_order_pattern, pattern=preset_pattern)

    return make_sequence(
        [shape],
        pick_pattern=pick_pattern
    )
