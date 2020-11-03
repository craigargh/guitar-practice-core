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
- Hammer-ons and pull-offs between two notes on multiple strings

Level three:
- Hammers-ons and/or pull-offs on a single string, but faster rhythm (e.g. 8th or 16th notes)
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
from guitarpractice.pickpatterns import asc, desc
from guitarpractice.sequencer import make_sequence


def technique_hammers_pulls(variation: str = None) -> Sequence:
    variation_map = {
        'level-one': level_one,
        'level-two': level_two,
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
            'positions': [single_string_shape(positions_length=4)],
            'annotators': [hammer_on_asc],
            'rhythm': [Beat(1, 4)],
            'pick_pattern': partial(desc, length=8),
        }
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