from unittest import TestCase

from guitarpractice.models import Note, Beat, FretPosition
from guitarpractice.sequenceshifters import repeat_each_position


class TestSequenceShifters(TestCase):
    def test_repeat_each_position_repeats_each_item_twice_by_default(self):
        original_sequence = [
            [FretPosition(fret=0, string=6)]
        ]

        result = repeat_each_position(original_sequence)

        expected_sequence = [
            [FretPosition(fret=0, string=6)],
            [FretPosition(fret=0, string=6)],
        ]

        self.assertEqual(expected_sequence, result)

    def test_can_set_number_of_repeats(self):
        original_sequence = [
            [FretPosition(fret=0, string=6)]
        ]

        result = repeat_each_position(original_sequence, repeats=3)

        expected_sequence = [
            [FretPosition(fret=0, string=6)],
            [FretPosition(fret=0, string=6)],
            [FretPosition(fret=0, string=6)],
        ]

        self.assertEqual(expected_sequence, result)

    def test_each_position_is_repeated(self):
        original_sequence = [
            [FretPosition(fret=0, string=6)],
            [FretPosition(fret=5, string=6)]
        ]

        result = repeat_each_position(original_sequence, repeats=3)

        expected_sequence = [
            [FretPosition(fret=0, string=6)],
            [FretPosition(fret=0, string=6)],
            [FretPosition(fret=0, string=6)],
            [FretPosition(fret=5, string=6)],
            [FretPosition(fret=5, string=6)],
            [FretPosition(fret=5, string=6)],
        ]

        self.assertEqual(expected_sequence, result)
