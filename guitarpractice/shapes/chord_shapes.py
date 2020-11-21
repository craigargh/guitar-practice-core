from guitarpractice.models import FretPosition, GuitarShape


def c_major() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=3, finger=3, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=1, finger=1, highlighted=True),
        FretPosition(string=1, fret=0)
    ]

    return GuitarShape('C Major', 'chord', positions, short_name='C')


def c_major_seven() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=3, finger=3, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=3, finger=4),
        FretPosition(string=2, fret=1, finger=1, highlighted=True),
        FretPosition(string=1, fret=0)
    ]

    return GuitarShape('C Major 7', 'chord', positions, short_name='Cmaj7')


def c_major_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=3, finger=2, highlighted=True),
        FretPosition(string=4, fret=2, finger=1),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=3, finger=3),
        FretPosition(string=1, fret=0)
    ]

    return GuitarShape('C Major add 9', 'chord', positions, short_name='Cadd9')


def d_minor() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=3, finger=3, highlighted=True),
        FretPosition(string=1, fret=1, finger=1)
    ]

    return GuitarShape('D Minor', 'chord', positions, short_name='Dm')


def d_minor_seven() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=1, finger=1)
    ]

    return GuitarShape('D Minor 7', 'chord', positions, short_name='Dm7')


def d_minor_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=3, finger=2),
        FretPosition(string=3, fret=2, finger=1),
        FretPosition(string=2, fret=3, finger=3, highlighted=True),
        FretPosition(string=1, fret=0)
    ]

    return GuitarShape('D Minor add 9', 'chord', positions, short_name='Dmadd9')


def e_minor() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=0, highlighted=True),
        FretPosition(string=5, fret=2, finger=2),
        FretPosition(string=4, fret=2, finger=3, highlighted=True),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=0, highlighted=True),
    ]

    return GuitarShape('E Minor', 'chord', positions, short_name='Em')


def e_minor_seven() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=0, highlighted=True),
        FretPosition(string=5, fret=2, finger=1),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=0, highlighted=True),
    ]

    return GuitarShape('E Minor 7', 'chord', positions, short_name='Em7')


def e_minor_flat_nine() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=0, highlighted=True),
        FretPosition(string=5, fret=2, finger=2),
        FretPosition(string=4, fret=3, finger=3, highlighted=True),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=0, highlighted=True),
    ]

    return GuitarShape('E Minor flat 9', 'chord', positions, short_name='Emb9')


def f_major() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=3, finger=3, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=1, finger=1, highlighted=True),
    ]

    return GuitarShape('F Major', 'chord', positions, short_name='F')


def f_major_seven() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=3, finger=3, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=0),
    ]

    return GuitarShape('F Major 7', 'chord', positions, short_name='Fmaj7')


def f_major_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=3, finger=3, highlighted=True),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=3, finger=4),
    ]

    return GuitarShape('F Major add 9', 'chord', positions, short_name='Fadd9')


def g_major() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=3, finger=2, highlighted=True),
        FretPosition(string=5, fret=2, finger=1),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=0, highlighted=True),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=3, finger=3, highlighted=True),
    ]

    return GuitarShape('G Major', 'chord', positions, short_name='G')


def g_seven() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=3, finger=3, highlighted=True),
        FretPosition(string=5, fret=2, finger=2),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=0, highlighted=True),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=1, finger=1),
    ]

    return GuitarShape('G 7', 'chord', positions, short_name='G7')


def g_major_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=6, fret=3, finger=2, highlighted=True),
        FretPosition(string=5, fret=0),
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=2, finger=1),
        FretPosition(string=2, fret=0),
        FretPosition(string=1, fret=3, finger=4, highlighted=True),
    ]

    return GuitarShape('G Major add 9', 'chord', positions, short_name='Gadd9')


def a_minor() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=0, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=2, finger=3, highlighted=True),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=0, highlighted=True)
    ]

    return GuitarShape('A Minor', 'chord', positions, short_name='Am')


def a_minor_seven() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=0, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=0),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=0, highlighted=True)
    ]

    return GuitarShape('A Minor 7', 'chord', positions, short_name='Am7')


def a_minor_add_9() -> GuitarShape:
    positions = [
        FretPosition(string=5, fret=0, highlighted=True),
        FretPosition(string=4, fret=2, finger=2),
        FretPosition(string=3, fret=4, finger=4),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=0, highlighted=True)
    ]

    return GuitarShape('A Minor add 9', 'chord', positions, short_name='Amadd9')


def b_diminished() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=4, finger=4, highlighted=True),
        FretPosition(string=2, fret=0, highlighted=True),
        FretPosition(string=1, fret=1, finger=1),
    ]

    return GuitarShape('B Diminished', 'chord', positions, short_name='Bdim')


def b_minor_seven_flat_five() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=2, finger=2),
        FretPosition(string=2, fret=0, highlighted=True),
        FretPosition(string=1, fret=1, finger=1),
    ]

    return GuitarShape('B Minor 7 Flat 5', 'chord', positions, short_name='Bm7b5')


def b_diminished_flat_9() -> GuitarShape:
    positions = [
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=4, finger=4, highlighted=True),
        FretPosition(string=2, fret=1, finger=1),
        FretPosition(string=1, fret=1, finger=1),
    ]

    return GuitarShape('B Diminished flat 9', 'chord', positions, short_name='Bdimb9')
