from unittest import TestCase
from guitarpractice.models import FretPosition


class TestFretPosition(TestCase):
    def test_position_on_lower_string_is_less_than_higher_string(self):
        lower_position = FretPosition(fret=1, string=6)
        higher_position = FretPosition(fret=1, string=5)

        self.assertLess(lower_position, higher_position)

    def test_same_position_is_equal(self):
        position_1 = FretPosition(fret=1, string=6)
        position_2 = FretPosition(fret=1, string=6)

        self.assertEqual(position_1, position_2)

    def test_same_string_higher_fret_is_greater(self):
        lower_position = FretPosition(fret=1, string=6)
        higher_position = FretPosition(fret=2, string=6)

        self.assertLess(lower_position, higher_position)
