from itertools import groupby
from operator import attrgetter
from typing import List

from guitarpractice.models import Sequence, Beat, Note


def to_vextab(exercise: Sequence) -> str:
    """
    http://vexflow.com/vextab/tutorial.html
    """
    elements = ['=|:']

    sorted_notes = sorted(exercise.notes, key=attrgetter('order'))
    note_groups = groupby(sorted_notes, key=attrgetter('order'))
    note_groups = {k: list(v) for k, v in note_groups}

    for group_key in sorted(note_groups.keys()):
        note_group = note_groups[group_key]

        note_el = vextab_note_string(note_group)
        elements.append(note_el)

        if (note_group[0].elapsed_beats + Beat(1, 1)).division == 1:
            elements.append("|")

    if elements[-1] == '|':
        elements[-1] = '=:|'
    else:
        elements.append('=:|')

    element_groups = split_staves(elements)

    staves = []
    for elements in element_groups:
        tab = " ".join(elements)
        tabstave = (
            f'tabstave notation=false\n'
            f'notes {tab}'
        )
        staves.append(tabstave)

    return "\n\n".join(staves)


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
            note_el = f":{duration} {note.position.fret}/{note.position.string}"
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
