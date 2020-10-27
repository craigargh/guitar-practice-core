from guitarpractice.models import Sequence


def to_vextab(exercise: Sequence) -> str:
    """
    http://vexflow.com/vextab/tutorial.html
    """
    elements = ['=|:']
    for note in exercise.notes:
        note_el = f":{int(note.duration.division / note.duration.duration)} {note.position.fret}/{note.position.string}"
        elements.append(note_el)

        if note.elapsed_beats.division == 1:
            elements.append("|")

    if elements[-1:] == '|':
        elements[-1:] = '=:|'
    else:
        elements.append('=:|')

    return " ".join(elements)
