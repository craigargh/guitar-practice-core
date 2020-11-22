import random
from functools import partial

from guitarpractice import pickpatterns
from guitarpractice.models import Sequence
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes.chord_collections import c_major_scale_triad_chords


def chord_arpeggios(variation) -> Sequence:
    variation_map = {
        'level-1': level_one,
        'level-2': level_two,
        'level-3': level_three,
    }
    variation_function = variation_map[variation]

    return variation_function()


def level_one():
    order_choices = [
        pickpatterns.asc,
        pickpatterns.asc_and_desc,
    ]
    order = random.choice(order_choices)
    notes_per_arpeggio = random.choice([4, 6, 8])

    chords = random.sample(c_major_scale_triad_chords(), 2)
    pick_pattern = partial(order, length=notes_per_arpeggio)

    return make_sequence(
        shapes=chords,
        pick_pattern=pick_pattern,
        shape_labels=True,
        tab_labels=True,
    )


def level_two():
    return level_two_variation_one()


def level_two_variation_one():
    preset_pattern = random.choice(level_two_fixed_patterns())

    chords = random.sample(c_major_scale_triad_chords(), 2)
    pick_pattern = partial(pickpatterns.fixed_string_pattern, pattern=preset_pattern)

    return make_sequence(
        shapes=chords,
        pick_pattern=pick_pattern,
        shape_labels=True,
    )


def level_three():
    return level_three_variation_one()


def level_three_variation_one():
    preset_pattern = random.choice(level_three_fixed_patterns())

    chords = random.sample(c_major_scale_triad_chords(), 2)
    pick_pattern = partial(pickpatterns.fixed_string_pattern, pattern=preset_pattern)

    return make_sequence(
        shapes=chords,
        pick_pattern=pick_pattern,
        shape_labels=True,
    )


def level_two_fixed_patterns():
    return [
        ['r', '1', '2', '1', '2', '1', '2', '1'],
        ['r', '3', '2', '1', 'r', '3', '2', '1'],
        ['r', '3', '1', '2', 'r', '3', '1', '2'],
        ['r', '2', '1', '3', 'r', '2', '1', '3'],
        ['r', '2', '3', '1', 'r', '2', '3', '1'],
        ['r', '1', '2', '3', 'r', '1', '2', '3'],
        ['r', '1', '3', '2', 'r', '1', '3', '2'],
    ]


def level_three_fixed_patterns():
    return [
        ['r', '2', '1', '3', 'a', '2', '1', '3'],
        ['r', '3', '2', '1', 'a', '3', '2', '1'],
        ['r', '1', '2', '3', 'a', '1', '2', '3'],
        ['r', '2', '3', '1', 'a', '2', '3', '1'],
        ['r', '1', '3', '2', 'a', '1', '3', '2'],
        ['r', '1', 'a', '2', 'r', '1', 'a', '2'],
        ['r', '1', '2', '1', 'a', '1', '2', '1'],
        ['r', '2', 'a', '1', 'r', '2', 'a', '1'],
    ]
