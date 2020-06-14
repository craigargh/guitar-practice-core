from unittest import TestCase

from guitarpractice import pickpatterns
from guitarpractice.models import FretPosition, GuitarShape


def get_chord_and_positions():
    positions = [
        FretPosition(string=4, fret=0),
        FretPosition(string=3, fret=2),
        FretPosition(string=2, fret=3),
        FretPosition(string=1, fret=2),
    ]
    chord = GuitarShape(name='D Major', positions=positions, category='chord')
    return chord, positions


class TestStrum(TestCase):
    def test_positions_are_returned_in_single_list(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.strum(chord)

        self.assertEqual(1, len(pattern))
        self.assertEqual(positions, pattern[0])

    def test_shape_is_repeated_when_length_is_set(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.strum(chord, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual(positions, pattern[0])
        self.assertEqual(positions, pattern[1])
        self.assertEqual(positions, pattern[2])
        self.assertEqual(positions, pattern[3])

    def test_value_error_is_raised_if_length_is_less_than_1(self):
        chord, positions = get_chord_and_positions()

        with self.assertRaises(ValueError):
            pickpatterns.strum(chord, length=0)


class TestAsc(TestCase):
    pass


class TestDesc(TestCase):
    pass
