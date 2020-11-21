import random
from functools import partial

from guitarpractice import pickpatterns
from guitarpractice.models import Sequence
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes.chord_collections import c_major_scale_triad_chords


def chord_arpeggios(variation) -> Sequence:
    variation_map = {
        'level-1': level_one,
        # 'level-2': level_two,
        # 'level-3': level_three,
    }
    variation_function = variation_map[variation]

    return variation_function()


def level_one():
    order_choices = [
        pickpatterns.asc,
        pickpatterns.asc_and_desc,
        pickpatterns.bass_and_asc,
        pickpatterns.bass_asc_and_desc,

    ]
    order = random.choice(order_choices)
    notes_per_arpeggio = random.choice([4, 6, 8])

    chords = random.sample(c_major_scale_triad_chords(), 2)
    pick_pattern = partial(order, length=notes_per_arpeggio)

    return make_sequence(
        shapes=chords,
        pick_pattern=pick_pattern,
        shape_labels=True,
    )
