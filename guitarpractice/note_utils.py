from copy import deepcopy
from itertools import groupby
from operator import attrgetter
from typing import List, Dict

from guitarpractice import constants
from guitarpractice.models import Note, Beat


def group_notes(notes) -> Dict[str, List[Note]]:
    sorted_notes = sorted(notes, key=attrgetter('order'))
    note_groups = groupby(sorted_notes, key=attrgetter('order'))
    return {k: list(v) for k, v in note_groups}


def normalise_note_durations(notes: List[Note]) -> List[Note]:
    changes_to_apply = calculate_normalised_beats_per_chord(notes)
    return apply_new_chord_rhythms(changes_to_apply)


def calculate_normalised_beats_per_chord(notes):
    chords = group_notes(notes)
    groups_with_new_beats = {}

    for chord_index in sorted(chords.keys()):
        chord = chords[chord_index]

        new_rhythm = chord[0].duration.tie_split()

        groups_with_new_beats[chord_index] = {
            'original_notes': chord,
            'new_rhythm': new_rhythm,
        }

    return groups_with_new_beats


def apply_new_chord_rhythms(normalised_beats_per_chord):
    all_notes = []

    elapsed_beats = Beat(0, 1)
    count = 0

    for chord_index in sorted(normalised_beats_per_chord.keys()):
        chord = normalised_beats_per_chord[chord_index]['original_notes']
        new_rhythm = normalised_beats_per_chord[chord_index]['new_rhythm']

        if not elapsed_beats.is_new_bar():
            new_rhythm.reverse()

        first_beat_in_tie = True
        for beat in new_rhythm:
            elapsed_beats += beat

            for note in chord:
                new_note = Note(
                    position=note.position,
                    duration=beat,
                    elapsed_beats=elapsed_beats,
                    order=count,
                    annotations=deepcopy(note.annotations),
                )

                if first_beat_in_tie:
                    new_note.slur = note.slur

                if not first_beat_in_tie and not beat.rest:
                    new_note.duration.tie = True

                all_notes.append(new_note)

            first_beat_in_tie = False
            count += 1

    return all_notes
