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

c-c-c-c-c-c-c-c-

0-c-c-c-0-c-c-c-

--c-c-c---c-c-c-
0-------0-------


same, but palm-mute root note of power chord instead of open E

Level 2:
level 1, but more chords

Level 3:

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
from typing import List, Dict, Callable

from guitarpractice.annotators import palm_mute_single
from guitarpractice.models import Sequence, GuitarShape, FretPosition, Beat
from guitarpractice.pickpatterns import chug, strum
from guitarpractice.sequencer import make_sequence


def metal_power_chords(variation: str) -> Sequence:
    variation_map = {
        'level-1': level_one,
        'level-2': level_two,
    }

    return variation_map[variation]()


def level_one() -> Sequence:
    return build_sequence_from_combo(level_one_combos())


def level_one_combos():
    return [
        {
            'choices': [
                {
                    'shapes': [
                        power_chord()
                    ],
                    'rhythm': [
                        Beat(1, 4)
                    ],
                },
            ],
            'repeats': 4
        },
        {
            'choices': [
                {
                    'shapes': [
                        power_chord()
                    ],
                    'rhythm': [
                        Beat(4, 4)
                    ],
                },
                {
                    'shapes': [
                        power_chord()
                    ],
                    'rhythm': [
                        Beat(4, 4)
                    ],
                },
            ],
            'repeats': 2,
        },
        {
            'choices': [
                {
                    'shapes': [
                        *repeated_power_chord(2),
                        *repeated_power_chord(2)
                    ],
                    'rhythm': [
                        Beat(1, 4),
                    ],
                },
            ],
            'repeats': 1,
        },
        {
            'choices': [
                {
                    'shapes': single_and_repeated_power_chords(2),
                    'rhythm': [
                        Beat(1, 2),
                        Beat(1, 4),
                        Beat(1, 4),
                    ],
                },
            ],
            'repeats': 2,
        },
        {
            'choices': [
                {
                    'shapes': single_and_repeated_power_chords(2),
                    'rhythm': [
                        Beat(1, 1),
                        Beat(1, 2),
                        Beat(1, 2),
                    ],
                },
            ],
            'repeats': 1,
        },
    ]


def level_two() -> Sequence:
    return build_sequence_from_combo(level_two_combos())


def build_sequence_from_combo(combos):
    combo = random.choice(combos)

    rhythm = []
    shapes = []

    for _ in range(combo.get('repeats', 4)):
        position = random.choice(combo.get('choices'))
        rhythm.extend(position['rhythm'])
        shapes.extend(position['shapes'])

    return make_sequence(
        shapes=shapes,
        rhythm=rhythm,
        pick_pattern=chug,
        annotators=[palm_mute_single]
    )


def level_two_combos():
    return [
        *level_two_chord_and_chug_combos(string=6),
        *level_two_chord_and_chug_combos(string=5),
        *level_two_power_chord_and_root_note_combos()
    ]


def level_two_power_chord_and_root_note_combos():
    chord, root_note = power_chord_and_root_note()
    return [
        {
            'choices': [
                {
                    'shapes': [
                        chord
                    ],
                    'rhythm': [
                        Beat(1, 4)
                    ],
                },
                {
                    'shapes': [
                        root_note,
                        root_note,
                    ],
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8),
                    ],
                },
            ],
            'repeats': 4
        },
        {
            'choices': [
                {
                    'shapes': [
                        chord,
                        chord,
                    ],
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8),
                    ],
                },
                {
                    'shapes': [
                        root_note,
                        root_note,
                    ],
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8),
                    ],
                },
            ],
            'repeats': 4
        },
        {
            'choices': [
                {
                    'shapes': [
                        root_note,
                        chord,
                        chord,
                        chord,
                    ],
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8),
                        Beat(1, 8),
                        Beat(1, 8),
                    ],
                },
            ],
            'repeats': 2
        },
    ]


def level_two_chord_and_chug_combos(string: int):
    return [
        {
            'choices': [
                {
                    'shapes': [
                        power_chord(string=string)
                    ],
                    'rhythm': [
                        Beat(1, 4)
                    ],
                },
                eighth_chugs(),
            ],
            'repeats': 4
        },
        {
            'choices': [
                {
                    'shapes': repeated_power_chord(2, string=string),
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8)
                    ],
                },
                eighth_chugs(),
            ],
            'repeats': 4
        },
        {
            'choices': [
                {
                    'shapes': [
                        open_string(),
                        *repeated_power_chord(3, string=string)
                    ],
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8),
                        Beat(1, 8),
                        Beat(1, 8),
                    ],
                },
            ],
            'repeats': 2,
        },
        {
            'choices': [
                {
                    'shapes': [
                        open_string(),
                        open_string(),
                        open_string(),
                        power_chord(string=string)
                    ],
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8),
                        Beat(1, 8),
                        Beat(1, 8),
                    ],
                },
            ],
            'repeats': 2,
        },
    ]


def level_three_combos():
    return [
        {
            'choices': [
                {
                    'shapes': power_chord_sequence(2),
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8)
                    ],
                },
                eighth_chugs(),
            ],
            'repeats': 4
        },
        {
            'choices': [
                {
                    'shapes': [
                        open_string(),
                        *power_chord_sequence(3)
                    ],
                    'rhythm': [
                        Beat(1, 8),
                        Beat(1, 8),
                        Beat(1, 8),
                        Beat(1, 8),
                    ],
                },
            ],
            'repeats': 2,
        },
    ]


def power_chord_and_root_note():
    chord = power_chord()
    root_note = chord.positions[0]
    root_note_shape = GuitarShape('Root note', 'note', positions=[root_note])

    return chord, root_note_shape


def power_chord(string=6, fret=None) -> GuitarShape:
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


def eighth_chugs() -> Dict:
    return {
        'shapes': [
            open_string(),
            open_string(),
        ],
        'rhythm': [
            Beat(1, 8),
            Beat(1, 8),
        ],
    }


def power_chord_sequence(qty: int, root_fret: int = None, string: int = 6) -> List[GuitarShape]:
    root_notes = []

    if root_fret is None:
        root_fret = random.randrange(0, 12)
    root_notes.append(root_fret)

    for _ in range(qty - 1):
        chord_offset = random.randrange(-3, 3)
        chord_root = min(max(0, root_fret + chord_offset), 12)

        root_notes.append(chord_root)

    chords = [
        power_chord(string=string, fret=root_position)
        for root_position in root_notes
    ]

    return chords


def repeated_power_chord(repeats: int, root_fret: int = None, string: int = 6) -> List[GuitarShape]:
    if root_fret is None:
        root_fret = random.randrange(0, 12)

    return [
        power_chord(string=string, fret=root_fret)
        for _ in range(repeats)
    ]


def single_and_repeated_power_chords(repeats: int):
    single_chord = power_chord()
    fret = single_chord.positions[0].fret + random.randrange(-4, 4)
    fret = max(0, fret)

    return [
        single_chord,
        *repeated_power_chord(repeats, root_fret=fret)
    ]
