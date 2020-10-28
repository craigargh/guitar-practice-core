import random
from unittest import TestCase

from guitarpractice.exercises.rhythm_sixteenth_notes import rhythm_sixteenth_notes
from guitarpractice.models import Beat, FretPosition


class TestRhythmSixteenthNotesLevelOne(TestCase):
    def test_sequence_has_16th_note_rhythm(self):
        random.seed(2)
        sequence = rhythm_sixteenth_notes(variation='level-1')

        sixteenth_beat = Beat(duration=1, division=16)

        self.assertEqual(16, len(sequence.notes))
        for beat in sequence.notes:
            self.assertEqual(sixteenth_beat, beat.duration)

    def test_single_fret_position_is_repeated(self):
        random.seed(2)
        sequence = rhythm_sixteenth_notes(variation='level-1')

        expected_position = FretPosition(fret=0, string=6)

        self.assertEqual(16, len(sequence.notes))
        for beat in sequence.notes:
            self.assertEqual(expected_position, beat.position)

    def test_random_string_number_is_between_1_and_6(self):
        for _ in range(1000):
            sequence = rhythm_sixteenth_notes(variation='level-1')

            self.assertLessEqual(sequence.shapes[0].positions[0].string, 6)
            self.assertGreaterEqual(sequence.shapes[0].positions[0].string, 1)

    def test_random_fret_number_is_between_0_and_12(self):
        for _ in range(1000):
            sequence = rhythm_sixteenth_notes(variation='level-1')

            self.assertLessEqual(sequence.shapes[0].positions[0].fret, 12)
            self.assertGreaterEqual(sequence.shapes[0].positions[0].fret, 0)


class TestRhythmSixteenthNotesLevelTwo(TestCase):
    def test_sequence_has_16th_note_rhythm(self):
        self.fail('Write the tests')
