from typing import List

from guitarpractice.models import Note, Beat


def fill_remaining_bar_with_rests(notes: List[Note]) -> List[Note]:
    last_beat = notes[-1].elapsed_beats
    remaining_beat = last_beat.next_bar() - last_beat

    if remaining_beat == Beat(0, 1):
        return notes

    remaining_beat.rest = True
    order = notes[-1].order + 1
    elapsed_beats = last_beat + remaining_beat

    rest_note = Note(position=None, duration=remaining_beat, elapsed_beats=elapsed_beats, order=order)

    return notes + [rest_note]
