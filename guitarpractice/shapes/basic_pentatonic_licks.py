from guitarpractice.models import Note, Beat, FretPosition


def basic_pentatonic_licks():
    return [
        lick_one(),
    ]


def lick_one():
    return [
        Note(duration=Beat(1, 4), elapsed_beats=Beat(1, 4), position=FretPosition(5, 6), order=1),
        Note(duration=Beat(1, 4), elapsed_beats=Beat(1, 4), position=FretPosition(7, 4), order=1),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(1, 4), position=FretPosition(5, 4), order=1),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(1, 4), position=FretPosition(7, 5), order=1),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(1, 4), position=FretPosition(8, 6), order=1),
        Note(duration=Beat(1, 8), elapsed_beats=Beat(1, 4), position=FretPosition(7, 4), order=1),
        Note(duration=Beat(1, 1), elapsed_beats=Beat(1, 4, tie=True), position=FretPosition(7, 4), order=1),
    ]
