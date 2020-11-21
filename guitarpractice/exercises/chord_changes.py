import random
from functools import partial

from guitarpractice.annotators import shape_name
from guitarpractice.models import Sequence
from guitarpractice.pickpatterns import strum, bass_and_strum
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes.chord_collections import c_major_scale_triad_chords, c_major_scale_seven_chords, \
    c_major_scale_add_9_chords


def chord_changes(variation) -> Sequence:
    variation_map = {
        'level-1': level_one,
        'level-2': level_two,
        # 'level-3': level_three,
    }
    variation_function = variation_map[variation]

    return variation_function()


def level_one():
    chords = random.sample(c_major_scale_triad_chords(), 2)
    pick_pattern = partial(strum, length=4)

    return make_sequence(
        shapes=chords,
        pick_pattern=pick_pattern,
        shape_labels=True,
        annotators=[shape_name]
    )


def level_two():
    chords = random.choice([
        level_two_chords_variation_one(),
        level_two_chords_variation_two(),
    ])
    order = random.choice([bass_and_strum, strum, strum, strum])

    pick_pattern = partial(order, length=4)

    return make_sequence(
        shapes=chords,
        pick_pattern=pick_pattern,
        shape_labels=True,
        annotators=[shape_name]
    )


def level_two_chords_variation_one():
    return level_two_chords(4)


def level_two_chords_variation_two():
    """
    Chord sequence that repeats the first chord every other bar
    """
    selected_chords = level_two_chords(3)
    selected_chords.insert(2, selected_chords[0])

    return selected_chords


def level_two_chords(qty):
    alternate_chords = random.choice([c_major_scale_seven_chords, c_major_scale_add_9_chords])
    all_chords = c_major_scale_triad_chords() + alternate_chords()

    return random.sample(all_chords, qty)
