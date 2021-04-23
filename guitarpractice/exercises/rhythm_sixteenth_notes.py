import random
from functools import partial

from guitarpractice import pickpatterns
from guitarpractice.models import Sequence, FretPosition, GuitarShape, Beat
from guitarpractice.pickpatterns import repeat_each_position, fixed_order_pattern
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes.fixed_order_patterns import sixteenth_note_patterns
from guitarpractice.shapes.scale_collections import c_major_modes, c_major_pentatonic_modes


def rhythm_sixteenth_notes(variation: str) -> Sequence:
    variation_map = {
        'level-1': level_one,
        'level-2': level_two,
        'level-3': level_three,
    }
    variation_function = variation_map[variation]

    return variation_function()


def level_one() -> Sequence:
    shape = generate_single_string_shape(1)
    repeater = partial(repeat_each_position, repeats=16)

    rhythm = [Beat(duration=1, division=16)]

    return make_sequence(
        shapes=[shape],
        rhythm=rhythm,
        pick_pattern=repeater,
    )


def level_two() -> Sequence:
    combos = [
        {
            'shapes': [generate_single_string_shape(4)],
            'pick_pattern': partial(
                repeat_each_position,
                repeats=16,
                order=random.choice([pickpatterns.asc, pickpatterns.desc, pickpatterns.randomly])
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
        {
            'shapes': [generate_single_string_shape(2)],
            'pick_pattern': partial(
                repeat_each_position,
                repeats=8,
                order=random.choice([pickpatterns.asc, pickpatterns.desc, pickpatterns.randomly])
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
        {
            'shapes': [positions_on_adjacent_strings()],
            'pick_pattern': partial(
                repeat_each_position,
                repeats=16,
                order=random.choice([pickpatterns.asc, pickpatterns.desc, pickpatterns.randomly])
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
    ]
    combo = random.choice(combos)

    return make_sequence(**combo)


def level_three() -> Sequence:
    combos = [
        {
            'shapes': [random.choice(c_major_modes())],
            'pick_pattern': partial(
                repeat_each_position,
                repeats=4,
                order=random.choice([pickpatterns.asc, pickpatterns.desc, pickpatterns.asc_and_desc])
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
        {
            'shapes': [random.choice(c_major_pentatonic_modes())],
            'pick_pattern': partial(
                repeat_each_position,
                repeats=4,
                order=random.choice([pickpatterns.asc, pickpatterns.desc, pickpatterns.asc_and_desc])
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
        {
            'shapes': [single_string_chromatic_pattern()],
            'pick_pattern': partial(
                repeat_each_position,
                repeats=4,
                order=random.choice([pickpatterns.asc, pickpatterns.desc, pickpatterns.randomly])
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
        {
            'shapes': [single_string_chromatic_pattern()],
            'pick_pattern': partial(
                repeat_each_position,
                repeats=2,
                length=16,
                order=pickpatterns.alternating_bass_asc_and_desc
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
        {
            'shapes': [generate_single_string_shape(2)],
            'pick_pattern': partial(
                fixed_order_pattern,
                pattern=random.choice(sixteenth_note_patterns())
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
        {
            'shapes': [positions_on_adjacent_strings()],
            'pick_pattern': partial(
                fixed_order_pattern,
                pattern=random.choice(sixteenth_note_patterns())
            ),
            'rhythm': [Beat(duration=1, division=16)],
        },
    ]
    combo = random.choice(combos)

    return make_sequence(**combo)


def generate_single_string_shape(positions_len: int) -> GuitarShape:
    positions = []
    string_choice = random.choice([6, 6, 6, 5, 5, 4, 3, 2, 1])

    lowest_fret = random.choice(list(range(0, 8)))
    fret_options = [0] + list(range(lowest_fret, lowest_fret + 5))
    random.shuffle(fret_options)

    for _ in range(positions_len):
        fret_choice = fret_options.pop()
        positions.append(FretPosition(fret=fret_choice, string=string_choice))

    shape = GuitarShape('Notes on a single string', 'scale', positions=positions)
    return shape


def positions_on_adjacent_strings():
    base_string = random.randrange(1, 6)
    other_string = base_string + 1

    base_fret = random.randrange(0, 8)
    other_fret = max(0, base_fret + random.randrange(-3, 3))

    positions = [
        FretPosition(string=base_string, fret=base_fret),
        FretPosition(string=other_string, fret=other_fret),
    ]

    return GuitarShape('Two notes on adjacent strings', 'scale', positions=positions)


def single_string_chromatic_pattern():
    base_string = random.randrange(1, 7)
    base_fret = random.randrange(0, 8)

    positions = [
        FretPosition(string=base_string, fret=fret)
        for fret in range(base_fret, base_fret + 4)
    ]

    return GuitarShape('Chromatic shape', 'scale', positions=positions)

"""
Exercise Ideas

Level 2:
- Play a whole bar of 16th notes before switching to another note on the same string, repeat for 4 bars/notes
- Play two notes in a bar of 16th notes, switching every 2 beats
- Play two notes on adjacent strings, switching every bar


Level 3:
- Ascend and/or descend a scale or arpeggio, picking each note 4 times
- Pick a four note chromatic pattern on a single string, repeating each note 4 times
- Alternate between base note and positions in a chromatic pattern, repeating each note twice

Level 4:
- Ascend and/or descend a scale or arpeggio, picking each note twice
- Pick a four note chromatic pattern on a single string, repeating each note twice
- Alternate between base note and positions in a chromatic pattern, repeating each note once

Level 5:
- Ascend and/or descend a scale or arpeggio, picking each note once
- Pick a four note chromatic pattern on a single string, repeating each note once
"""
