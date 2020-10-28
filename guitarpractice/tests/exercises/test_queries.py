from unittest import TestCase

from guitarpractice.exercises import list_exercises, get_exercise
from guitarpractice.models import Sequence


class TestListExercises(TestCase):
    def test_list_of_exercises_is_returned(self):
        result = list_exercises()

        expected = {
            'exercises': {
                'rhythm-16th-notes': {
                    'variations': {
                        'level-1': 'Level 1'
                    },
                }
            }
        }

        self.assertEqual(expected, result)


class TestGetExercise(TestCase):
    def test_get_rhythm_16_notes_level_1_exercise_returns_sequence(self):
        result = get_exercise('rhythm-16th-notes', 'level-1')

        self.assertEqual(Sequence, type(result))
