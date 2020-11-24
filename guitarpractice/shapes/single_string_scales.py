"""
http://www.fretjam.com/single-string-scales.html
"""
from guitarpractice.models import FretPosition, GuitarShape


def chromatic_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=2),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=4),
        FretPosition(string=6, fret=5),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=7),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=9),
        FretPosition(string=6, fret=10),
        FretPosition(string=6, fret=11),
        FretPosition(string=6, fret=12),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Chromatic', 'scale', positions)


def major_pentatonic_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=5),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=10),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Major Pentatonic', 'scale', positions)


def major_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=5),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=10),
        FretPosition(string=6, fret=12),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Major', 'scale', positions)


def mixolydian_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=5),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=10),
        FretPosition(string=6, fret=11),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Mixolydian', 'scale', positions)


def lydian_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=5),
        FretPosition(string=6, fret=7),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=10),
        FretPosition(string=6, fret=12),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Lydian', 'scale', positions)


def phrygian_dominant_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=2),
        FretPosition(string=6, fret=5),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=9),
        FretPosition(string=6, fret=11),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Phrygian Dominant', 'scale', positions)


def minor_pentatonic_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=4),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=11),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Minor Pentatonic', 'scale', positions)


def minor_blues_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=4),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=7),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=11),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Minor Blues', 'scale', positions)


def natural_minor_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=4),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=9),
        FretPosition(string=6, fret=11),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Natural Minor', 'scale', positions)


def harmonic_minor_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=4),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=9),
        FretPosition(string=6, fret=12),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Harmonic Minor', 'scale', positions)


def melodic_minor_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=4),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=10),
        FretPosition(string=6, fret=12),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Melodic Minor', 'scale', positions)


def dorian_string_6():
    positions = [
        FretPosition(string=6, fret=1),
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=4),
        FretPosition(string=6, fret=6),
        FretPosition(string=6, fret=8),
        FretPosition(string=6, fret=10),
        FretPosition(string=6, fret=11),
        FretPosition(string=6, fret=13),
    ]

    return GuitarShape('Dorian', 'scale', positions)


def chromatic_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=2),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=4),
        FretPosition(string=5, fret=5),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=7),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=9),
        FretPosition(string=5, fret=10),
        FretPosition(string=5, fret=11),
        FretPosition(string=5, fret=12),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Chromatic', 'scale', positions)


def major_pentatonic_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=5),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=10),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Major Pentatonic', 'scale', positions)


def major_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=5),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=10),
        FretPosition(string=5, fret=12),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Major', 'scale', positions)


def mixolydian_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=5),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=10),
        FretPosition(string=5, fret=11),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Mixolydian', 'scale', positions)


def lydian_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=5),
        FretPosition(string=5, fret=7),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=10),
        FretPosition(string=5, fret=12),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Lydian', 'scale', positions)


def phrygian_dominant_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=2),
        FretPosition(string=5, fret=5),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=9),
        FretPosition(string=5, fret=11),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Phrygian Dominant', 'scale', positions)


def minor_pentatonic_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=4),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=11),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Minor Pentatonic', 'scale', positions)


def minor_blues_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=4),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=7),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=11),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Minor Blues', 'scale', positions)


def natural_minor_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=4),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=9),
        FretPosition(string=5, fret=11),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Natural Minor', 'scale', positions)


def harmonic_minor_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=4),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=9),
        FretPosition(string=5, fret=12),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Harmonic Minor', 'scale', positions)


def melodic_minor_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=4),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=10),
        FretPosition(string=5, fret=12),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Melodic Minor', 'scale', positions)


def dorian_string_5():
    positions = [
        FretPosition(string=5, fret=1),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=4),
        FretPosition(string=5, fret=6),
        FretPosition(string=5, fret=8),
        FretPosition(string=5, fret=10),
        FretPosition(string=5, fret=11),
        FretPosition(string=5, fret=13),
    ]

    return GuitarShape('Dorian', 'scale', positions)
