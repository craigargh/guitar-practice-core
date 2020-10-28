from guitarpractice.models import Sequence, Beat, Note


def to_vextab(exercise: Sequence) -> str:
    """
    http://vexflow.com/vextab/tutorial.html
    """
    elements = ['=|:']
    for note in exercise.notes:
        note_el = vextab_note_string(note)
        elements.append(note_el)

        if (note.elapsed_beats + Beat(1, 1)).division == 1:
            elements.append("|")

    if elements[-1] == '|':
        elements[-1] = '=:|'
    else:
        elements.append('=:|')

    return " ".join(elements)


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


def vextab_note_string(note: Note) -> str:
    duration = vextab_duration(note)

    if note.duration.rest:
        note_el = f':{duration} ##'
    else:
        note_el = f":{duration} {note.position.fret}/{note.position.string}"

    return note_el
