from guitarpractice.models import Note, Beat, FretPosition


def basic_pentatonic_licks():
    return [
        lick_one(),
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
