from unittest import TestCase

from guitarpractice.models import FretPosition, GuitarShape, Note, Beat
from guitarpractice.sequencer import make_sequence


class TestSequencer(TestCase):
    def test_shape_is_converted_into_notes(self):
        positions = [
            FretPosition(string=1, fret=1),
            FretPosition(string=1, fret=2),
            FretPosition(string=1, fret=3),
            FretPosition(string=1, fret=4),
        ]
        shape = GuitarShape(name='shape1', positions=positions, category='scale')

        sequence = make_sequence([shape])

        duration = Beat(duration=1)
        expected_notes = [
            Note(start_beat=Beat(duration=1), position=positions[0], duration=duration),
            Note(start_beat=Beat(duration=2), position=positions[1], duration=duration),
            Note(start_beat=Beat(duration=3), position=positions[2], duration=duration),
            Note(start_beat=Beat(duration=4), position=positions[3], duration=duration),
        ]
        self.assertEqual(expected_notes, sequence.notes)
        self.assertEqual([shape], sequence.shapes)

    def test_multiple_shapes_are_combined_into_a_sequence(self):
        positions_1 = [
            FretPosition(string=1, fret=1),
            FretPosition(string=1, fret=2),
        ]
        shape_1 = GuitarShape(name='shape1', positions=positions_1, category='scale')

        positions_2 = [
            FretPosition(string=2, fret=1),
            FretPosition(string=2, fret=2),
        ]
        shape_2 = GuitarShape(name='shape2', positions=positions_2, category='scale')

        sequence = make_sequence([shape_1, shape_2])

        duration = Beat(duration=1)
        expected_notes = [
            Note(start_beat=Beat(duration=1), position=positions_1[0], duration=duration),
            Note(start_beat=Beat(duration=2), position=positions_1[1], duration=duration),
            Note(start_beat=Beat(duration=3), position=positions_2[0], duration=duration),
            Note(start_beat=Beat(duration=4), position=positions_2[1], duration=duration),
        ]

        self.assertEqual(expected_notes, sequence.notes)
        self.assertEqual([shape_1, shape_2], sequence.shapes)

    def test_can_set_rhythm_for_sequence(self):
        self.fail('Write the test')


class TestApplyRhythm(TestCase):
    def test_start_beat_increases_based_on_rhythm(self):
        self.fail('Write the test')

    def test_can_apply_half_notes(self):
        self.fail('Write the test')

    def test_can_apply_triplets(self):
        self.fail('Write the test')

    def test_can_apply_sixteenth_notes(self):
        self.fail('Write the test')

    def test_rest_beats_are_added_to_sequence_and_ignored_by_pick_pattern(self):
        self.fail('Write the test')

    def test_rest_beat_is_added_to_end_of_sequence_if_bar_not_full(self):
        pass
