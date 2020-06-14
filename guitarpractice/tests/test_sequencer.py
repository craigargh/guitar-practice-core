from unittest import TestCase

from guitarpractice.models import FretPosition, GuitarShape, Note, Beat
from guitarpractice.sequencer import make_sequence, apply_rhythm


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
        rhythm = [
            Beat(duration=1, division=1),
            Beat(duration=1, division=2),
            Beat(duration=1, division=2),
            Beat(duration=1, division=1),
        ]

        positions = [
            FretPosition(string=1, fret=1),
            FretPosition(string=1, fret=2),
            FretPosition(string=1, fret=3),
            FretPosition(string=1, fret=4),
        ]
        shape = GuitarShape(name='shape1', positions=positions, category='scale')

        sequence = make_sequence([shape], rhythm=rhythm)

        expected_notes = [
            Note(start_beat=Beat(1), position=positions[0], duration=Beat(1)),
            Note(start_beat=Beat(2), position=positions[1], duration=Beat(1, 2)),
            Note(start_beat=Beat(5, 2), position=positions[2], duration=Beat(1, 2)),
            Note(start_beat=Beat(3, 1), position=positions[3], duration=Beat(1)),
        ]
        self.assertEqual(expected_notes, sequence.notes)
        self.assertEqual([shape], sequence.shapes)


def make_single_position_pattern(length: int):
    pattern = [
        [FretPosition(string=6, fret=3)],
        [FretPosition(string=6, fret=5)],
        [FretPosition(string=5, fret=2)],
        [FretPosition(string=5, fret=3)],
        [FretPosition(string=5, fret=5)],
        [FretPosition(string=4, fret=2)],
        [FretPosition(string=4, fret=4)],
        [FretPosition(string=4, fret=5)],
    ]
    return pattern[:length]


class TestApplyRhythm(TestCase):
    def test_start_beat_increases_based_on_rhythm(self):
        rhythm = [
            Beat(duration=1),
            Beat(duration=1),
            Beat(duration=1),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=4)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(4, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), start_beat=Beat(2)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1), start_beat=Beat(3)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), start_beat=Beat(4)), notes[3])

    def test_can_apply_four_beats(self):
        rhythm = [
            Beat(duration=4),
            Beat(duration=1),
            Beat(duration=1),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=4)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(4, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(4), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), start_beat=Beat(5)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1), start_beat=Beat(6)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), start_beat=Beat(7)), notes[3])

    def test_can_can_apply_two_beats(self):
        rhythm = [
            Beat(duration=2),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=2)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(2, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(2), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), start_beat=Beat(3)), notes[1])

    def test_can_apply_half_beats(self):
        rhythm = [
            Beat(duration=1, division=2),
            Beat(duration=1),
            Beat(duration=1, division=2),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=4)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(4, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1, 2), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), start_beat=Beat(3, 2)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1, 2), start_beat=Beat(5, 2)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), start_beat=Beat(3)), notes[3])

    def test_can_apply_triplets(self):
        rhythm = [
            Beat(duration=1, division=3),
            Beat(duration=1, division=3),
            Beat(duration=1, division=3),
            Beat(duration=1),
            Beat(duration=1, division=3),
            Beat(duration=2, division=3),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=7)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(7, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1, 3), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1, 3), start_beat=Beat(4, 3)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1, 3), start_beat=Beat(5, 3)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), start_beat=Beat(2)), notes[3])
        self.assertEqual(Note(position=pattern[4][0], duration=Beat(1, 3), start_beat=Beat(3)), notes[4])
        self.assertEqual(Note(position=pattern[5][0], duration=Beat(2, 3), start_beat=Beat(10, 3)), notes[5])
        self.assertEqual(Note(position=pattern[6][0], duration=Beat(1), start_beat=Beat(4)), notes[6])

    def test_can_apply_sixteenth_notes(self):
        rhythm = [
            Beat(duration=1, division=4),
            Beat(duration=1, division=4),
            Beat(duration=1, division=4),
            Beat(duration=1, division=4),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=5)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(5, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1, 4), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1, 4), start_beat=Beat(5, 4)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1, 4), start_beat=Beat(3, 2)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1, 4), start_beat=Beat(7, 4)), notes[3])
        self.assertEqual(Note(position=pattern[4][0], duration=Beat(1), start_beat=Beat(2)), notes[4])

    def test_rest_beats_are_added_to_sequence_and_ignored_by_pick_pattern(self):
        rhythm = [
            Beat(duration=1),
            Beat(duration=1, rest=True),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=2)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(3, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=None, duration=Beat(1, rest=True), start_beat=Beat(2)), notes[1])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), start_beat=Beat(3)), notes[2])

    def test_can_apply_rhythm_to_chords_and_individual_notes(self):
        pattern = [
            [
                FretPosition(string=6, fret=1),
                FretPosition(string=5, fret=3),
            ],
            [FretPosition(string=6, fret=0)],
        ]

        rhythm = [
            Beat(duration=1),
            Beat(duration=1),
        ]

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(3, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[0][1], duration=Beat(1), start_beat=Beat(1)), notes[1])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), start_beat=Beat(2)), notes[2])

    def test_rhythm_is_repeated_when_shorter_than_pattern(self):
        rhythm = [
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=4)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(4, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), start_beat=Beat(2)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1), start_beat=Beat(3)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), start_beat=Beat(4)), notes[3])

    def test_rhythm_is_shortened_when_longer_than_pattern(self):
        rhythm = [
            Beat(duration=1),
            Beat(duration=1),
            Beat(duration=1),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=1)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(1, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), start_beat=Beat(1)), notes[0])

    def test_single_rest_returned_if_all_beats_are_rests(self):
        rhythm = [
            Beat(duration=1, rest=True),
            Beat(duration=1000, rest=True),
            Beat(duration=1, rest=True),
        ]

        pattern = make_single_position_pattern(length=4)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(1, len(notes))
        self.assertEqual(Note(position=None, duration=Beat(4, rest=True), start_beat=Beat(1)), notes[0])

    def test_can_handle_multiple_rests_in_sequence(self):
        rhythm = [
            Beat(duration=1),
            Beat(duration=1, rest=True),
            Beat(duration=1, rest=True),
            Beat(duration=1),
        ]

        pattern = make_single_position_pattern(length=2)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(4, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), start_beat=Beat(1)), notes[0])
        self.assertEqual(Note(position=None, duration=Beat(1, rest=True), start_beat=Beat(2)), notes[1])
        self.assertEqual(Note(position=None, duration=Beat(1, rest=True), start_beat=Beat(3)), notes[2])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), start_beat=Beat(4)), notes[3])
