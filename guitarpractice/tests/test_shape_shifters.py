from unittest import TestCase

from guitarpractice.models import FretPosition, GuitarShape
from guitarpractice.shapeshifters import shift_vertically


class TestShiftVertically(TestCase):
    def test_setting_lowest_fret_to_lower_number_moves_shape_down(self):
        positions = [
            FretPosition(fret=5, string=6),
            FretPosition(fret=7, string=5),
        ]
        shape = GuitarShape('Power chord', 'chord', positions=positions)

        result = shift_vertically(shape, 1)

        expected_positions = [
            FretPosition(fret=1, string=6),
            FretPosition(fret=3, string=5),
        ]
        self.assertEqual(expected_positions, result.positions)

    def test_setting_lowest_fret_to_lower_number_moves_shape_up(self):
        positions = [
            FretPosition(fret=5, string=6),
            FretPosition(fret=7, string=5),
        ]
        shape = GuitarShape('Power chord', 'chord', positions=positions)

        result = shift_vertically(shape, 10)

        expected_positions = [
            FretPosition(fret=10, string=6),
            FretPosition(fret=12, string=5),
        ]
        self.assertEqual(expected_positions, result.positions)

    def test_setting_lowest_fret_to_same_lowest_fret_does_not_move_shape(self):
        positions = [
            FretPosition(fret=5, string=6),
            FretPosition(fret=7, string=5),
        ]
        shape = GuitarShape('Power chord', 'chord', positions=positions)

        result = shift_vertically(shape, 5)

        expected_positions = [
            FretPosition(fret=5, string=6),
            FretPosition(fret=7, string=5),
        ]
        self.assertEqual(expected_positions, result.positions)
