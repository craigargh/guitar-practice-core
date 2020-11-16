"""
Exercise Ideas

- Power chords and open string palm muting
  - Power chord on the same string as the open string
  - Power chord on a different string to the open string
- Power chords and root note palm muting
- Changing power chords on a single string
- Changing power chords on a single string with palm muting
- Sliding power chords
- Changing power chords across two strings
- Power chords and individual note phrases
- Power chords and gallops
- Power chords and sixteenth notes


Pattern ideas:

Level 1:

0-0-0-0-c-c-c-c-

0-0-c-c-0-0-c-c-

0-c-c-c-0-c-c-c-

--c-c-c---c-c-c-
0-------0-------

c-c-c-c-c-c-c-c-

same, but palm-mute root note of power chord instead of open E

Level 2:

0-c-c-0-0-c-c-0-

0-c-c-0-c-c-0-0-

c-c-----c-c-----
----c-c-----c-c-

--------c---c---
0-0-0-0---c---c-

c-0-c-0-c-0-c-0-

0-c-0-c-0-c-0-c-

Level 3:

(gallop)
c-00-0-00-0-00-c----

0-00-0-00-0-00-c----

0-00-c----0-00-c----

0-00-0-00-c----c----

0-00-0-00-c-c-c-c-

0-00-c-c-0-00-c-c-

(reverse-gallop)

c-c-000-c-c-000-

c---000-000-000-

c-c-000-000-000-

000-000-000-c---

000-c---000-c---

"""
import random
from typing import List, Dict

from guitarpractice.models import Sequence, GuitarShape, FretPosition, Beat
from guitarpractice.pickpatterns import chug
from guitarpractice.sequencer import make_sequence


def generate_power_chord(string=6, fret=None) -> GuitarShape:
    if fret is None:
        fret = random.randrange(0, 12)

    positions = [
        FretPosition(string=string, fret=fret),
        FretPosition(string=string - 1, fret=fret + 2),
    ]
    return GuitarShape('Power Chord', 'chord', positions)


def open_string(string=6) -> GuitarShape:
    positions = [
        FretPosition(string=string, fret=0),
    ]
    return GuitarShape('Open String', 'single note', positions)


def metal_power_chords(variation: str) -> Sequence:
    return level_one()


def level_one() -> Sequence:
    position_choices = random.choice([
        level_one_variation_one(),
        level_one_variation_two(),
    ])

    rhythm = []
    shapes = []

    for _ in range(4):
        position = random.choice(position_choices)
        rhythm.extend(position['rhythm'])
        shapes.extend(position['shapes'])

    return make_sequence(
        shapes=shapes,
        rhythm=rhythm,
        pick_pattern=chug,
    )


def level_one_variation_one() -> List[Dict]:
    return [
        {
            'shapes': [
                generate_power_chord()
            ],
            'rhythm': [
                Beat(1, 4)
            ],
        },
        {
            'shapes': [
                open_string(),
                open_string(),
            ],
            'rhythm': [
                Beat(1, 8),
                Beat(1, 8),
            ],
        },
    ]


def level_one_variation_two() -> List[Dict]:
    chord_root = random.randrange(0, 12)
    second_chord_offset = random.randrange(-3, 3)
    second_chord_root = min(max(0, chord_root + second_chord_offset), 12)

    return [
        {
            'shapes': [
                generate_power_chord(fret=chord_root),
                generate_power_chord(fret=second_chord_root),
            ],
            'rhythm': [
                Beat(1, 8),
                Beat(1, 8)
            ],
        },
        {
            'shapes': [
                open_string(),
                open_string(),
            ],
            'rhythm': [
                Beat(1, 8),
                Beat(1, 8),
            ],
        },
    ]
