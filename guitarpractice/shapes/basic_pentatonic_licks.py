from guitarpractice.models import Note, Beat, FretPosition


def basic_pentatonic_licks():
    return [
        lick_one(),
        lick_two(),
        lick_three(),
        lick_four(),
        lick_five(),
        lick_six(),
        lick_seven(),
        lick_eight(),
        lick_nine(),
        lick_ten(),
    ]


def lick_one():
    return [
        Note(duration=Beat(1, 4), elapsed_beats=Beat(1, 4), position=FretPosition(5, 6), order=0),
        Note(duration=Beat(1, 4), elapsed_beats=Beat(2, 4), position=FretPosition(7, 4), order=1),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(5, 8), position=FretPosition(5, 4), order=2),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(6, 8), position=FretPosition(7, 5), order=3),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(7, 8), position=FretPosition(8, 6), order=4),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(8, 8), position=FretPosition(7, 4), order=5),
        Note(duration=Beat(1, 1, tie=True), elapsed_beats=Beat(2, 1), position=FretPosition(7, 4), order=6),
    ]


def lick_two():
    return [
        Note(duration=Beat(1, 4, rest=True), elapsed_beats=Beat(1, 4), position=None, order=0),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(3, 8), position=FretPosition(5, 4), order=1),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(4, 8), position=FretPosition(7, 5), order=2),
        Note(duration=Beat(1, 4), elapsed_beats=Beat(3, 4), position=FretPosition(5, 4), order=3),
        Note(duration=Beat(1, 4), elapsed_beats=Beat(4, 4), position=FretPosition(7, 4), order=4),
    ]


def lick_three():
    return [
        Note(duration=Beat(1, 8, rest=True), elapsed_beats=Beat(1, 8), position=None, order=0),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(2, 8), position=FretPosition(5, 1), order=1),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(3, 8), position=FretPosition(8, 2), order=2),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(4, 8), position=FretPosition(5, 2), order=3),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(5, 8), position=FretPosition(7, 3), order=4),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(6, 8), position=FretPosition(5, 3), order=5),
        Note(duration=Beat(1, 4), elapsed_beats=Beat(7, 8), position=FretPosition(7, 4), order=6),
    ]


def lick_four():
    return [
        Note(order=0, position=FretPosition(7, 4), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
        Note(order=1, position=FretPosition(5, 4), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
        Note(order=2, position=FretPosition(7, 4), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
        Note(order=3, position=FretPosition(5, 3), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
        Note(order=4, position=FretPosition(7, 4), duration=Beat(2, 4), elapsed_beats=Beat(4, 4)),
    ]


def lick_five():
    return [
        Note(order=0, position=FretPosition(5, 3), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
        Note(order=1, position=FretPosition(7, 3), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
        Note(order=2, position=FretPosition(5, 2), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
        Note(order=3, position=FretPosition(8, 2), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
        Note(order=4, position=FretPosition(5, 1), duration=Beat(1, 8), elapsed_beats=Beat(5, 8)),
        Note(order=5, position=FretPosition(8, 1), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
        Note(order=6, position=FretPosition(5, 1), duration=Beat(1, 4), elapsed_beats=Beat(8, 8)),
    ]


def lick_six():
    return [
        Note(order=0, position=FretPosition(8, 1), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
        Note(order=1, position=FretPosition(5, 1), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
        Note(order=2, position=FretPosition(8, 2), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
        Note(order=3, position=FretPosition(5, 2), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
        Note(order=4, position=FretPosition(8, 1), duration=Beat(1, 8), elapsed_beats=Beat(5, 8)),
        Note(order=5, position=FretPosition(5, 1), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
        Note(order=6, position=FretPosition(8, 2), duration=Beat(1, 8), elapsed_beats=Beat(7, 8)),
        Note(order=7, position=FretPosition(5, 2), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
    ]


def lick_seven():
    return [
        Note(order=0, position=FretPosition(7, 3), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
        Note(order=1, position=FretPosition(5, 3), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
        Note(order=2, position=FretPosition(7, 4), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
        Note(order=3, position=FretPosition(5, 4), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
        Note(order=4, position=FretPosition(7, 4), duration=Beat(2, 4), elapsed_beats=Beat(8, 8)),
    ]


def lick_eight():
    return [
        Note(order=0, position=FretPosition(5, 1), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
        Note(order=1, position=FretPosition(8, 1), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
        Note(order=2, position=FretPosition(5, 1), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
        Note(order=3, position=FretPosition(8, 2), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
        Note(order=4, position=FretPosition(5, 2), duration=Beat(1, 8), elapsed_beats=Beat(5, 8)),
        Note(order=5, position=FretPosition(8, 2), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
        Note(order=6, position=FretPosition(5, 2), duration=Beat(1, 8), elapsed_beats=Beat(7, 8)),
        Note(order=7, position=FretPosition(5, 3), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
    ]


def lick_nine():
    return [
        Note(order=0, position=FretPosition(5, 3), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
        Note(order=1, position=FretPosition(7, 3), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
        Note(order=2, position=FretPosition(5, 3), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
        Note(order=3, position=FretPosition(7, 4), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
        Note(order=4, position=FretPosition(5, 3), duration=Beat(1, 4), elapsed_beats=Beat(3, 4)),
        Note(order=5, position=FretPosition(7, 4), duration=Beat(1, 4), elapsed_beats=Beat(4, 4)),
    ]


def lick_ten():
    return [
        Note(order=0, position=FretPosition(5, 4), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
        Note(order=1, position=FretPosition(7, 4), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
        Note(order=2, position=FretPosition(5, 4), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
        Note(order=3, position=FretPosition(7, 5), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
        Note(order=4, position=FretPosition(5, 5), duration=Beat(1, 8), elapsed_beats=Beat(5, 8)),
        Note(order=5, position=FretPosition(7, 5), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
        Note(order=6, position=FretPosition(5, 5), duration=Beat(1, 8), elapsed_beats=Beat(7, 8)),
        Note(order=7, position=FretPosition(8, 6), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
    ]


def lick_eleven():
    return [
        Note(order=0, position=FretPosition(5, 5), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
        Note(order=1, position=FretPosition(7, 5), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
        Note(order=2, position=FretPosition(5, 4), duration=Beat(1, 4), elapsed_beats=Beat(2, 4)),
        Note(order=3, position=FretPosition(7, 4), duration=Beat(1, 2), elapsed_beats=Beat(4, 4)),
    ]
