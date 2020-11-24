from guitarpractice.models import FretPosition, GuitarShape


def chromatic_5_notes_per_string():
    positions = [
        FretPosition(string=6, fret=5),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=7),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=9),
        FretPosition(string=5, fret=5),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=7),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=9),
        FretPosition(string=4, fret=5),
        FretPosition(string=4, fret=6),
        FretPosition(string=4, fret=7),
        FretPosition(string=4, fret=8),
        FretPosition(string=4, fret=9),
        FretPosition(string=3, fret=5),
        FretPosition(string=3, fret=6),
        FretPosition(string=3, fret=7),
        FretPosition(string=3, fret=8),
        FretPosition(string=2, fret=5),
        FretPosition(string=2, fret=6),
        FretPosition(string=2, fret=7),
        FretPosition(string=2, fret=8),
        FretPosition(string=2, fret=9),
        FretPosition(string=1, fret=5),
        FretPosition(string=1, fret=6),
        FretPosition(string=1, fret=7),
        FretPosition(string=1, fret=8),
        FretPosition(string=1, fret=9),
    ]

    return GuitarShape('Chromatic', 'scale', positions)


def chromatic_4_notes_per_string():
    positions = [
        FretPosition(string=6, fret=5),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=7),
        FretPosition(string=6, fret=8),

        FretPosition(string=5, fret=4),
        FretPosition(string=5, fret=5),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=7),

        FretPosition(string=4, fret=3),
        FretPosition(string=4, fret=4),
        FretPosition(string=4, fret=5),
        FretPosition(string=4, fret=6),

        FretPosition(string=3, fret=2),
        FretPosition(string=3, fret=3),
        FretPosition(string=3, fret=4),
        FretPosition(string=3, fret=5),

        FretPosition(string=2, fret=2),
        FretPosition(string=2, fret=3),
        FretPosition(string=2, fret=4),
        FretPosition(string=2, fret=5),

        FretPosition(string=1, fret=1),
        FretPosition(string=1, fret=2),
        FretPosition(string=1, fret=3),
        FretPosition(string=1, fret=4),
    ]

    return GuitarShape('Chromatic', 'scale', positions)
