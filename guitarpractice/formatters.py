from guitarpractice.models import Sequence


def to_vextab(exercise: Sequence) -> str:
    notes = [
        f":{int(note.duration.division / note.duration.duration)} {note.position.fret}/{note.position.string}"
        for note in exercise.notes
    ]

    return " ".join(notes)
