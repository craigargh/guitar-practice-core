import random
from functools import partial

from guitarpractice.annotators import palm_mute_open
from guitarpractice.models import Beat, GuitarShape, FretPosition
from guitarpractice.pickpatterns import fixed_order_pattern, adjust_length
from guitarpractice.sequencer import make_sequence
from guitarpractice.shapes import major_scale_shapes
from guitarpractice.shapes.fixed_order_patterns import level_one_picked_metal_patterns
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
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 2,
            'in_between_beats': 0,
            'notes_per_bit': 4,
            'length': 8,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 2,
            'notes_per_bit': 4,
            'length': 8,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 0.5,
            'notes_per_bit': 1,
            'length': 8,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0.5,
            'in_between_beats': 0.5,
            'notes_per_bit': 1,
            'length': 8,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 1,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 8,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 8,
        },
    ]
    return build_sequence_from_combo(combos)


def level_two():
    combos = [
        {
            'preset_patterns': level_one_picked_metal_patterns(length=8),
            'preceding_beats': 4,
            'in_between_beats': 0,
            'notes_per_bit': 8,
            'length': 16,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=8),
            'preceding_beats': 0,
            'in_between_beats': 0.5,
            'notes_per_bit': 1,
            'length': 16,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=8),
            'preceding_beats': 0.5,
            'in_between_beats': 0.5,
            'notes_per_bit': 1,
            'length': 16,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=8),
            'preceding_beats': 1,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 16,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=8),
            'preceding_beats': 0,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 16,
        },
    ]

    return build_sequence_from_combo(combos)


def level_three():
    reverse_gallop = [Beat(1, 16), Beat(1, 16), Beat(1, 8)]
    gallop = [Beat(1, 8), Beat(1, 16), Beat(1, 16)]
    two_eighths = [Beat(1, 8), Beat(1, 8)]
    sixteenth_notes = [Beat(1, 16), Beat(1, 16), Beat(1, 16), Beat(1, 16)]

    combos = [
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 2,
            'in_between_beats': 0,
            'notes_per_bit': 4,
            'length': 10,
            'rhythm': [*reverse_gallop, *reverse_gallop, *two_eighths, *two_eighths],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 2,
            'notes_per_bit': 4,
            'length': 10,
            'rhythm': [*two_eighths, *two_eighths, *reverse_gallop, *reverse_gallop],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 1,
            'in_between_beats': 1,
            'notes_per_bit': 4,
            'length': 10,
            'rhythm': [*reverse_gallop, *two_eighths, *two_eighths, *reverse_gallop],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 1,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 10,
            'rhythm': [*reverse_gallop, *two_eighths],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 10,
            'rhythm': [*two_eighths, *reverse_gallop],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 2,
            'in_between_beats': 0,
            'notes_per_bit': 4,
            'length': 10,
            'rhythm': [*gallop, *gallop, *two_eighths, *two_eighths],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 2,
            'notes_per_bit': 4,
            'length': 10,
            'rhythm': [*two_eighths, *two_eighths, *gallop, *gallop],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 1,
            'in_between_beats': 1,
            'notes_per_bit': 4,
            'length': 10,
            'rhythm': [*gallop, *two_eighths, *two_eighths, *gallop],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 1,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 10,
            'rhythm': [*gallop, *two_eighths],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 10,
            'rhythm': [*two_eighths, *gallop],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 2,
            'in_between_beats': 0,
            'notes_per_bit': 4,
            'length': 12,
            'rhythm': [*sixteenth_notes, *sixteenth_notes, *two_eighths, *two_eighths],
            'notes_per_chug': 4,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 2,
            'notes_per_bit': 4,
            'length': 12,
            'rhythm': [*two_eighths, *two_eighths, *sixteenth_notes, *sixteenth_notes],
            'notes_per_chug': 4,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 1,
            'in_between_beats': 1,
            'notes_per_bit': 4,
            'length': 12,
            'rhythm': [*sixteenth_notes, *two_eighths, *two_eighths, *sixteenth_notes],
            'notes_per_chug': 4,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 1,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 12,
            'rhythm': [*sixteenth_notes, *two_eighths],
            'notes_per_chug': 4,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 1,
            'notes_per_bit': 2,
            'length': 12,
            'rhythm': [*two_eighths, *sixteenth_notes],
            'notes_per_chug': 4,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 3,
            'notes_per_bit': 2,
            'length': 28,
            'rhythm': [*two_eighths, *sixteenth_notes, *sixteenth_notes, *sixteenth_notes],
            'notes_per_chug': 4,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 3,
            'in_between_beats': 3,
            'notes_per_bit': 2,
            'length': 28,
            'rhythm': [*sixteenth_notes, *sixteenth_notes, *sixteenth_notes, *two_eighths],
            'notes_per_chug': 4,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 3,
            'notes_per_bit': 2,
            'length': 22,
            'rhythm': [*two_eighths, *reverse_gallop, *reverse_gallop, *reverse_gallop],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 3,
            'in_between_beats': 3,
            'notes_per_bit': 2,
            'length': 22,
            'rhythm': [*reverse_gallop, *reverse_gallop, *reverse_gallop, *two_eighths],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 0,
            'in_between_beats': 3,
            'notes_per_bit': 2,
            'length': 22,
            'rhythm': [*two_eighths, *reverse_gallop, *reverse_gallop, *reverse_gallop],
            'notes_per_chug': 3,
        },
        {
            'preset_patterns': level_one_picked_metal_patterns(length=4),
            'preceding_beats': 3,
            'in_between_beats': 3,
            'notes_per_bit': 2,
            'length': 22,
            'rhythm': [*gallop, *gallop, *gallop, *two_eighths],
            'notes_per_chug': 3,
        },
    ]

    return build_sequence_from_combo(combos)


def build_sequence_from_combo(combos):
    shape_choices = [
        major_scale_shapes.c_ionian(),
        major_scale_shapes.a_aeolian(),
    ]
    shape = random.choice(shape_choices)

    combo = random.choice(combos)

    preset_pattern = random.choice(combo['preset_patterns'])
    pick_pattern = partial(fixed_order_pattern, pattern=preset_pattern)

    chug_pattern = partial(
        chug,
        length=combo['length'],
        order=pick_pattern,
        preceding_beats=combo['preceding_beats'],
        in_between_beats=combo['in_between_beats'],
        notes_per_bit=combo['notes_per_bit'],
        notes_per_chug=combo.get('notes_per_chug', 2),
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


def chug(shape: GuitarShape, length: int = None, order: callable = None, preceding_beats=0, in_between_beats=0,
         notes_per_bit=1, notes_per_chug=2):
    pick_pattern = order(shape)
    chug_position = [FretPosition(fret=0, string=6)]

    if in_between_beats > 0:
        new_pattern = []

        note_count = 0
        for item in pick_pattern:
            new_pattern.append(item)
            note_count += 1

            if note_count == notes_per_bit:
                new_pattern.extend([chug_position] * int(notes_per_chug * in_between_beats))
                note_count = 0

        pick_pattern = new_pattern

    if preceding_beats > 0:
        pick_pattern = ([chug_position] * int(preceding_beats * notes_per_chug)) + pick_pattern

    pick_pattern = adjust_length(pick_pattern, length=length)
    return pick_pattern
