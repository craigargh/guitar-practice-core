import random
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


def get_scale_and_positions():
    positions = [
        FretPosition(string=6, fret=3),
        FretPosition(string=6, fret=6),
        FretPosition(string=5, fret=3),
        FretPosition(string=5, fret=5),
        FretPosition(string=4, fret=3),
        FretPosition(string=4, fret=5),
    ]
    scale = GuitarShape(name='C Major Pentatonic', positions=positions, category='scale')
    return scale, positions


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
    def test_positions_are_returned_in_ascending_order(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc(chord)

        self.assertEqual(4, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[2])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[3])

    def test_last_notes_are_repeated_when_length_is_greater_than_positions_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc(chord, length=6)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[2]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[2]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])

    def test_last_notes_are_repeated_when_length_is_more_than_double_positions_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc(chord, length=10)

        self.assertEqual(10, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[2]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[1]], pattern[5])
        self.assertEqual([positions[2]], pattern[6])
        self.assertEqual([positions[3]], pattern[7])
        self.assertEqual([positions[2]], pattern[8])
        self.assertEqual([positions[3]], pattern[9])

    def test_can_shorten_pattern(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc(chord, length=2)

        self.assertEqual(2, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])

    def test_length_of_zero_raises_error(self):
        chord, positions = get_chord_and_positions()

        with self.assertRaises(ValueError):
            pickpatterns.asc(chord, length=0)

    def test_lowest_note_returned_for_length_of_1(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestDesc(TestCase):
    def test_positions_are_returned_is_descending_order(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.desc(chord)

        self.assertEqual([FretPosition(string=1, fret=2)], pattern[0])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[1])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[2])
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[3])

    def test_last_notes_are_repeated_when_length_is_greater_than_positions_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.desc(chord, length=6)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[3]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[1]], pattern[2])
        self.assertEqual([positions[0]], pattern[3])
        self.assertEqual([positions[1]], pattern[4])
        self.assertEqual([positions[0]], pattern[5])

    def test_last_notes_are_repeated_when_length_is_more_than_double_positions_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.desc(chord, length=10)

        self.assertEqual(10, len(pattern))
        self.assertEqual([positions[3]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[1]], pattern[2])
        self.assertEqual([positions[0]], pattern[3])
        self.assertEqual([positions[3]], pattern[4])
        self.assertEqual([positions[2]], pattern[5])
        self.assertEqual([positions[1]], pattern[6])
        self.assertEqual([positions[0]], pattern[7])
        self.assertEqual([positions[1]], pattern[8])
        self.assertEqual([positions[0]], pattern[9])

    def test_can_shorten_pattern(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.desc(chord, length=2)

        self.assertEqual(2, len(pattern))
        self.assertEqual([positions[3]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])

    def test_length_of_zero_raises_error(self):
        chord, positions = get_chord_and_positions()

        with self.assertRaises(ValueError):
            pickpatterns.desc(chord, length=0)

    def test_highest_note_returned_for_length_of_1(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.desc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[3]], pattern[0])


class TestAscAndDesc(TestCase):
    def test_pattern_is_sorted_into_asc_and_desc_order(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc_and_desc(chord)

        self.assertEqual(8, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[2])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[3])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[4])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[5])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[6])
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[7])

    def test_even_length_repeats_top_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc_and_desc(chord, length=8)

        self.assertEqual(8, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[2])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[3])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[4])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[5])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[6])
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[7])

    def test_uneven_length_does_not_repeat_top_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc_and_desc(chord, length=7)

        self.assertEqual(7, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[2])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[3])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[4])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[5])
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[6])

    def test_even_shortened_pattern_uses_first_notes_from_asc_and_first_notes_from_desc(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc_and_desc(chord, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[2])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[3])

    def test_single_string_extended_twice_pattern_repeats_pattern_fully(self):
        positions = [
            FretPosition(5, 6),
            FretPosition(7, 6),
            FretPosition(8, 6),
        ]
        shape = GuitarShape('single string shape', 'scale', positions=positions)

        pattern = pickpatterns.asc_and_desc(shape, length=8)

        self.assertEqual(8, len(pattern))
        self.assertEqual([FretPosition(fret=5, string=6)], pattern[0])
        self.assertEqual([FretPosition(fret=7, string=6)], pattern[1])
        self.assertEqual([FretPosition(fret=8, string=6)], pattern[2])
        self.assertEqual([FretPosition(fret=7, string=6)], pattern[3])
        self.assertEqual([FretPosition(fret=5, string=6)], pattern[4])
        self.assertEqual([FretPosition(fret=7, string=6)], pattern[5])
        self.assertEqual([FretPosition(fret=8, string=6)], pattern[6])
        self.assertEqual([FretPosition(fret=7, string=6)], pattern[7])

    def test_uneven_shortened_pattern_uses_first_notes_from_asc_and_desc(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc_and_desc(chord, length=5)

        self.assertEqual(5, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[2])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[3])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[4])

    def test_even_lengthened_pattern_repeats_end_notes_on_asc_and_desc(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc_and_desc(chord, length=10)

        self.assertEqual(10, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[2])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[3])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[4])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[5])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[6])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[7])
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[8])
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[9])

    def test_uneven_lengthened_pattern_uses_last_notes_from_asc_and_desc(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc_and_desc(chord, length=9)

        self.assertEqual(9, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[2])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[3])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[4])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[5])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[6])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[7])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[8])

    def test_length_of_one_returns_first_position(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.asc_and_desc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])


class TestBassAndAsc(TestCase):
    def test_positions_are_returned_in_ascending_order(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_asc(chord)

        self.assertEqual(4, len(pattern))
        self.assertEqual([FretPosition(string=4, fret=0)], pattern[0])
        self.assertEqual([FretPosition(string=3, fret=2)], pattern[1])
        self.assertEqual([FretPosition(string=2, fret=3)], pattern[2])
        self.assertEqual([FretPosition(string=1, fret=2)], pattern[3])

    def test_last_notes_are_repeated_when_length_is_greater_than_positions_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_asc(chord, length=6)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[2]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[2]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])

    def test_bass_notes_are_not_repeated_when_length_is_more_than_double_positions_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_asc(chord, length=10)

        self.assertEqual(10, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[2]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[1]], pattern[4])
        self.assertEqual([positions[2]], pattern[5])
        self.assertEqual([positions[3]], pattern[6])
        self.assertEqual([positions[1]], pattern[7])
        self.assertEqual([positions[2]], pattern[8])
        self.assertEqual([positions[3]], pattern[9])

    def test_bass_note_is_played_when_pattern_is_shortened(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_asc(chord, length=3)

        self.assertEqual(3, len(pattern))
        self.assertEqual([positions[0]], pattern[0])

    def test_pattern_is_shortened_from_last_positions_not_first_positions(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_asc(chord, length=3)

        self.assertEqual(3, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[3]], pattern[2])

    def test_only_bass_note_is_returned_for_length_of_1(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_asc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestBassAndDesc(TestCase):
    def test_pattern_is_returned_bass_note_then_desc_order(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_desc(chord)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[2]], pattern[2])
        self.assertEqual([positions[1]], pattern[3])

    def test_last_notes_are_repeated_when_length_is_greater_than_positions_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_desc(chord, length=6)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[2]], pattern[2])
        self.assertEqual([positions[1]], pattern[3])
        self.assertEqual([positions[2]], pattern[4])
        self.assertEqual([positions[1]], pattern[5])

    def test_bass_note_is_played_when_pattern_is_shortened(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_desc(chord, length=3)

        self.assertEqual(3, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[2]], pattern[2])

    def test_only_bass_note_is_returned_for_length_of_1(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_desc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestBassAscAndDesc(TestCase):
    def test_pattern_is_returned_bass_note_then_asc_and_desc_order(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_asc_and_desc(chord)

        self.assertEqual(7, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[2]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[3]], pattern[4])
        self.assertEqual([positions[2]], pattern[5])
        self.assertEqual([positions[1]], pattern[6])

    def test_shortening_even_pattern_returns_final_notes_of_asc(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_asc_and_desc(chord, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[3]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])

    def test_shortening_odd_pattern_repeats_top_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_asc_and_desc(chord, length=5)

        self.assertEqual(5, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[3]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[2]], pattern[4])

    def test_only_bass_note_is_returned_for_length_of_1(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_asc_and_desc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestBassAndStrum(TestCase):
    def test_bass_note_then_strummed_chord_is_returned(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_strum(chord)

        self.assertEqual(2, len(pattern))
        self.assertEqual(4, len(pattern[1]))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual(chord.positions, pattern[1])

    def test_lengthen_repeats_strummed_chord(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_strum(chord, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual(chord.positions, pattern[1])
        self.assertEqual(chord.positions, pattern[2])
        self.assertEqual(chord.positions, pattern[3])

    def test_only_bass_note_is_returned_for_length_of_1(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.bass_and_strum(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestAlternatingBassAndAsc(TestCase):
    def test_bass_note_is_played_every_other_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_asc(chord)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])

    def test_can_shorten_pattern_to_even_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_asc(chord, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])

    def test_can_shorten_pattern_to_odd_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_asc(chord, length=5)

        self.assertEqual(5, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])

    def test_can_lengthen_pattern_to_even_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_asc(chord, length=8)

        self.assertEqual(8, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[3]], pattern[7])

    def test_can_lengthen_pattern_to_odd_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_asc(chord, length=7)

        self.assertEqual(7, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])

    def test_length_of_one_returns_bass_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_asc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestAlternatingBassAndDesc(TestCase):
    def test_bass_note_is_played_every_other_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_desc(chord)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[1]], pattern[5])

    def test_can_shorten_pattern_to_even_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_desc(chord, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])

    def test_can_shorten_pattern_to_odd_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_desc(chord, length=5)

        self.assertEqual(5, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])

    def test_can_lengthen_pattern_to_even_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_desc(chord, length=8)

        self.assertEqual(8, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[1]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[1]], pattern[7])

    def test_can_lengthen_pattern_to_odd_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_desc(chord, length=7)

        self.assertEqual(7, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[1]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])

    def test_length_of_one_returns_bass_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_and_desc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestAlternatingBassAscAndDesc(TestCase):
    def test_bass_note_is_played_every_other_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc(chord)

        self.assertEqual(12, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[3]], pattern[7])
        self.assertEqual([positions[0]], pattern[8])
        self.assertEqual([positions[2]], pattern[9])
        self.assertEqual([positions[0]], pattern[10])
        self.assertEqual([positions[1]], pattern[11])

    def test_can_shorten_pattern_to_even_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc(chord, length=8)

        self.assertEqual(8, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[2]], pattern[7])

    def test_can_shorten_pattern_to_odd_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc(chord, length=7)

        self.assertEqual(7, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])

    def test_can_lengthen_pattern_to_even_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc(chord, length=14)

        self.assertEqual(14, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[3]], pattern[7])
        self.assertEqual([positions[0]], pattern[8])
        self.assertEqual([positions[3]], pattern[9])
        self.assertEqual([positions[0]], pattern[10])
        self.assertEqual([positions[2]], pattern[11])
        self.assertEqual([positions[0]], pattern[12])
        self.assertEqual([positions[1]], pattern[13])

    def test_can_lengthen_pattern_to_odd_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc(chord, length=13)

        self.assertEqual(13, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[3]], pattern[7])
        self.assertEqual([positions[0]], pattern[8])
        self.assertEqual([positions[2]], pattern[9])
        self.assertEqual([positions[0]], pattern[10])
        self.assertEqual([positions[1]], pattern[11])
        self.assertEqual([positions[0]], pattern[12])

    def test_length_of_one_returns_bass_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestAlternatingBassAscAndDescTopStrings(TestCase):
    def test_bass_note_is_played_every_other_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc_top_strings(chord)

        self.assertEqual(12, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[3]], pattern[7])
        self.assertEqual([positions[0]], pattern[8])
        self.assertEqual([positions[2]], pattern[9])
        self.assertEqual([positions[0]], pattern[10])
        self.assertEqual([positions[1]], pattern[11])

    def test_can_shorten_pattern_to_even_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc_top_strings(chord, length=8)

        self.assertEqual(8, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[2]], pattern[7])

    def test_can_shorten_pattern_to_odd_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc_top_strings(chord, length=7)

        self.assertEqual(7, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[2]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])

    def test_can_lengthen_pattern_to_even_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc_top_strings(chord, length=14)

        self.assertEqual(14, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[3]], pattern[7])
        self.assertEqual([positions[0]], pattern[8])
        self.assertEqual([positions[2]], pattern[9])
        self.assertEqual([positions[0]], pattern[10])
        self.assertEqual([positions[1]], pattern[11])
        self.assertEqual([positions[0]], pattern[12])
        self.assertEqual([positions[1]], pattern[13])

    def test_can_lengthen_pattern_to_odd_length(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc_top_strings(chord, length=13)

        self.assertEqual(13, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[1]], pattern[1])
        self.assertEqual([positions[0]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[0]], pattern[4])
        self.assertEqual([positions[3]], pattern[5])
        self.assertEqual([positions[0]], pattern[6])
        self.assertEqual([positions[3]], pattern[7])
        self.assertEqual([positions[0]], pattern[8])
        self.assertEqual([positions[2]], pattern[9])
        self.assertEqual([positions[0]], pattern[10])
        self.assertEqual([positions[1]], pattern[11])
        self.assertEqual([positions[0]], pattern[12])

    def test_length_of_one_returns_bass_note(self):
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.alternating_bass_asc_and_desc_top_strings(chord, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestSteppedAsc(TestCase):
    def test_notes_are_played_in_stepped_sequence(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_asc(scale)

        self.assertEqual(8, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[1]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[2]], pattern[4])
        self.assertEqual([positions[4]], pattern[5])
        self.assertEqual([positions[3]], pattern[6])
        self.assertEqual([positions[5]], pattern[7])

    def test_can_set_step_size(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_asc(scale, step=3)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[1]], pattern[2])
        self.assertEqual([positions[4]], pattern[3])
        self.assertEqual([positions[2]], pattern[4])
        self.assertEqual([positions[5]], pattern[5])

    def test_pattern_can_be_shortened(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_asc(scale, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[1]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])

    def test_can_set_step_size_and_shorten(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_asc(scale, step=3, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[1]], pattern[2])
        self.assertEqual([positions[4]], pattern[3])

    def test_last_notes_are_repeated_for_lengthened_sequence(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_asc(scale, length=10)

        self.assertEqual(10, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[1]], pattern[2])
        self.assertEqual([positions[3]], pattern[3])
        self.assertEqual([positions[2]], pattern[4])
        self.assertEqual([positions[4]], pattern[5])
        self.assertEqual([positions[3]], pattern[6])
        self.assertEqual([positions[5]], pattern[7])
        self.assertEqual([positions[3]], pattern[8])
        self.assertEqual([positions[5]], pattern[9])

    def test_can_set_step_size_and_lengthen(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_asc(scale, step=3, length=8)

        self.assertEqual(8, len(pattern))
        self.assertEqual([positions[0]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[1]], pattern[2])
        self.assertEqual([positions[4]], pattern[3])
        self.assertEqual([positions[2]], pattern[4])
        self.assertEqual([positions[5]], pattern[5])
        self.assertEqual([positions[2]], pattern[6])
        self.assertEqual([positions[5]], pattern[7])

    def test_length_of_one_returns_single_note(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_asc(scale, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[0]], pattern[0])


class TestSteppedDesc(TestCase):
    def test_notes_are_played_in_stepped_sequence(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_desc(scale)

        self.assertEqual(8, len(pattern))
        self.assertEqual([positions[5]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[4]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[3]], pattern[4])
        self.assertEqual([positions[1]], pattern[5])
        self.assertEqual([positions[2]], pattern[6])
        self.assertEqual([positions[0]], pattern[7])

    def test_can_set_step_size(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_desc(scale, step=3)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[5]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[4]], pattern[2])
        self.assertEqual([positions[1]], pattern[3])
        self.assertEqual([positions[3]], pattern[4])
        self.assertEqual([positions[0]], pattern[5])

    def test_pattern_can_be_shortened(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_desc(scale, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[5]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[4]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])

    def test_can_set_step_size_and_shorten(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_desc(scale, step=3, length=4)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[5]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[4]], pattern[2])
        self.assertEqual([positions[1]], pattern[3])

    def test_last_notes_are_repeated_for_lengthened_sequence(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_desc(scale, length=10)

        self.assertEqual(10, len(pattern))
        self.assertEqual([positions[5]], pattern[0])
        self.assertEqual([positions[3]], pattern[1])
        self.assertEqual([positions[4]], pattern[2])
        self.assertEqual([positions[2]], pattern[3])
        self.assertEqual([positions[3]], pattern[4])
        self.assertEqual([positions[1]], pattern[5])
        self.assertEqual([positions[2]], pattern[6])
        self.assertEqual([positions[0]], pattern[7])
        self.assertEqual([positions[2]], pattern[8])
        self.assertEqual([positions[0]], pattern[9])

    def test_can_set_step_size_and_lengthen(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_desc(scale, step=3, length=8)

        self.assertEqual(8, len(pattern))
        self.assertEqual([positions[5]], pattern[0])
        self.assertEqual([positions[2]], pattern[1])
        self.assertEqual([positions[4]], pattern[2])
        self.assertEqual([positions[1]], pattern[3])
        self.assertEqual([positions[3]], pattern[4])
        self.assertEqual([positions[0]], pattern[5])
        self.assertEqual([positions[3]], pattern[6])
        self.assertEqual([positions[0]], pattern[7])

    def test_length_of_one_returns_single_note(self):
        scale, positions = get_scale_and_positions()

        pattern = pickpatterns.stepped_desc(scale, length=1)

        self.assertEqual(1, len(pattern))
        self.assertEqual([positions[5]], pattern[0])


class TestRandomly(TestCase):
    def test_notes_are_returned_in_a_random_order(self):
        random.seed(20)
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.randomly(shape=chord)

        self.assertEqual(4, len(pattern))
        self.assertEqual([positions[2]], pattern[0])
        self.assertEqual([positions[0]], pattern[1])
        self.assertEqual([positions[3]], pattern[2])
        self.assertEqual([positions[1]], pattern[3])

    def test_can_set_length_to_shorten_pattern(self):
        random.seed(20)
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.randomly(shape=chord, length=2)

        self.assertEqual(2, len(pattern))
        self.assertEqual([positions[2]], pattern[0])
        self.assertEqual([positions[0]], pattern[1])

    def test_can_lengthen_pattern(self):
        random.seed(20)
        chord, positions = get_chord_and_positions()

        pattern = pickpatterns.randomly(shape=chord, length=6)

        self.assertEqual(6, len(pattern))
        self.assertEqual([positions[2]], pattern[0])
        self.assertEqual([positions[0]], pattern[1])
        self.assertEqual([positions[3]], pattern[2])
        self.assertEqual([positions[1]], pattern[3])
        self.assertEqual([positions[3]], pattern[2])
        self.assertEqual([positions[1]], pattern[3])


class TestBassAndRandomly(TestCase):
    pass


class TestAlternatingBassAndRandomly(TestCase):
    pass


class TestEachRandomly(TestCase):
    pass


class TestBassAndEachRandomly(TestCase):
    pass


class TestAlternatingBassAndEachRandomly(TestCase):
    pass


class TestRepeatEachPosition(TestCase):
    def test_repeat_each_position_repeats_each_item_twice_by_default(self):
        scale, positions = get_scale_and_positions()

        result = pickpatterns.repeat_each_position(scale)

        expected_sequence = [
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
            [FretPosition(fret=5, string=5, finger=None)],
            [FretPosition(fret=5, string=5, finger=None)],
            [FretPosition(fret=3, string=4, finger=None)],
            [FretPosition(fret=3, string=4, finger=None)],
            [FretPosition(fret=5, string=4, finger=None)],
            [FretPosition(fret=5, string=4, finger=None)]
        ]

        self.assertEqual(expected_sequence, result)

    def test_can_set_number_of_repeats(self):
        scale, positions = get_scale_and_positions()

        result = pickpatterns.repeat_each_position(scale, repeats=3)

        expected_sequence = [
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
            [FretPosition(fret=5, string=5, finger=None)],
            [FretPosition(fret=5, string=5, finger=None)],
            [FretPosition(fret=5, string=5, finger=None)],
            [FretPosition(fret=3, string=4, finger=None)],
            [FretPosition(fret=3, string=4, finger=None)],
            [FretPosition(fret=3, string=4, finger=None)],
            [FretPosition(fret=5, string=4, finger=None)],
            [FretPosition(fret=5, string=4, finger=None)],
            [FretPosition(fret=5, string=4, finger=None)]
        ]

        self.assertEqual(expected_sequence, result)

    def test_can_set_length_to_multiple_of_repeats(self):
        scale, positions = get_scale_and_positions()

        result = pickpatterns.repeat_each_position(scale, repeats=3, length=6)

        expected_sequence = [
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
        ]

        self.assertEqual(6, len(result))
        self.assertEqual(expected_sequence, result)

    def test_can_set_length_to_not_a_multiple_of_repeats(self):
        scale, positions = get_scale_and_positions()

        result = pickpatterns.repeat_each_position(scale, repeats=3, length=8)

        expected_sequence = [
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
        ]

        self.assertEqual(8, len(result))
        self.assertEqual(expected_sequence, result)

    def test_can_set_order_to_another_pickpattern(self):
        scale, positions = get_scale_and_positions()

        result = pickpatterns.repeat_each_position(scale, order=pickpatterns.desc)

        expected_sequence = [
            [FretPosition(fret=5, string=4, finger=None)],
            [FretPosition(fret=5, string=4, finger=None)],
            [FretPosition(fret=3, string=4, finger=None)],
            [FretPosition(fret=3, string=4, finger=None)],
            [FretPosition(fret=5, string=5, finger=None)],
            [FretPosition(fret=5, string=5, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
            [FretPosition(fret=3, string=5, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=6, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
            [FretPosition(fret=3, string=6, finger=None)],
        ]

        self.assertEqual(expected_sequence, result)
