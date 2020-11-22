from unittest import TestCase

from guitarpractice import pickpatterns
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
            Note(order=0, position=positions[0], duration=duration, elapsed_beats=Beat(1)),
            Note(order=1, position=positions[1], duration=duration, elapsed_beats=Beat(2)),
            Note(order=2, position=positions[2], duration=duration, elapsed_beats=Beat(3)),
            Note(order=3, position=positions[3], duration=duration, elapsed_beats=Beat(4)),
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
            Note(order=0, position=positions_1[0], duration=duration, elapsed_beats=Beat(1)),
            Note(order=1, position=positions_1[1], duration=duration, elapsed_beats=Beat(2)),
            Note(order=2, position=positions_2[0], duration=duration, elapsed_beats=Beat(3)),
            Note(order=3, position=positions_2[1], duration=duration, elapsed_beats=Beat(4)),
        ]

        self.assertEqual(expected_notes, sequence.notes)
        self.assertEqual([shape_1, shape_2], sequence.shapes)

    def test_can_set_rhythm_for_sequence(self):
        rhythm = [
            Beat(duration=1, division=4),
            Beat(duration=1, division=2),
            Beat(duration=1, division=4),
        ]

        positions = [
            FretPosition(string=1, fret=1),
            FretPosition(string=1, fret=2),
            FretPosition(string=1, fret=3),
        ]
        shape = GuitarShape(name='shape1', positions=positions, category='scale')

        sequence = make_sequence([shape], rhythm=rhythm)

        expected_notes = [
            Note(order=0, position=positions[0], duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=positions[1], duration=Beat(1, 2), elapsed_beats=Beat(3, 4)),
            Note(order=2, position=positions[2], duration=Beat(1, 4), elapsed_beats=Beat(4, 4)),
        ]
        self.assertEqual(expected_notes, sequence.notes)
        self.assertEqual([shape], sequence.shapes)

    def test_rests_are_added_to_incomplete_bars_at_the_end(self):
        rhythm = [
            Beat(duration=1, division=1),
            Beat(duration=1, division=4),
        ]

        positions = [
            FretPosition(string=1, fret=1),
            FretPosition(string=1, fret=2),
        ]
        shape = GuitarShape(name='shape1', positions=positions, category='scale')

        sequence = make_sequence([shape], rhythm=rhythm)

        expected_notes = [
            Note(order=0, position=positions[0], duration=Beat(1, 1), elapsed_beats=Beat(1, 1)),
            Note(order=1, position=positions[1], duration=Beat(1, 4), elapsed_beats=Beat(5, 4)),
            Note(order=2, position=None, duration=Beat(3, 4, rest=True), elapsed_beats=Beat(2, 1)),
        ]
        self.assertEqual(expected_notes, sequence.notes)
        self.assertEqual([shape], sequence.shapes)

    def test_can_apply_a_single_shape_shifter(self):
        self.fail('write the test')

    def test_can_apply_multiple_shape_shifters(self):
        self.fail('write the test')

    def test_shapes_are_not_duplicated(self):
        positions = [
            FretPosition(fret=0, string=6)
        ]

        shape_1 = GuitarShape('open string', 'note', positions=positions)
        shape_2 = GuitarShape('open string', 'note', positions=positions)

        sequence = make_sequence(shapes=[shape_1, shape_2])

        self.assertEqual(len(sequence.shapes), 1)
        self.assertEqual(sequence.shapes[0], shape_1)
        self.assertEqual(sequence.shapes[0], shape_2)

    def test_show_shape_labels_sets_shape_labels_to_true(self):
        positions = [
            FretPosition(fret=0, string=6)
        ]

        shape = GuitarShape('open string', 'note', positions=positions)

        sequence = make_sequence(shapes=[shape], shape_labels=True)

        self.assertTrue(sequence.shape_labels)


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
    def test_order_increases_based_on_rhythm(self):
        rhythm = [
            Beat(duration=1),
            Beat(duration=1),
            Beat(duration=1),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=4)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(4, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), order=0, elapsed_beats=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), order=1, elapsed_beats=Beat(2)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1), order=2, elapsed_beats=Beat(3)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), order=3, elapsed_beats=Beat(4)), notes[3])

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
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(4), order=0, elapsed_beats=Beat(4)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), order=1, elapsed_beats=Beat(5)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1), order=2, elapsed_beats=Beat(6)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), order=3, elapsed_beats=Beat(7)), notes[3])

    def test_can_can_apply_two_beats(self):
        rhythm = [
            Beat(duration=2),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=2)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(2, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(2), order=0, elapsed_beats=Beat(2)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), order=1, elapsed_beats=Beat(3)), notes[1])

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
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1, 2), order=0, elapsed_beats=Beat(1, 2)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), order=1, elapsed_beats=Beat(3, 4)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1, 2), order=2, elapsed_beats=Beat(5, 4)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), order=3, elapsed_beats=Beat(6, 4)), notes[3])

    def test_can_apply_triplets(self):
        rhythm = [
            Beat(duration=1, division=12),
            Beat(duration=1, division=12),
            Beat(duration=1, division=12),
            Beat(duration=1),
            Beat(duration=1, division=12),
            Beat(duration=2, division=12),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=7)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(7, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1, 12), order=0, elapsed_beats=Beat(1, 12)),
                         notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1, 12), order=1, elapsed_beats=Beat(2, 12)),
                         notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1, 12), order=2, elapsed_beats=Beat(3, 12)),
                         notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), order=3, elapsed_beats=Beat(2, 4)), notes[3])
        self.assertEqual(Note(position=pattern[4][0], duration=Beat(1, 12), order=4, elapsed_beats=Beat(7, 12)),
                         notes[4])
        self.assertEqual(Note(position=pattern[5][0], duration=Beat(2, 12), order=5, elapsed_beats=Beat(3, 4)),
                         notes[5])
        self.assertEqual(Note(position=pattern[6][0], duration=Beat(1), order=6, elapsed_beats=Beat(4)), notes[6])

    def test_can_apply_sixteenth_notes(self):
        rhythm = [
            Beat(duration=1, division=16),
            Beat(duration=1, division=16),
            Beat(duration=1, division=16),
            Beat(duration=1, division=16),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=5)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(5, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1, 16), order=0, elapsed_beats=Beat(1, 16)),
                         notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1, 16), order=1, elapsed_beats=Beat(2, 16)),
                         notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1, 16), order=2, elapsed_beats=Beat(3, 16)),
                         notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1, 16), order=3, elapsed_beats=Beat(4, 16)),
                         notes[3])
        self.assertEqual(Note(position=pattern[4][0], duration=Beat(1), order=4, elapsed_beats=Beat(2, 4)), notes[4])

    def test_rest_beats_are_added_to_sequence_and_ignored_by_pick_pattern(self):
        rhythm = [
            Beat(duration=1),
            Beat(duration=1, rest=True),
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=2)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(3, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), order=0, elapsed_beats=Beat(1)), notes[0])
        self.assertEqual(Note(position=None, duration=Beat(1, rest=True), order=1, elapsed_beats=Beat(2)), notes[1])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), order=2, elapsed_beats=Beat(3)), notes[2])

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
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), order=0, elapsed_beats=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[0][1], duration=Beat(1), order=0, elapsed_beats=Beat(1)), notes[1])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), order=1, elapsed_beats=Beat(2)), notes[2])

    def test_rhythm_is_repeated_when_shorter_than_pattern(self):
        rhythm = [
            Beat(duration=1),
        ]
        pattern = make_single_position_pattern(length=4)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(4, len(notes))
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), order=0, elapsed_beats=Beat(1)), notes[0])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), order=1, elapsed_beats=Beat(2)), notes[1])
        self.assertEqual(Note(position=pattern[2][0], duration=Beat(1), order=2, elapsed_beats=Beat(3)), notes[2])
        self.assertEqual(Note(position=pattern[3][0], duration=Beat(1), order=3, elapsed_beats=Beat(4)), notes[3])

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
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), order=0, elapsed_beats=Beat(1)), notes[0])

    def test_single_rest_returned_if_all_beats_are_rests(self):
        rhythm = [
            Beat(duration=1, rest=True),
            Beat(duration=1000, rest=True),
            Beat(duration=1, rest=True),
        ]

        pattern = make_single_position_pattern(length=4)

        notes = apply_rhythm(pattern, rhythm)

        self.assertEqual(1, len(notes))
        self.assertEqual(Note(position=None, duration=Beat(4, rest=True), order=0, elapsed_beats=Beat(4)), notes[0])

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
        self.assertEqual(Note(position=pattern[0][0], duration=Beat(1), order=0, elapsed_beats=Beat(1)), notes[0])
        self.assertEqual(Note(position=None, duration=Beat(1, rest=True), order=1, elapsed_beats=Beat(2)), notes[1])
        self.assertEqual(Note(position=None, duration=Beat(1, rest=True), order=2, elapsed_beats=Beat(3)), notes[2])
        self.assertEqual(Note(position=pattern[1][0], duration=Beat(1), order=3, elapsed_beats=Beat(4)), notes[3])


class TestLabelTabShapes(TestCase):
    def test_shape_name_is_added_to_annotations(self):
        positions = [
            FretPosition(0, 6),
            FretPosition(2, 5),
        ]
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', positions=positions, short_name='E5')
        ]

        sequence = make_sequence(shapes, pick_pattern=pickpatterns.strum, tab_labels=True, rhythm=[Beat(4)])

        expected_notes = [
            Note(position=positions[0], duration=Beat(4), elapsed_beats=Beat(1, 1), order=0, annotations=['label:E5']),
            Note(position=positions[1], duration=Beat(4), elapsed_beats=Beat(1, 1), order=0, annotations=['label:E5']),
        ]

        self.assertEqual(expected_notes, sequence.notes)
        self.assertEqual(shapes, sequence.shapes)

    def test_repeated_shapes_are_not_labeled(self):
        positions = [
            FretPosition(0, 6),
            FretPosition(2, 5),
        ]
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', positions=positions, short_name='E5'),
            GuitarShape(category='chord', name='E5 Power Chord', positions=positions, short_name='E5'),
        ]

        result = make_sequence(shapes, pick_pattern=pickpatterns.strum, tab_labels=True, rhythm=[Beat(2)])

        expected = [
            Note(position=positions[0], duration=Beat(2), elapsed_beats=Beat(1, 2), order=0, annotations=['label:E5']),
            Note(position=positions[1], duration=Beat(2), elapsed_beats=Beat(1, 2), order=0, annotations=['label:E5']),
            Note(position=positions[0], duration=Beat(2), elapsed_beats=Beat(1, 1), order=1),
            Note(position=positions[1], duration=Beat(2), elapsed_beats=Beat(1, 1), order=1),
        ]

        self.assertEqual(expected, result.notes)

    def test_chord_changes_are_labeled(self):
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', short_name='E5', positions=[
                FretPosition(0, 6),
                FretPosition(2, 5),
            ]),
            GuitarShape(category='chord', name='F5 Power Chord', short_name='F5', positions=[
                FretPosition(1, 6),
                FretPosition(3, 5),
            ]),
        ]

        result = make_sequence(shapes, pick_pattern=pickpatterns.strum, tab_labels=True, rhythm=[Beat(2)])

        expected = [
            Note(position=shapes[0].positions[0], duration=Beat(2), elapsed_beats=Beat(1, 2), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[0].positions[1], duration=Beat(2), elapsed_beats=Beat(1, 2), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[1].positions[0], duration=Beat(2), elapsed_beats=Beat(1, 1), order=1,
                 annotations=['label:F5']),
            Note(position=shapes[1].positions[1], duration=Beat(2), elapsed_beats=Beat(1, 1), order=1,
                 annotations=['label:F5']),
        ]

        self.assertEqual(expected, result.notes)

    def test_repeated_chords_are_labelled_after_chord_change(self):
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', short_name='E5', positions=[
                FretPosition(0, 6),
                FretPosition(2, 5),
            ]),
            GuitarShape(category='chord', name='F5 Power Chord', short_name='F5', positions=[
                FretPosition(1, 6),
                FretPosition(3, 5),
            ]),
            GuitarShape(category='chord', name='E5 Power Chord', short_name='E5', positions=[
                FretPosition(0, 6),
                FretPosition(2, 5),
            ]),
        ]
        rhythm = [Beat(1), Beat(1), Beat(2)]

        result = make_sequence(shapes, pick_pattern=pickpatterns.strum, tab_labels=True, rhythm=rhythm)

        expected = [
            Note(position=shapes[0].positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[0].positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[1].positions[0], duration=Beat(1), elapsed_beats=Beat(1, 2), order=1,
                 annotations=['label:F5']),
            Note(position=shapes[1].positions[1], duration=Beat(1), elapsed_beats=Beat(1, 2), order=1,
                 annotations=['label:F5']),
            Note(position=shapes[0].positions[0], duration=Beat(2), elapsed_beats=Beat(1, 1), order=2,
                 annotations=['label:E5']),
            Note(position=shapes[0].positions[1], duration=Beat(2), elapsed_beats=Beat(1, 1), order=2,
                 annotations=['label:E5']),
        ]

        self.assertEqual(expected, result.notes)

    def test_shape_name_is_not_added_if_short_name_is_none(self):
        positions = [
            FretPosition(0, 6),
            FretPosition(2, 5),
        ]
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', positions=positions)
        ]

        result = make_sequence(shapes, pick_pattern=pickpatterns.strum, tab_labels=True, rhythm=[Beat(4)])

        expected = [
            Note(position=positions[0], duration=Beat(4), elapsed_beats=Beat(1, 1), order=0),
            Note(position=positions[1], duration=Beat(4), elapsed_beats=Beat(1, 1), order=0),
        ]

        self.assertEqual(expected, result.notes)

    def test_rests_are_ignored_when_labelling(self):
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', short_name='E5', positions=[
                FretPosition(0, 6),
                FretPosition(2, 5),
            ]),
            GuitarShape(category='chord', name='F5 Power Chord', short_name='F5', positions=[
                FretPosition(1, 6),
                FretPosition(3, 5),
            ]),
        ]

        rhythm = [Beat(2), Beat(1, rest=True), Beat(1)]

        result = make_sequence(shapes, pick_pattern=pickpatterns.strum, tab_labels=True, rhythm=rhythm)

        expected = [
            Note(position=shapes[0].positions[0], duration=Beat(2), elapsed_beats=Beat(1, 2), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[0].positions[1], duration=Beat(2), elapsed_beats=Beat(1, 2), order=0,
                 annotations=['label:E5']),
            Note(position=None, duration=Beat(1, rest=True), elapsed_beats=Beat(3), order=1),
            Note(position=shapes[1].positions[0], duration=Beat(1), elapsed_beats=Beat(1, 1), order=2,
                 annotations=['label:F5']),
            Note(position=shapes[1].positions[1], duration=Beat(1), elapsed_beats=Beat(1, 1), order=2,
                 annotations=['label:F5']),
        ]

        self.assertEqual(expected, result.notes)

    def test_can_label_arpeggios(self):
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', short_name='E5', positions=[
                FretPosition(0, 6),
                FretPosition(2, 5),
            ]),
            GuitarShape(category='chord', name='F5 Power Chord', short_name='F5', positions=[
                FretPosition(1, 6),
                FretPosition(3, 5),
            ]),
        ]

        result = make_sequence(shapes, tab_labels=True, rhythm=[Beat(1)])

        expected = [
            Note(position=shapes[0].positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[0].positions[1], duration=Beat(1), elapsed_beats=Beat(1, 2), order=1),
            Note(position=shapes[1].positions[0], duration=Beat(1), elapsed_beats=Beat(3), order=2,
                 annotations=['label:F5']),
            Note(position=shapes[1].positions[1], duration=Beat(1), elapsed_beats=Beat(1, 1), order=3),
        ]

        self.assertEqual(expected, result.notes)
