from dataclasses import dataclass
from typing import List

from guitarpractice.models import FretPosition

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

tuning_mapping = {
    'standard': [0, 5, 10, 3, 7, 0]
}


@dataclass
class Tuning:
    root: str
    tuning: str


def make_fretboard(tuning: Tuning) -> dict:
    fretboard = {}

    string_intervals = tuning_mapping[tuning.tuning]
    total_strings = len(string_intervals)

    root_index = notes.index(tuning.root)
    note_loop = notes * 3

    for index, string_interval in enumerate(string_intervals):
        string_name = total_strings - index
        open_note_index = root_index + string_interval

        fretboard[string_name] = {}

        for fret in range(13):
            note_index = open_note_index + fret
            note = note_loop[note_index]
            fretboard[string_name][fret] = note

    return fretboard


def get_note(position: FretPosition, tuning: Tuning):
    fretboard = make_fretboard(tuning)
    note_string = position.string
    fret = position.fret

    return fretboard[note_string][fret]


def note_positions(note: str, tuning: Tuning = None) -> List[FretPosition]:
    if tuning is None:
        tuning = Tuning('E', 'standard')

    fretboard = make_fretboard(tuning)
    return [
        FretPosition(fret=fret, string=guitar_string)
        for guitar_string, frets in fretboard.items()
        for fret, fret_note in frets.items()
        if fret_note == note
    ]
