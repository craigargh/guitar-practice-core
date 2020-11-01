from typing import List

from guitarpractice.models import Sequence, Beat, Note
from guitarpractice.note_utils import group_notes, normalise_note_durations


def to_vextab(exercise: Sequence) -> str:
    """
    http://vexflow.com/vextab/tutorial.html
    """
    split = normalise_note_durations(exercise.notes)

    elements = make_elements(split)
    element_groups = split_staves(elements)

    staves = []
    for element_group in element_groups:
        tab = " ".join(element_group)
        tabstave = (
            f'tabstave notation=false\n'
            f'notes {tab}'
        )
        staves.append(tabstave)

    return "\n\n".join(staves)


def make_elements(notes):
    elements = ['=|:']
    note_groups = group_notes(notes)

    for group_key in sorted(note_groups.keys()):
        note_group = note_groups[group_key]

        note_el = vextab_note_string(note_group)
        elements.append(note_el)

        if note_group[0].elapsed_beats.is_new_bar():
            elements.append("|")

    if elements[-1] == '|':
        elements[-1] = '=:|'
    else:
        elements.append('=:|')

    return elements


def vextab_duration(note: Note) -> str:
    duration = int(note.duration.division / note.duration.duration)
    if duration < 8:
        duration_map = {
            1: 'w',
            2: 'h',
            4: 'q'
        }
        duration = duration_map[duration]

    return duration


def vextab_note_string(notes: List[Note]) -> str:
    duration = vextab_duration(notes[0])

    if len(notes) == 1:
        note = notes[0]

        if note.duration.rest:
            note_el = f':{duration} ##'
        else:
            duration_string = f':{duration}'
            if 'tie' in note.annotations:
                duration_string = f'T:{duration}:'

            note_el = f"{duration_string} {note.position.fret}/{note.position.string}"
    else:
        chord = [
            f'{note.position.fret}/{note.position.string}'
            for note in notes
        ]
        chord_join = ".".join(chord)
        note_el = f":{duration} ({chord_join})"

    return note_el


def split_staves(elements: List[str]) -> List[List[str]]:
    groups = [[]]
    bar_count = 0
    groups_count = 0

    for element in elements:
        if element == '|':
            bar_count += 1

        groups[groups_count].append(element)

        if bar_count == 2:
            groups.append([])
            groups_count += 1
            bar_count = 0

    return groups
