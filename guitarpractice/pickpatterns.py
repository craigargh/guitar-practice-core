import math
import random
from functools import partial
from itertools import cycle
from typing import List, Callable, Tuple

from guitarpractice.models import GuitarShape, FretPosition


def strum(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    validate_length(length)

    repeats = 1 if length is None else length
    return [shape.positions] * repeats


chug = strum


def asc(shape: GuitarShape, length: int = None, shorten_from_end=False) -> List[List[FretPosition]]:
    positions = sorted(shape.positions)
    positions = adjust_length(positions, length, shorten_from_end)

    pattern = [
        [position]
        for position in positions
    ]

    return pattern


def desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    positions = sorted(shape.positions, reverse=True)
    positions = adjust_length(positions, length)

    pattern = [
        [position]
        for position in positions
    ]
    return pattern


def asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    shape_asc_and_desc_length = (len(shape.positions) - 1) * 2
    positions_can_repeat_fully_twice = length and shape_asc_and_desc_length == length / 2

    if positions_can_repeat_fully_twice:
        pattern = sequential_patterns(shape, asc, desc, length=int(length / 2))
        return adjust_length(pattern, length)

    return sequential_patterns(shape, asc, desc, length=length)


def asc_and_desc_top_strings(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    asc_func = partial(asc, shorten_from_end=True)
    return sequential_patterns(shape, asc_func, desc, length=length, cut_pattern_2_top_note=True)


# Do not work correctly
#
# def bass_and_asc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
#     asc_func = partial(asc, shorten_from_end=True)
#     return bass_and_pattern(shape, length, asc_func)
#
#
# def bass_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
#     return bass_and_pattern(shape, length, desc)
#
#
# def bass_asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
#     return bass_and_pattern(shape, length, asc_and_desc_top_strings)
#
#
# def bass_and_pattern(shape: GuitarShape, length: int, pick_pattern: Callable) -> List[List[FretPosition]]:
#     bass_position, split_shape = split_bass_position(shape)
#
#     if length == 1:
#         return [[bass_position]]
#
#     if length is not None:
#         length -= 1
#
#     pattern = pick_pattern(split_shape, length=length)
#
#     return [[bass_position]] + pattern


def bass_and_strum(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    bass_position, _ = split_bass_position(shape)
    if length == 1:
        return [[bass_position]]

    if length is not None:
        length -= 1

    strum_pattern = strum(shape, length=length)

    return [[bass_position]] + strum_pattern


def alternating_bass_and_asc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return alternating_bass_and_pattern(shape, length, asc)


def alternating_bass_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return alternating_bass_and_pattern(shape, length, desc)


def alternating_bass_asc_and_desc(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return alternating_bass_and_pattern(shape, length, asc_and_desc)


def alternating_bass_asc_and_desc_top_strings(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    return alternating_bass_and_pattern(shape, length, asc_and_desc_top_strings)


def alternating_bass_and_pattern(shape: GuitarShape, length: int, pick_pattern: Callable) -> List[List[FretPosition]]:
    bass_position, split_shape = split_bass_position(shape)

    if length == 1:
        return [[bass_position]]

    if length is not None:
        half_length = length // 2
    else:
        half_length = None

    ordered_pattern = pick_pattern(split_shape, length=half_length)

    pattern = []
    for item in ordered_pattern:
        pattern.append([bass_position])
        pattern.append(item)

    if length is not None and length % 2 != 0:
        pattern.append([bass_position])

    return pattern


def stepped_asc(shape: GuitarShape, step: int = 2, length: int = None) -> List[List[FretPosition]]:
    return stepped_pattern(shape, step, length, asc)


def stepped_desc(shape: GuitarShape, step: int = 2, length: int = None) -> List[List[FretPosition]]:
    return stepped_pattern(shape, step, length, desc)


def stepped_pattern(shape: GuitarShape, step: int, length: int, pick_pattern: Callable) -> List[List[FretPosition]]:
    positions = pick_pattern(shape)

    pattern = []
    for index in range(len(positions) - step):
        position_1 = positions[index]
        position_2 = positions[index + step]
        pattern.append(position_1)
        pattern.append(position_2)

    pattern = adjust_length(pattern, length=length)

    return pattern


def randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    positions = sorted(shape.positions)
    random.shuffle(positions)

    positions = adjust_length(positions, length=length)

    pattern = [
        [position]
        for position in positions
    ]

    return pattern


def bass_and_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def alternating_bass_and_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def each_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def bass_and_each_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def alternating_bass_and_each_randomly(shape: GuitarShape, length: int = None) -> List[List[FretPosition]]:
    pass


def fixed_string_pattern(shape: GuitarShape, length: int = None, pattern: List[str] = None) -> List[List[FretPosition]]:
    if pattern is None:
        raise ValueError('pattern must be set')

    positions = sorted(shape.positions)

    required_strings = [
        string
        for string in pattern
        if string != 'r'
    ]

    string_map = {
        'r': positions[0],
        'a': positions[1],
    }

    for string in required_strings:
        for position in positions:
            if str(position.string) == string:
                string_map[string] = position

    pick_pattern = [
        [string_map.get(string, positions[0])]
        for string in pattern
    ]

    pick_pattern = adjust_length(pick_pattern, length=length)
    return pick_pattern


def fixed_order_pattern(shape: GuitarShape, length: int = None, pattern: List[str] = None) -> List[List[FretPosition]]:
    if pattern is None:
        raise ValueError('pattern must be set')

    positions = sorted(shape.positions)
    default_position = positions[-1]

    pick_pattern = [
        [positions[location - 1] if location <= len(positions) else default_position]
        for location in pattern
    ]

    pick_pattern = adjust_length(pick_pattern, length=length)
    return pick_pattern


def fixed_chug_pattern(shape: GuitarShape, length: int = None, pattern: List[str] = None,
                       note_order: Callable = None) -> List[List[FretPosition]]:
    if note_order is None:
        raise ValueError('note_order must be set')

    if pattern is None:
        raise ValueError('pattern must be set')

    if length is None:
        length = len(pattern)

    notes_pick_pattern = cycle(note_order(shape))
    pattern_cycle = cycle(pattern)

    pick_pattern = []

    while len(pick_pattern) < length:
        item = next(pattern_cycle)
        if item == 'c':
            pick_pattern.append([FretPosition(string=6, fret=0)])

        elif item == 'n':
            pick_pattern.append(next(notes_pick_pattern))

    return pick_pattern


def repeat_each_position(shape: GuitarShape, length: int = None, repeats: int = 2, order: Callable = asc) -> List[
    List[FretPosition]]:
    """
    Play each fret in the sequence two or more times
    """
    if length is not None:
        div_length = math.ceil(length / repeats)
    else:
        div_length = length

    pattern = order(shape, length=div_length)

    new_positions = []
    for positions in pattern:
        new_positions.extend([positions] * repeats)

    if length is not None and len(new_positions) != length:
        new_positions = adjust_length(new_positions, length)

    return new_positions


def repeat_whole_pattern(shape: GuitarShape, length: int = None, repeats: int = 2, order: Callable = asc) -> List[
    List[FretPosition]]:
    if length:
        adjusted_length = math.ceil(length / repeats)
    else:
        adjusted_length = None

    pattern = order(shape, length=adjusted_length)
    pattern = pattern * repeats

    adjust_length(pattern, length=length)

    return pattern


def split_bass_position(shape: GuitarShape) -> Tuple[FretPosition, GuitarShape]:
    positions = sorted(shape.positions)
    bass_note = positions.pop(0)

    split_shape = GuitarShape(positions=positions, name=None, category=None)
    return bass_note, split_shape


def sequential_patterns(shape: GuitarShape, pick_pattern_1: Callable, pick_pattern_2: Callable, length: int = None,
                        cut_pattern_2_top_note: bool = False) -> List[List[FretPosition]]:
    """
    Sequences multiple pick patterns to be applied to the same shape sequentially.
    For example strum a chord shape and then pick it as an arpeggio.
    """
    if length == 1:
        return pick_pattern_1(shape, length=1)

    if cut_pattern_2_top_note and length is not None and length % 2 != 0:
        shape_2 = GuitarShape(category=None, name=None, positions=shape.positions[:-1])
    else:
        shape_2 = shape

    pattern_1_length, pattern_2_length = calculate_divided_pattern_length(length, len(shape.positions))

    both_patterns = pick_pattern_1(shape, length=pattern_1_length) + pick_pattern_2(shape_2, length=pattern_2_length)

    return adjust_length(both_patterns, length)


def calculate_divided_pattern_length(total_length, positions_length):
    if total_length is not None:
        half_length = math.ceil(total_length / 2)
    else:
        half_length = total_length

    pattern_1_length = half_length
    pattern_2_length = half_length

    is_odd_length = total_length is not None and total_length % 2 != 0
    pattern_completes_once_fully = half_length is not None and positions_length % half_length == 0

    if is_odd_length and pattern_completes_once_fully:
        pattern_1_length -= 1
    elif is_odd_length and not pattern_completes_once_fully:
        pattern_2_length -= 1

    return pattern_1_length, pattern_2_length


def alternate_patterns(pick_patterns: List[Callable], strip_end_positions=False) -> List[List[FretPosition]]:
    """
    Sequences multiple pick patterns to be applied to shapes alternatively.
    For example strum the first shape, then pick the second shape.
    """
    pass


def validate_length(length: int):
    if length is not None and length < 1:
        raise ValueError(f'Length of {length} is not allowed. Must be greater than 0.')


def adjust_length(positions: List, length: int, shorten_from_end=False) -> List:
    validate_length(length)

    if length is not None and len(positions) > length:
        positions = shorten(positions, length, shorten_from_end)

    elif length is not None and len(positions) < length:
        positions = lengthen(positions, length)

    return positions


def shorten(positions, length, shorten_from_end):
    if shorten_from_end:
        return positions[length - 1:]
    else:
        return positions[:length]


def lengthen(positions, length):
    if length is None:
        return positions

    number_of_full_repeats = length // len(positions)
    partial_repeat_positions = length % len(positions)

    positions *= number_of_full_repeats
    if partial_repeat_positions != 0:
        extra_positions = positions[-partial_repeat_positions:]
        positions.extend(extra_positions)

    return positions
