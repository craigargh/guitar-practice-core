from unittest import TestCase
from guitarpractice.models import FretPosition, Beat


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


class TestBeat(TestCase):
    def test_can_add_two_beats_together(self):
        beat1 = Beat(duration=1, division=1)
        beat2 = Beat(duration=2, division=1)

        result = beat1 + beat2

        self.assertEqual(Beat(duration=3, division=1), result)

    def test_can_add_two_half_notes_together(self):
        beat1 = Beat(duration=1, division=2)
        beat2 = Beat(duration=1, division=2)

        result = beat1 + beat2

        self.assertEqual(Beat(duration=1, division=1), result)

    def test_can_add_a_half_and_whole_note_together(self):
        beat1 = Beat(duration=1, division=2)
        beat2 = Beat(duration=1, division=1)

        result = beat1 + beat2

        self.assertEqual(Beat(duration=3, division=2), result)

    def test_can_add_two_triplets_together(self):
        beat1 = Beat(duration=1, division=3)
        beat2 = Beat(duration=1, division=3)

        result = beat1 + beat2

        self.assertEqual(Beat(duration=2, division=3), result)

    def test_can_add_three_triplets_together(self):
        beat1 = Beat(duration=1, division=3)
        beat2 = Beat(duration=1, division=3)
        beat3 = Beat(duration=1, division=3)

        result = beat1 + beat2 + beat3

        self.assertEqual(Beat(duration=1, division=1), result)

    def test_can_add_to_zero_duration_beat(self):
        beat1 = Beat(duration=0, division=1)
        beat2 = Beat(duration=1, division=1)

        result = beat1 + beat2

        self.assertEqual(Beat(duration=1, division=1), result)

    def test_whole_beats_returns_number_of_full_beats(self):
        beat = Beat(duration=11, division=2)
        self.assertEqual(5, beat.whole_beats)

    def test_subdivision_offset_returns_beat_subtracting_whole_beats(self):
        beat = Beat(duration=11, division=2)
        self.assertEqual(Beat(1, 2), beat.subdivision_offset)
