import random
from functools import partial

from guitarpractice.annotators import palm_mute_open
from guitarpractice.models import Beat
from guitarpractice.pickpatterns import fixed_order_pattern, fixed_chug_pattern
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes import major_scale_shapes, chromatic_shapes, single_string_scales
from guitarpractice.shapes.fixed_order_patterns import picked_metal_patterns
from guitarpractice.shapeshifters import shift_vertically


def metal_picked_riffs(variation=None):
    variation_map = {
        'level-1': level_one,
        'level-2': level_two,
        'level-3': level_three,
    }
    variation_function = variation_map[variation]

    return variation_function()


def level_one():
    combos = [
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 8,
            'chug_pattern': ['c', 'c', 'c', 'c', 'n', 'n', 'n', 'n']
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 8,
            'chug_pattern': ['n', 'n', 'n', 'n', 'c', 'c', 'c', 'c']
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 8,
            'chug_pattern': ['n', 'c']
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 8,
            'chug_pattern': ['c', 'n']
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 8,
            'chug_pattern': ['n', 'n', 'c', 'c']
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 8,
            'chug_pattern': ['c', 'c', 'n', 'n']
        },
    ]
    return build_sequence_from_combo(combos)


def level_two():
    combos = [
        {
            'preset_patterns': picked_metal_patterns(length=8),
            'length': 16,
            'chug_pattern': ['c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'],
        },
        {
            'preset_patterns': picked_metal_patterns(length=8),
            'length': 16,
            'chug_pattern': ['c', 'c', 'c', 'c', 'n', 'n', 'n', 'n'],
        },
        {
            'preset_patterns': picked_metal_patterns(length=8),
            'length': 16,
            'chug_pattern': ['n', 'n', 'n', 'n', 'c', 'c', 'c', 'c'],
        },
        {
            'preset_patterns': picked_metal_patterns(length=8),
            'length': 16,
            'chug_pattern': ['n', 'n', 'n', 'n', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'n', 'n', 'n', 'n'],
        },
        {
            'preset_patterns': picked_metal_patterns(length=8),
            'length': 16,
            'chug_pattern': ['n', 'c'],
        },
        {
            'preset_patterns': picked_metal_patterns(length=8),
            'length': 16,
            'chug_pattern': ['c', 'n'],
        },
        {
            'preset_patterns': picked_metal_patterns(length=8),
            'length': 16,
            'chug_pattern': ['c', 'c', 'n', 'n'],
        },
        {
            'preset_patterns': picked_metal_patterns(length=8),
            'length': 16,
            'chug_pattern': ['n', 'n', 'c', 'c'],
        },
    ]

    return build_sequence_from_combo(combos)


def level_three():
    reverse_gallop = [Beat(1, 16), Beat(1, 16), Beat(1, 8)]
    gallop = [Beat(1, 8), Beat(1, 16), Beat(1, 16)]
    two_eighths = [Beat(1, 8), Beat(1, 8)]
    sixteenth_notes = [Beat(1, 16), Beat(1, 16), Beat(1, 16), Beat(1, 16)]

    gallop_chug = ['c', 'c', 'c']
    sixteenth_chug = ['c', 'c', 'c', 'c']
    two_notes = ['n', 'n']

    combos = [
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'rhythm': [*reverse_gallop, *reverse_gallop, *two_eighths, *two_eighths],
            'chug_pattern': [*gallop_chug, *gallop_chug, *two_notes, *two_notes],
            'length': 10,
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'rhythm': [*two_eighths, *two_eighths, *reverse_gallop, *reverse_gallop],
            'chug_pattern': [*two_notes, *two_notes, *gallop_chug, *gallop_chug],
            'length': 10,
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 10,
            'rhythm': [*reverse_gallop, *two_eighths, *two_eighths, *reverse_gallop],
            'chug_pattern': [*gallop_chug, *two_notes, *two_notes, *gallop_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 10,
            'rhythm': [*reverse_gallop, *two_eighths],
            'chug_pattern': [*gallop_chug, *two_notes],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 10,
            'rhythm': [*two_eighths, *reverse_gallop],
            'chug_pattern': [*two_notes, *gallop_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 10,
            'rhythm': [*gallop, *gallop, *two_eighths, *two_eighths],
            'chug_pattern': [*gallop_chug, *gallop_chug, *two_notes, *two_notes],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 10,
            'rhythm': [*two_eighths, *two_eighths, *gallop, *gallop],
            'chug_pattern': [*two_notes, *two_notes, *gallop_chug, *gallop_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 10,
            'rhythm': [*gallop, *two_eighths, *two_eighths, *gallop],
            'chug_pattern': [*gallop_chug, *two_notes, *two_notes, *gallop_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 10,
            'rhythm': [*gallop, *two_eighths],
            'chug_pattern': [*gallop_chug, *two_notes],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 10,
            'rhythm': [*two_eighths, *gallop],
            'chug_pattern': [*two_notes, *gallop_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 12,
            'rhythm': [*sixteenth_notes, *sixteenth_notes, *two_eighths, *two_eighths],
            'chug_pattern': [*sixteenth_chug, *sixteenth_chug, *two_notes, *two_notes],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 12,
            'rhythm': [*two_eighths, *two_eighths, *sixteenth_notes, *sixteenth_notes],
            'chug_pattern': [*two_notes, *two_notes, *sixteenth_chug, *sixteenth_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 12,
            'rhythm': [*sixteenth_notes, *two_eighths, *two_eighths, *sixteenth_notes],
            'chug_pattern': [*sixteenth_chug, *two_notes, *two_notes, *sixteenth_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 12,
            'rhythm': [*sixteenth_notes, *two_eighths],
            'chug_pattern': [*sixteenth_chug, *two_notes],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 12,
            'rhythm': [*two_eighths, *sixteenth_notes],
            'chug_pattern': [*two_notes, *sixteenth_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 28,
            'rhythm': [*two_eighths, *sixteenth_notes, *sixteenth_notes, *sixteenth_notes],
            'chug_pattern': [*two_notes, *sixteenth_chug, *sixteenth_chug, *sixteenth_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 28,
            'rhythm': [*sixteenth_notes, *sixteenth_notes, *sixteenth_notes, *two_eighths],
            'chug_pattern': [*sixteenth_chug, *sixteenth_chug, *sixteenth_chug, *two_notes],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 22,
            'rhythm': [*two_eighths, *reverse_gallop, *reverse_gallop, *reverse_gallop],
            'chug_pattern': [*two_notes, *gallop_chug, *gallop_chug, *gallop_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 22,
            'rhythm': [*reverse_gallop, *reverse_gallop, *reverse_gallop, *two_eighths],
            'chug_pattern': [*gallop_chug, *gallop_chug, *gallop_chug, *two_notes],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 22,
            'rhythm': [*two_eighths, *reverse_gallop, *reverse_gallop, *reverse_gallop],
            'chug_pattern': [*two_notes, *gallop_chug, *gallop_chug, *gallop_chug],
        },
        {
            'preset_patterns': picked_metal_patterns(length=4),
            'length': 22,
            'rhythm': [*gallop, *gallop, *gallop, *two_eighths],
            'chug_pattern': [*gallop_chug, *gallop_chug, *gallop_chug, *two_notes],
        },
    ]

    return build_sequence_from_combo(combos)


def build_sequence_from_combo(combos):
    shape_choices = [
        major_scale_shapes.c_ionian(),
        major_scale_shapes.a_aeolian(),
        chromatic_shapes.chromatic_4_notes_per_string(),
        chromatic_shapes.chromatic_5_notes_per_string(),
        single_string_scales.chromatic_string_6(),
        single_string_scales.major_pentatonic_string_6(),
        single_string_scales.major_string_6(),
        single_string_scales.mixolydian_string_6(),
        single_string_scales.lydian_string_6(),
        single_string_scales.phrygian_dominant_string_6(),
        single_string_scales.minor_pentatonic_string_6(),
        single_string_scales.minor_blues_string_6(),
        single_string_scales.natural_minor_string_6(),
        single_string_scales.harmonic_minor_string_6(),
        single_string_scales.melodic_minor_string_6(),
        single_string_scales.dorian_string_6(),
        single_string_scales.chromatic_string_5(),
        single_string_scales.major_pentatonic_string_5(),
        single_string_scales.major_string_5(),
        single_string_scales.mixolydian_string_5(),
        single_string_scales.lydian_string_5(),
        single_string_scales.phrygian_dominant_string_5(),
        single_string_scales.minor_pentatonic_string_5(),
        single_string_scales.minor_blues_string_5(),
        single_string_scales.natural_minor_string_5(),
        single_string_scales.harmonic_minor_string_5(),
        single_string_scales.melodic_minor_string_5(),
        single_string_scales.dorian_string_5(),
    ]
    shape = random.choice(shape_choices)

    combo = random.choice(combos)

    preset_pattern = random.choice(combo['preset_patterns'])
    pick_pattern = partial(fixed_order_pattern, pattern=preset_pattern)

    chug_pattern = partial(
        fixed_chug_pattern,
        length=combo['length'],
        note_order=pick_pattern,
        pattern=combo['chug_pattern']
    )

    if combo.get('rhythm'):
        rhythm = combo.get('rhythm')
    else:
        rhythm = [Beat(1, 8)]

    shape_shifter = partial(shift_vertically, lowest_fret=random.randrange(1, 7))

    return make_sequence(
        [shape],
        pick_pattern=chug_pattern,
        rhythm=rhythm,
        annotators=[palm_mute_open],
        shape_shifters=[shape_shifter],
    )
