from typing import List

from guitarpractice import constants
from guitarpractice.models import Sequence, Note
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

        show_notation = 'false'
        if '^3^' in tab:
            show_notation = 'true'

        tabstave = (
            f'tabstave notation={show_notation}\n'
            f'notes {tab}'
        )
        staves.append(tabstave)

    return "\n\n".join(staves)


def make_elements(notes):
    elements = ['=|:']
    note_groups = group_notes(notes)

    triplet_count = 0

    for group_key in sorted(note_groups.keys()):
        note_group = note_groups[group_key]

        note_el = vextab_note_string(note_group)
        elements.append(note_el)

        if note_group[0].duration.division % 3 == 0:
            triplet_count += 1

            if triplet_count == 3:
                triplet_count = 0
                elements.append('^3^')

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
            3: 'h',
            4: 'q',
            6: 'q',
        }
        duration = duration_map[duration]

    elif duration % 3 == 0:
        triplet_duration_map = {
            12: 8,
            24: 16,
            48: 32,
        }
        duration = triplet_duration_map[duration]

    return duration


def vextab_note_string(notes: List[Note]) -> str:
    if len(notes) == 1:
        note_el = format_note_element(notes[0])
    else:
        note_el = format_chord_elements(notes)

    return note_el


def format_note_element(note: Note) -> str:
    duration = vextab_duration(note)

    if note.duration.rest:
        note_el = f':{duration} ##'
    else:
        duration_string = f':{duration}'
        if note.duration.tie or note.slur:
            duration_string = f'{slur_map(note)}:{duration}:'

        annotation_string = ''
        if note.annotations:
            annotation_string = format_annotations(note.annotations)

        note_el = f"{duration_string} {note.position.fret}/{note.position.string}{annotation_string}"

    return note_el


def format_chord_elements(notes: List[Note]) -> str:
    duration = vextab_duration(notes[0])

    chord = [
        f'{note.position.fret}/{note.position.string}'
        for note in notes
    ]
    chord_join = ".".join(chord)

    if notes[0].slur or notes[0].duration.tie:
        tie_element = slur_map(notes[0])
    else:
        tie_element = ""

    annotation_element = ""
    if annotations := set(annotation for note in notes for annotation in note.annotations):
        annotation_element = format_annotations(sorted(annotations))

    return f":{duration} {tie_element}({chord_join}){annotation_element}"


def slur_map(note: Note) -> str:
    if note.duration.tie:
        return 'T'

    tie_mapping = {
        constants.HAMMER_ON: 'h',
        constants.PULL_OFF: 'p',
        constants.SLIDE: 's',
        constants.BEND: 'b',
        constants.TAP: 't',
    }
    return tie_mapping.get(note.slur)


def format_annotations(annotations: List[str]) -> str:
    annotation_map = {
        constants.PALM_MUTE: '.top.pm',
        constants.UP_PICK: '.a|/top.',
        constants.DOWN_PICK: '.am/top.',
    }
    annotation_list = [
        f' ${annotation_map[annotation]}$'
        for annotation in annotations
        if 'label:' not in annotation
    ]

    for annotation in annotations:
        if 'label:' in annotation:
            label = annotation.replace('label:', '')
            annotation_list.append(f' $.top.{label}$')

    annotation_string = "".join(annotation_list)

    return annotation_string


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
