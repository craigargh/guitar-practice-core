from ..exercises.rhythm_sixteenth_notes import rhythm_sixteenth_notes

rhythm_notation = {
    4: "𝅘𝅥",
    8: "",
}


def run():
    sequence = rhythm_sixteenth_notes(level=1)
    columns = max(note.order for note in sequence.notes)
    highest_fret = max(note.position.fret for note in sequence.notes)
    strings = 6

    if highest_fret > 9:
        placeholder = "--"
        fret_length = 2
    else:
        placeholder = "-"
        fret_length = 1

    tab_buffer = [
        [placeholder for _ in range(columns)]
        for _ in range(strings)
    ]

    for note in sequence.notes:
        if fret_length == 2:
            fret = '{:-<2}'.format(note.position.fret)
        else:
            fret = str(note.position.fret)

        tab_buffer[note.position.string - 1][note.order - 1] = fret

    for string in tab_buffer:
        print("-".join(string))
