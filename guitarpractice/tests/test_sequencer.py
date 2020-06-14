from unittest import TestCase

from guitarpractice.models import FretPosition, GuitarShape, Note
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

        expected_notes = [
            Note(start_beat=1, position=positions[0], duration=1),
            Note(start_beat=2, position=positions[1], duration=1),
            Note(start_beat=3, position=positions[2], duration=1),
            Note(start_beat=4, position=positions[3], duration=1),
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

        expected_notes = [
            Note(start_beat=1, position=positions_1[0], duration=1),
            Note(start_beat=2, position=positions_1[1], duration=1),
            Note(start_beat=3, position=positions_2[0], duration=1),
            Note(start_beat=4, position=positions_2[1], duration=1),
        ]

        self.assertEqual(expected_notes, sequence.notes)
        self.assertEqual([shape_1, shape_2], sequence.shapes)
