from guitarpractice.models import FretPosition, GuitarShape


def c_major() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=3, finger=3, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=1, finger=1, highlighted=True),
        FretPosition(string=1, fret=0)
    ]

    return GuitarShape('C Major', 'chord', positions)


def c_major_seven() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=3, finger=3, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=3, finger=4),
        FretPosition(string=2, fret=1, finger=1, highlighted=True),
        FretPosition(string=1, fret=0)
    ]

    return GuitarShape('C Major 7', 'chord', positions)


def c_major_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=3, finger=2, highlighted=True),
        FretPosition(string=4, fret=2, finger=1),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=3, finger=3),
        FretPosition(string=1, fret=0)
    ]

    return GuitarShape('C Major add 9', 'chord', positions)


def d_minor() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=3, finger=3, highlighted=True),
        FretPosition(string=1, fret=1, finger=1)
    ]

    return GuitarShape('D Minor', 'chord', positions)


def d_minor_seven() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=1, finger=1)
    ]

    return GuitarShape('D Minor 7', 'chord', positions)


def d_minor_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=3, finger=2),
        FretPosition(string=3, fret=2, finger=1),
        FretPosition(string=2, fret=3, finger=3, highlighted=True),
        FretPosition(string=1, fret=0)
    ]

    return GuitarShape('D Minor add 9', 'chord', positions)


def e_minor() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=0, highlighted=True),
        FretPosition(string=5, fret=2, finger=2),
        FretPosition(string=4, fret=2, finger=3, highlighted=True),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=0, highlighted=True),
    ]

    return GuitarShape('E Minor', 'chord', positions)


def e_minor_seven() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=0, highlighted=True),
        FretPosition(string=5, fret=2, finger=1),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=0, highlighted=True),
    ]

    return GuitarShape('E Minor 7', 'chord', positions)


def e_minor_flat_nine() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=0, highlighted=True),
        FretPosition(string=5, fret=2, finger=2),
        FretPosition(string=4, fret=3, finger=3, highlighted=True),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=0, highlighted=True),
    ]

    return GuitarShape('E Minor flat 9', 'chord', positions)


def f_major() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=3, finger=3, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=1, finger=1, highlighted=True),
    ]

    return GuitarShape('F Major', 'chord', positions)


def f_major_seven() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=3, finger=3, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=0),
    ]

    return GuitarShape('F Major 7', 'chord', positions)


def f_major_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=3, finger=3, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=3, finger=4, highlighted=True),
    ]

    return GuitarShape('F Major add 9', 'chord', positions)


def g_major() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=3, finger=2, highlighted=True),
        FretPosition(string=5, fret=2, finger=1),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=0, highlighted=True),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=3, finger=3, highlighted=True),
    ]

    return GuitarShape('G Major', 'chord', positions)


def g_seven() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=3, finger=3, highlighted=True),
        FretPosition(string=5, fret=2, finger=2),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=0, highlighted=True),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=1, finger=1),
    ]

    return GuitarShape('G 7', 'chord', positions)


def g_major_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=3, finger=2, highlighted=True),
        FretPosition(string=5, fret=0),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=2, finger=1),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=3, finger=4, highlighted=True),
    ]

    return GuitarShape('G Major add 9', 'chord', positions)


def a_minor() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=0, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=2, finger=3, highlighted=True),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=0, highlighted=True)
    ]

    return GuitarShape('A Minor', 'chord', positions)


def a_minor_seven() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=0, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=0, highlighted=True)
    ]

    return GuitarShape('A Minor 7', 'chord', positions)


def a_minor_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=0, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=4, finger=4),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=0, highlighted=True)
    ]

    return GuitarShape('A Minor add 9', 'chord', positions)


def b_diminished() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=4, finger=4, highlighted=True),
        FretPosition(string=2, fret=0, highlighted=True),
        FretPosition(string=1, fret=1, finger=1),
    ]

    return GuitarShape('B Diminished', 'chord', positions)


def b_minor_seven_flat_five() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=0, highlighted=True),
        FretPosition(string=1, fret=1, finger=1),
    ]

    return GuitarShape('B Minor 7 Flat 5', 'chord', positions)


def b_diminished_flat_9() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=4, finger=4, highlighted=True),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=1, finger=1),
    ]

    return GuitarShape('B Diminished flat 9', 'chord', positions)
