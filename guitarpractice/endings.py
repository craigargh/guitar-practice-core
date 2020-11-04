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


def fill_remaining_with_repeated_patterns(notes: List[Note]) -> List[Note]:
    last_beat = notes[-1].elapsed_beats
    remaining_beat = last_beat.next_bar() - last_beat

    new_notes = []
    elapsed_beats = last_beat
    count = notes[-1].order

    if last_beat <= Beat(2, 4) and last_beat.division % 4 == 0:
        for _ in range(remaining_beat.duration):
            for note in notes:
                elapsed_beats += note.duration
                count += 1

                new_note = Note(
                    duration=note.duration,
                    position=note.position,
                    elapsed_beats=elapsed_beats,
                    order=count,
                    tie=note.tie,
                    annotations=note.annotations,
                )
                new_notes.append(new_note)

    return notes + new_notes
