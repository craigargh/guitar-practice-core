from typing import List

from guitarpractice.models import GuitarShape
from guitarpractice.shapes import chord_shapes, open_chords_shapes
from guitarpractice.shapes import movable_chord_shapes

"""
major scale nine chords
Cmaj9-Dm9-Em7b9-Fmaj9-G9-Am9-Bm7b9b5

https://io9.gizmodo.com/a-chart-of-the-most-commonly-used-keys-shows-our-actual-1703086174
"""


def c_major_scale_triad_chords() -> List[GuitarShape]:
    return [
        chord_shapes.c_major(),
        chord_shapes.d_minor(),
        chord_shapes.e_minor(),
        chord_shapes.f_major(),
        chord_shapes.g_major(),
        chord_shapes.a_minor(),
        chord_shapes.b_diminished(),
    ]


def c_major_scale_seven_chords() -> List[GuitarShape]:
    return [
        chord_shapes.c_major_seven(),
        chord_shapes.d_minor_seven(),
        chord_shapes.e_minor_seven(),
        chord_shapes.f_major_seven(),
        chord_shapes.g_seven(),
        chord_shapes.a_minor_seven(),
        chord_shapes.b_minor_seven_flat_five(),
    ]


def c_major_scale_add_9_chords() -> List[GuitarShape]:
    return [
        chord_shapes.c_major_add_9(),
        chord_shapes.d_minor_add_9(),
        chord_shapes.e_minor_flat_nine(),
        chord_shapes.f_major_add_9(),
        chord_shapes.g_major_add_9(),
        chord_shapes.a_minor_add_9(),
        chord_shapes.b_diminished_flat_9(),
    ]


def movable_chords() -> List[GuitarShape]:
    return [
        movable_chord_shapes.movable_major_root_6_var_1(),
        movable_chord_shapes.movable_major_root_5_var_1(),
        movable_chord_shapes.movable_major_root_4_var_1(),
        movable_chord_shapes.movable_major_root_4_var_2(),
        movable_chord_shapes.movable_major_root_3_var_1(),
        movable_chord_shapes.movable_major_root_2_var_1(),
    ]


def open_chords() -> List[GuitarShape]:
    return [
        open_chords_shapes.open_major_root_6_var_1(),
        open_chords_shapes.open_major_root_6_var_2(),
        open_chords_shapes.open_major_root_5_var_1(),
        open_chords_shapes.open_major_root_5_var_2(),
        open_chords_shapes.open_major_root_4_var_1(),
    ]
