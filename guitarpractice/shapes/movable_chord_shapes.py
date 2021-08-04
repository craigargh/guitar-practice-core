from guitarpractice.models import GuitarShape, FretPosition


def movable_major_root_6_var_1() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=5, finger=1, highlighted=True),
        FretPosition(string=5, fret=7, finger=3),
        FretPosition(string=4, fret=7, finger=4, highlighted=True),
        FretPosition(string=3, fret=6, finger=2),
        FretPosition(string=2, fret=5, finger=1),
        FretPosition(string=1, fret=5, finger=1, highlighted=True),
    ]

    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=True)


def movable_major_root_5_var_1() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=5, finger=1, highlighted=True),
        FretPosition(string=4, fret=7, finger=2),
        FretPosition(string=3, fret=7, finger=3, highlighted=True),
        FretPosition(string=2, fret=7, finger=4),
        FretPosition(string=1, fret=5, finger=1, highlighted=True)
    ]

    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=True)


def movable_major_root_4_var_1() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=7, finger=3, highlighted=True),
        FretPosition(string=3, fret=6, finger=2),
        FretPosition(string=2, fret=5, finger=1),
        FretPosition(string=1, fret=5, finger=1, highlighted=True),
    ]

    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=True)


def movable_major_root_4_var_2() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=5, finger=1, highlighted=True),
        FretPosition(string=3, fret=7, finger=2),
        FretPosition(string=2, fret=8, finger=4, highlighted=True),
        FretPosition(string=1, fret=7, finger=3)
    ]

    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=True)


def movable_major_root_3_var_1() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=5, finger=1),
        FretPosition(string=3, fret=5, finger=1, highlighted=True),
        FretPosition(string=2, fret=5, finger=1),
        FretPosition(string=1, fret=8, finger=4)
    ]

    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=True)


def movable_major_root_2_var_1() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=7, finger=3),
        FretPosition(string=3, fret=5, finger=1),
        FretPosition(string=2, fret=6, finger=2, highlighted=True),
        FretPosition(string=1, fret=5, finger=1)
    ]

    return GuitarShape('Major', 'chord', positions, tonality='maj', frets_movable=True)
