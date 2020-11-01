from itertools import groupby
from operator import attrgetter
from typing import List, Dict

from guitarpractice.models import Note, Beat


def group_notes(notes) -> Dict[str, List[Note]]:
    sorted_notes = sorted(notes, key=attrgetter('order'))
    note_groups = groupby(sorted_notes, key=attrgetter('order'))
    return {k: list(v) for k, v in note_groups}


def normalise_note_durations(notes: List[Note]) -> List[Note]:
    notes = sorted(notes, key=attrgetter('order'))

    elapsed_beats = Beat(0, 0)
    count = 0

    normalised_notes = []

    for note in notes:
        first_note = True
        normalised_durations = note.duration.tie_split()

        for duration in normalised_durations:
            elapsed_beats += duration

            new_note = Note(position=note.position, duration=duration, elapsed_beats=elapsed_beats, order=count)
            if not first_note and not note.duration.rest:
                new_note.annotations.append('tie')

            normalised_notes.append(new_note)
            first_note = False

            count += 1

    return normalised_notes
