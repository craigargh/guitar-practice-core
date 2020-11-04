'''
Exercise ideas

Level one:
- Hammer-ons on between two notes
- Pull-offs between two notes
- Hammer-ons and pull off between two notes

Level two:
- Hammer-ons between multiple notes on a single string
- Hammer-ons between two notes on multiple strings
- Pull-offs between multiple notes on a single string
- Pull-offs between two notes on multiple strings
- Hammer-ons and pull-offs between multiple notes on a single string
- Two note hammers/pulls but faster (16th note)

Level three:
- Hammers-ons and/or pull-offs on a single string, but faster rhythm (16th notes)
- Hammer-ons ascending a scale
- Pull-offs descending a scale
- Hammer-ons and pull-offs ascending and descending a scale

Level four:
- Trills
- Legato
- Level three but faster
- Chord hammer-ons/pull-offs (hammering on a single extra note while a chord is barred)
- Double stop hammer-ons/pull-offs (hammer on two strings at one)


Reference material:
https://www.youtube.com/watch?v=Gtx8PGK4Aac


'''
import random
from functools import partial

from guitarpractice.annotators import hammer_on_asc, pull_off_desc
from guitarpractice.models import Sequence, GuitarShape, FretPosition, Beat
from guitarpractice.pickpatterns import asc, desc, alternating_bass_asc_and_desc, asc_and_desc
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes.scale_collections import c_major_pentatonic_modes


def technique_hammers_pulls(variation: str = None) -> Sequence:
    variation_map = {
        'level-1': level_one,
        'level-2': level_two,
        'level-3': level_three,
    }
    variation_function = variation_map[variation]
    return variation_function()


def level_one():
    base_fret = random.randrange(1, 9)
    second_fret = base_fret + random.randrange(1, 4)
    string = random.randrange(1, 7)

    positions = [
        FretPosition(base_fret, string),
        FretPosition(second_fret, string),
    ]
    shape = GuitarShape(category='scale', name='Single string notes', positions=positions)
    rhythm = [Beat(1, 8)]

    combos = [
        {
            'annotators': [hammer_on_asc],
            'pick_pattern': partial(asc, length=8)
        },
        {
            'annotators': [pull_off_desc],
            'pick_pattern': partial(desc, length=8)
        },
        {
            'annotators': [hammer_on_asc, pull_off_desc],
            'pick_pattern': partial(asc, length=8)
        },
        {
            'annotators': [pull_off_desc, hammer_on_asc],
            'pick_pattern': partial(desc, length=8)
        },
    ]

    combo = random.choice(combos)

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        pick_pattern=combo['pick_pattern'],
        annotators=combo['annotators'],
    )


def level_two():
    combos = [
        {
            'shapes': [single_string_shape(positions_length=4)],
            'annotators': [hammer_on_asc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(asc, length=8),
        },
        {
            'shapes': [single_string_shape(positions_length=4)],
            'annotators': [pull_off_desc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(desc, length=8),
        },
        {
            'shapes': [single_string_shape(positions_length=4)],
            'annotators': [hammer_on_asc, pull_off_desc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(alternating_bass_asc_and_desc, length=8),
        },
        {
            'shapes': [single_string_shape(positions_length=3)],
            'annotators': [hammer_on_asc, pull_off_desc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(asc_and_desc, length=8),
        },
        {
            'shapes': [two_string_repeated_shape()],
            'annotators': [hammer_on_asc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(asc, length=8),
        },
        {
            'shapes': [two_string_repeated_shape()],
            'annotators': [pull_off_desc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(desc, length=8),
        },
        {
            'shapes': [single_string_shape(positions_length=2)],
            'annotators': [hammer_on_asc],
            'rhythm': [Beat(1, 16)],
            'pick_pattern': partial(asc, length=16),
        },
        {
            'shapes': [single_string_shape(positions_length=2)],
            'annotators': [pull_off_desc],
            'rhythm': [Beat(1, 16)],
            'pick_pattern': partial(desc, length=16),
        },
    ]

    combo = random.choice(combos)
    return make_sequence(**combo)


def level_three():
    combos = [
        {
            'shapes': [single_string_shape(positions_length=4)],
            'annotators': [hammer_on_asc],
            'rhythm': [Beat(1, 16)],
            'pick_pattern': partial(asc, length=16),
        },
        {
            'shapes': [single_string_shape(positions_length=4)],
            'annotators': [pull_off_desc],
            'rhythm': [Beat(1, 16)],
            'pick_pattern': partial(desc, length=16),
        },
        {
            'shapes': [single_string_shape(positions_length=4)],
            'annotators': [hammer_on_asc, pull_off_desc],
            'rhythm': [Beat(1, 16)],
            'pick_pattern': partial(alternating_bass_asc_and_desc, length=8),
        },
        {
            'shapes': [single_string_shape(positions_length=3)],
            'annotators': [hammer_on_asc, pull_off_desc],
            'rhythm': [Beat(1, 16)],
            'pick_pattern': partial(asc_and_desc, length=16),
        },
        {
            'shapes': [random.choice(c_major_pentatonic_modes())],
            'annotators': [hammer_on_asc, pull_off_desc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(asc_and_desc),
        },
        {
            'shapes': [random.choice(c_major_pentatonic_modes())],
            'annotators': [hammer_on_asc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(asc),
        },
        {
            'shapes': [random.choice(c_major_pentatonic_modes())],
            'annotators': [pull_off_desc],
            'rhythm': [Beat(1, 8)],
            'pick_pattern': partial(desc),
        },
    ]

    combo = random.choice(combos)
    return make_sequence(**combo)


def single_string_shape(positions_length):
    positions_length -= 1

    string = random.randrange(1, 7)
    base_fret = random.randrange(1, 9)
    frets = [base_fret]

    fret_offsets = [1, 2, 3]
    random.shuffle(fret_offsets)

    for _ in range(positions_length):
        frets.append(fret_offsets.pop() + base_fret)

    positions = [
        FretPosition(fret, string)
        for fret in frets
    ]

    return GuitarShape(
        positions=positions,
        category='scale',
        name='Single string shape'
    )


def two_string_repeated_shape():
    shape = single_string_shape(2)

    new_positions = [
        FretPosition(
            fret=position.fret,
            string=position.string - 1 if position.string != 1 else 2
        )
        for position in shape.positions
    ]

    shape.positions.extend(new_positions)

    return shape
