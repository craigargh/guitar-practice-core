from math import ceil
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

    def test_full_note_and_four_quarter_notes_are_equal(self):
        full_beat = Beat(duration=1, division=1)
        quarter_beat = Beat(duration=4, division=4)

        self.assertEqual(full_beat, quarter_beat)

    def test_one_fourth_and_four_sixteenths_are_equal(self):
        quarter = Beat(duration=1, division=4)
        sixteenth = Beat(duration=4, division=16)

        self.assertEqual(quarter, sixteenth)

    def test_three_triplets_and_one_fourth_are_equal(self):
        quarter = Beat(duration=1, division=4)
        triplet = Beat(duration=3, division=12)

        self.assertEqual(quarter, triplet)

    def test_can_subtract_notes(self):
        calculations = [
            [Beat(duration=1, division=1), Beat(duration=1, division=1), Beat(duration=0, division=1)],
            [Beat(duration=1, division=1), Beat(duration=1, division=2), Beat(duration=1, division=2)],
            [Beat(duration=1, division=1), Beat(duration=1, division=4), Beat(duration=3, division=4)],
            [Beat(duration=1, division=1), Beat(duration=1, division=8), Beat(duration=7, division=8)],
            [Beat(duration=1, division=1), Beat(duration=1, division=16), Beat(duration=15, division=16)],
            [Beat(duration=1, division=1), Beat(duration=1, division=32), Beat(duration=31, division=32)],
            [Beat(duration=1, division=2), Beat(duration=1, division=2), Beat(duration=0, division=1)],
            [Beat(duration=1, division=2), Beat(duration=1, division=4), Beat(duration=1, division=4)],
            [Beat(duration=1, division=2), Beat(duration=1, division=8), Beat(duration=3, division=8)],
            [Beat(duration=1, division=2), Beat(duration=1, division=16), Beat(duration=7, division=16)],
            [Beat(duration=1, division=2), Beat(duration=1, division=32), Beat(duration=15, division=32)],
            [Beat(duration=1, division=4), Beat(duration=1, division=4), Beat(duration=0, division=1)],
            [Beat(duration=1, division=4), Beat(duration=1, division=8), Beat(duration=1, division=8)],
            [Beat(duration=1, division=4), Beat(duration=1, division=16), Beat(duration=3, division=16)],
            [Beat(duration=1, division=4), Beat(duration=1, division=32), Beat(duration=7, division=32)],
            [Beat(duration=1, division=8), Beat(duration=1, division=8), Beat(duration=0, division=1)],
            [Beat(duration=1, division=8), Beat(duration=1, division=16), Beat(duration=1, division=16)],
            [Beat(duration=1, division=8), Beat(duration=1, division=32), Beat(duration=3, division=32)],
            [Beat(duration=1, division=16), Beat(duration=1, division=16), Beat(duration=0, division=1)],
            [Beat(duration=1, division=16), Beat(duration=1, division=32), Beat(duration=1, division=32)],
            [Beat(duration=1, division=32), Beat(duration=1, division=32), Beat(duration=0, division=1)],
        ]

        for calculation in calculations:
            result = calculation[0] - calculation[1]

            self.assertEqual(calculation[2], result)

    def test_subtracting_the_same_beat_returns_zero_beat(self):
        result = Beat(1, 1) - Beat(1, 1)

        self.assertEqual(Beat(0, 1), result)

    def test_result_of_subtracting_notes_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            Beat(duration=1, division=4) - Beat(duration=1, division=1)

    def test_next_bar_rounds_beat_up_to_the_nearest_whole_beat(self):
        calculations = [
            [Beat(duration=1, division=1), Beat(duration=1, division=1)],
            [Beat(duration=1, division=2), Beat(duration=1, division=1)],
            [Beat(duration=3, division=4), Beat(duration=1, division=1)],
            [Beat(duration=5, division=8), Beat(duration=1, division=1)],
            [Beat(duration=8, division=16), Beat(duration=1, division=1)],
            [Beat(duration=31, division=32), Beat(duration=1, division=1)],
            [Beat(duration=2, division=1), Beat(duration=2, division=1)],
            [Beat(duration=5, division=2), Beat(duration=3, division=1)],
            [Beat(duration=12, division=4), Beat(duration=3, division=1)],
            [Beat(duration=48, division=8), Beat(duration=6, division=1)],
            [Beat(duration=160, division=16), Beat(duration=10, division=1)],
            [Beat(duration=900, division=32), Beat(duration=29, division=1)],
        ]

        for calculation in calculations:
            result = calculation[0].next_bar()

            self.assertEqual(calculation[1], result)

    def test_larger_beats_are_greater_than_smaller_beats(self):
        self.assertGreater(Beat(1, 1), Beat(1, 2))

    def test_smaller_beats_are_not_greater_than_larger_beats(self):
        result = Beat(1, 2) > Beat(1, 1)
        self.assertFalse(result)

    def test_larger_beats_are_greater_or_equal_to_smaller_beats(self):
        self.assertGreaterEqual(Beat(1, 1), Beat(1, 2))

    def test_smaller_beats_are_not_greater_or_equal_to_larger_beats(self):
        result = Beat(1, 2) >= Beat(1, 1)
        self.assertFalse(result)

    def test_smaller_beats_are_lesser_than_bigger_beats(self):
        self.assertLess(Beat(1, 2), Beat(1, 1))

    def test_bigger_beats_are_not_lesser_than_smaller_beats(self):
        result = Beat(1, 1) < Beat(1, 2)
        self.assertFalse(result)

    def test_smaller_beats_are_lesser_or_equal_to_bigger_beats(self):
        self.assertLessEqual(Beat(1, 2), Beat(1, 1))

    def test_bigger_beats_are_not_lesser_or_equal_to_smaller_beats(self):
        result = Beat(1, 1) <= Beat(1, 2)
        self.assertFalse(result)

    def test_greater_than_or_equal_for_same_beats(self):
        self.assertGreaterEqual(Beat(1, 1), Beat(1, 1))

    def test_less_than_or_equal_for_same_beats(self):
        self.assertLessEqual(Beat(1, 1), Beat(1, 1))

    def test_new_bar_returns_true_when_division_is_1(self):
        self.assertTrue(Beat(2, 1).is_new_bar())

    def test_new_bar_returns_true_when_division_is_not_end_beat(self):
        self.assertFalse(Beat(2, 4).is_new_bar())

    def test_new_bar_returns_true_when_division_is_end_beat(self):
        self.assertTrue(Beat(4, 4).is_new_bar())

    def test_rest_beats_are_equal(self):
        self.assertEqual(Beat(1, rest=True), Beat(1, rest=True))

    def test_rest_and_non_rest_beats_are_not_equal(self):
        self.assertNotEqual(Beat(1, rest=True), Beat(1, rest=False))


class TestBeatTieSplit(TestCase):
    def test_tie_split_breaks_down_quarter_notes(self):
        calculations = [
            (Beat(1, 4), [Beat(1, 4)]),
            (Beat(2, 4), [Beat(1, 2)]),
            (Beat(3, 4), [Beat(1, 2), Beat(1, 4)]),
            (Beat(4, 4), [Beat(1, 1)]),
        ]

        for calculation in calculations:
            split = calculation[0].tie_split()
            self.assertEqual(calculation[1], split)

    def test_tie_split_breaks_down_eighth_notes(self):
        calculations = [
            (Beat(1, 8), [Beat(1, 8)]),
            (Beat(2, 8), [Beat(1, 4)]),
            (Beat(3, 8), [Beat(1, 4), Beat(1, 8)]),
            (Beat(4, 8), [Beat(1, 2)]),
            (Beat(5, 8), [Beat(1, 2), Beat(1, 8)]),
            (Beat(6, 8), [Beat(1, 2), Beat(1, 4)]),
            (Beat(7, 8), [Beat(1, 2), Beat(1, 4), Beat(1, 8)]),
            (Beat(8, 8), [Beat(1, 1)]),
        ]

        for calculation in calculations:
            split = calculation[0].tie_split()
            self.assertEqual(calculation[1], split)

    def test_tie_split_breaks_down_sixteenth_notes(self):
        calculations = [
            (Beat(1, 16), [Beat(1, 16)]),
            (Beat(2, 16), [Beat(1, 8)]),
            (Beat(3, 16), [Beat(1, 8), Beat(1, 16)]),
            (Beat(4, 16), [Beat(1, 4)]),
            (Beat(5, 16), [Beat(1, 4), Beat(1, 16)]),
            (Beat(6, 16), [Beat(1, 4), Beat(1, 8)]),
            (Beat(7, 16), [Beat(1, 4), Beat(1, 8), Beat(1, 16)]),
            (Beat(8, 16), [Beat(1, 2)]),
            (Beat(9, 16), [Beat(1, 2), Beat(1, 16)]),
            (Beat(10, 16), [Beat(1, 2), Beat(1, 8)]),
            (Beat(11, 16), [Beat(1, 2), Beat(1, 8), Beat(1, 16)]),
            (Beat(12, 16), [Beat(1, 2), Beat(1, 4)]),
            (Beat(13, 16), [Beat(1, 2), Beat(1, 4), Beat(1, 16)]),
            (Beat(14, 16), [Beat(1, 2), Beat(1, 4), Beat(1, 8)]),
            (Beat(15, 16), [Beat(1, 2), Beat(1, 4), Beat(1, 8), Beat(1, 16)]),
            (Beat(16, 16), [Beat(1, 1)]),
        ]

        for calculation in calculations:
            split = calculation[0].tie_split()
            self.assertEqual(calculation[1], split)

    def test_tie_split_breaks_down_thirty_second_notes(self):
        calculations = [
            (Beat(1, 32), [Beat(1, 32)]),
            (Beat(5, 32), [Beat(1, 8), Beat(1, 32)]),
            (Beat(19, 32), [Beat(1, 2), Beat(1, 16), Beat(1, 32)]),
            (Beat(32, 32), [Beat(1, 1)]),
        ]

        for calculation in calculations:
            split = calculation[0].tie_split()
            self.assertEqual(calculation[1], split)

    def test_multi_bar_beats_are_broken_down(self):
        duration = Beat(5, 1) + Beat(1, 2)
        result = duration.tie_split()

        expected = [Beat(1, 1), Beat(1, 1), Beat(1, 1), Beat(1, 1), Beat(1, 1), Beat(1, 2)]
        self.assertEqual(expected, result)

    def test_odd_rests_can_be_split(self):
        duration = Beat(3, 4, rest=True)
        result = duration.tie_split()

        self.assertEqual([Beat(2, 4, rest=True), Beat(1, 4, rest=True)], result)

    def test_even_rests_are_not_split(self):
        duration = Beat(1, 4, rest=True)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 4, rest=True)], result)

    def test_does_not_convert_half_note_triplets(self):
        duration = Beat(1, 3)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 3)], result)

    def test_does_not_convert_quarter_note_triplets(self):
        duration = Beat(1, 6)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 6)], result)

    def test_does_not_convert_eighth_note_triplets(self):
        duration = Beat(1, 12)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 12)], result)

    def test_does_not_convert_sixteenth_note_triplets(self):
        duration = Beat(1, 24)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 24)], result)

    def test_does_convert_odd_half_note_triplets(self):
        duration = Beat(2, 3)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 3), Beat(1, 3)], result)

    def test_does_convert_odd_quarter_note_triplets(self):
        duration = Beat(3, 6)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 3), Beat(1, 6)], result)

    def test_does_convert_odd_eighth_note_triplets(self):
        duration = Beat(3, 12)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 6), Beat(1, 12)], result)

    def test_does_convert_odd_sixteenth_note_triplets(self):
        duration = Beat(3, 24)
        result = duration.tie_split()

        self.assertEqual([Beat(1, 12), Beat(1, 24)], result)
