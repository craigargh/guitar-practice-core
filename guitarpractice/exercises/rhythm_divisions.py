'''
Exercise ideas:

- Combinations of:
  - quarter notes
  - eighth notes
  - rests
  - syncopation
  - triplets
  - gallops
  - sixteenth notes
  - irregular tuplets
'''
import random
from functools import partial
from itertools import chain

from guitarpractice.models import Sequence, Beat, FretPosition, GuitarShape
from guitarpractice.pickpatterns import repeat_each_position
from guitarpractice.sequencer import make_sequence

QUARTER_BEAT = [Beat(1, 4)]
QUARTER_REST = [Beat(1, 4, rest=True)]

DOUBLE_EIGHTH_BEAT = [Beat(1, 8), Beat(1, 8)]
EIGHTH_BEAT_AND_REST = [Beat(1, 8), Beat(1, 8, rest=True)]
SYNCOPATED_EIGHTH_BEAT = [Beat(1, 8, rest=True), Beat(1, 8)]

FOUR_SIXTEENTH_BEATS = [Beat(1, 16), Beat(1, 16), Beat(1, 16), Beat(1, 16)]
GALLOP = [Beat(1, 8), Beat(1, 16), Beat(1, 16)]
REVERSE_GALLOP = [Beat(1, 16), Beat(1, 16), Beat(1, 8)]
MIDDLE_GALLOP = [Beat(1, 16), Beat(1, 8), Beat(1, 16)]

REST_SYNCOPATED_GALLOP = [Beat(1, 16, rest=True), Beat(1, 16), Beat(1, 16), Beat(1, 16)]
REST_GALLOP = [Beat(1, 16), Beat(1, 16, rest=True), Beat(1, 16), Beat(1, 16)]
REST_MIDDLE_GALLOP = [Beat(1, 16), Beat(1, 16), Beat(1, 16, rest=True), Beat(1, 16)]
REST_REVERSE_GALLOP = [Beat(1, 16), Beat(1, 16), Beat(1, 16, rest=True), Beat(1, 16)]

THREE_EIGHTH_NOTE_TRIPLETS = [Beat(1, 12)] * 3
SIX_SIXTEENTH_NOTE_TRIPLETS = [Beat(1, 24)] * 6
TWELVE_THIRTY_SECOND_TRIPLETS = [Beat(1, 24)] * 12

SWING = [Beat(1, 12), Beat(1, 12, tie=True), Beat(1, 12)]

FIRST_REST_EIGHTH_TRIPLET = [Beat(1, 12, rest=True), Beat(1, 12), Beat(1, 12)]
MIDDLE_REST_EIGHTH_TRIPLET = [Beat(1, 12), Beat(1, 12, rest=True), Beat(1, 12)]
LAST_REST_EIGHTH_TRIPLET = [Beat(1, 12), Beat(1, 12), Beat(1, 12, rest=True)]
DOUBLE_REST_TRIPLET_FRONT = [Beat(1, 12, rest=True), Beat(1, 12, rest=True), Beat(1, 12)]
DOUBLE_REST_TRIPLET_END = [Beat(1, 12), Beat(1, 12, rest=True), Beat(1, 12, rest=True)]


def rhythm_divisions(variation: str = None) -> Sequence:
    variation_map = {
        'level-1': level_one,
        'level-2': level_two,
        # 'level-3': level_three,
    }
    variation_function = variation_map[variation]

    return variation_function()


def level_one():
    rhythm_options = [
        QUARTER_BEAT,
        QUARTER_BEAT,
        QUARTER_BEAT,
        QUARTER_BEAT,
        DOUBLE_EIGHTH_BEAT,
        DOUBLE_EIGHTH_BEAT,
        DOUBLE_EIGHTH_BEAT,
        QUARTER_REST,
    ]

    return assorted_rhythm(rhythm_options, 4)


def level_two():
    combos = [
        {
            'beat_options': [
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                DOUBLE_EIGHTH_BEAT,
                DOUBLE_EIGHTH_BEAT,
                DOUBLE_EIGHTH_BEAT,
                DOUBLE_EIGHTH_BEAT,
                QUARTER_REST,
            ],
            'length': 8,
        },
        {
            'beat_options': [
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                DOUBLE_EIGHTH_BEAT,
                THREE_EIGHTH_NOTE_TRIPLETS,
                THREE_EIGHTH_NOTE_TRIPLETS,
                THREE_EIGHTH_NOTE_TRIPLETS,
                THREE_EIGHTH_NOTE_TRIPLETS,
                QUARTER_REST,
            ],
            'length': 4,
        },
        {
            'beat_options': [
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                DOUBLE_EIGHTH_BEAT,
                FOUR_SIXTEENTH_BEATS,
                FOUR_SIXTEENTH_BEATS,
                FOUR_SIXTEENTH_BEATS,
                FOUR_SIXTEENTH_BEATS,
                QUARTER_REST,
            ],
            'length': 4,
        },
        {
            'beat_options': [
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                DOUBLE_EIGHTH_BEAT,
                GALLOP,
                GALLOP,
                GALLOP,
                GALLOP,
                QUARTER_REST,
            ],
            'length': 4,
        },
        {
            'beat_options': [
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                DOUBLE_EIGHTH_BEAT,
                REVERSE_GALLOP,
                REVERSE_GALLOP,
                REVERSE_GALLOP,
                REVERSE_GALLOP,
                QUARTER_REST,
            ],
            'length': 4,
        },
        {
            'beat_options': [
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                DOUBLE_EIGHTH_BEAT,
                SYNCOPATED_EIGHTH_BEAT,
                SYNCOPATED_EIGHTH_BEAT,
                SYNCOPATED_EIGHTH_BEAT,
                SYNCOPATED_EIGHTH_BEAT,
                QUARTER_REST,
            ],
            'length': 4,
        },
        {
            'beat_options': [
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                QUARTER_BEAT,
                DOUBLE_EIGHTH_BEAT,
                SWING,
                SWING,
                SWING,
                SWING,
                QUARTER_REST,
            ],
            'length': 4,
        }
    ]

    combo = random.choice(combos)
    return assorted_rhythm(combo['beat_options'], combo['length'])


def assorted_rhythm(rhythm_options, beat_count):
    position = FretPosition(0, 6)
    shape = GuitarShape('Open String', 'scale', positions=[position])

    rhythm_choices = [
        random.choice(rhythm_options)
        for _ in range(beat_count)
    ]
    rhythm = list(chain.from_iterable(rhythm_choices))

    picked_notes = [beat for beat in rhythm if not beat.rest]
    repeater = partial(repeat_each_position, repeats=len(picked_notes))

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        pick_pattern=repeater,
    )
