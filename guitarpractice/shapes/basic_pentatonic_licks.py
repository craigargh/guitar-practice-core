from guitarpractice.models import Note, Beat, FretPosition


def basic_pentatonic_licks():
    return [
        lick_one(),
        lick_two(),
        lick_three(),
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
