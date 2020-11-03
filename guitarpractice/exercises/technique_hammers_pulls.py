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

from guitarpractice.annotators import hammer_on_asc
from guitarpractice.models import Sequence, GuitarShape, FretPosition, Beat
from guitarpractice.pickpatterns import asc
from guitarpractice.sequencer import make_sequence


def technique_hammers_pulls(variation: str = None) -> Sequence:
    base_fret = random.randrange(1, 9)
    second_fret = base_fret + random.randrange(1, 4)
    string = random.randrange(1, 7)

    positions = [
        FretPosition(base_fret, string),
        FretPosition(second_fret, string),
    ]
    shape = GuitarShape(category='scale', name='Single string notes', positions=positions)
    rhythm = [Beat(1, 8)]
    pick_pattern = partial(asc, length=8)

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        pick_pattern=pick_pattern,
        annotators=[hammer_on_asc]
    )
