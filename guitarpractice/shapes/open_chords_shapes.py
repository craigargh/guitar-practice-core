from guitarpractice.models import FretPosition, GuitarShape


def open_major_root_6_var_1():
    positions = [
        FretPosition(string=6, fret=0, highlighted=True),
        FretPosition(string=5, fret=2, finger=2),
        FretPosition(string=4, fret=2, finger=3, highlighted=True),
        FretPosition(string=3, fret=1, finger=1),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=0, highlighted=True),
    ]
    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=False)


def open_major_root_6_var_2():
    positions = [
        FretPosition(string=6, fret=3, finger=2, highlighted=True),
        FretPosition(string=5, fret=2, finger=1),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=0, highlighted=True),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=3, finger=3, highlighted=True),
    ]
    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=False)


def open_major_root_5_var_1():
    positions = [
        FretPosition(string=5, fret=0, highlighted=True),
        FretPosition(string=4, fret=2, finger=3),
        FretPosition(string=3, fret=2, finger=2, highlighted=True),
        FretPosition(string=2, fret=2, finger=1),
        FretPosition(string=1, fret=0, highlighted=True)
    ]

    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=False)


def open_major_root_5_var_2():
    positions = [
        FretPosition(string=5, fret=3, finger=3, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=1, finger=1, highlighted=True),
        FretPosition(string=1, fret=0)
    ]
    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=False)


def open_major_root_4_var_1():
    positions = [
        FretPosition(string=4, fret=0, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=3, finger=3, highlighted=True),
        FretPosition(string=1, fret=1, finger=1)
    ]
    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=False)
