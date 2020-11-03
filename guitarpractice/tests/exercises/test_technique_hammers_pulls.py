import random
from unittest import TestCase

from guitarpractice.exercises.technique_hammers_pulls import technique_hammers_pulls
from guitarpractice.models import Beat


class TestHammersAndPulls(TestCase):
    def test_level_one_has_eighth_notes(self):
        random.seed(10)

        result = technique_hammers_pulls(variation='level-1')

        self.assertEqual(8, len(result.notes))
        self.assertTrue(all(Beat(1, 8) == note.duration for note in result.notes))

    def test_level_two_has_eighth_notes(self):
        random.seed(10)

        result = technique_hammers_pulls(variation='level-2')

        self.assertEqual(8, len(result.notes))
        self.assertTrue(all(Beat(1, 8) == note.duration for note in result.notes))

    def test_level_two_can_have_eighteenth_notes(self):
        random.seed(3)

        result = technique_hammers_pulls(variation='level-2')

        self.assertEqual(16, len(result.notes))
        self.assertTrue(all(Beat(1, 16) == note.duration for note in result.notes))
