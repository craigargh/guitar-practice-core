from unittest import TestCase

from guitarpractice.exercises import list_exercises, get_exercise
from guitarpractice.models import Sequence


class TestListExercises(TestCase):
    def test_list_of_exercises_is_returned(self):
        result = list_exercises()

        expected = {
            'exercises': {
                'rhythm-16th-notes': {
                    'title': 'Rhythm 16th Notes',
                    'variations': [
                        {'id': 'level-1', 'title': 'Level 1'},
                        {'id': 'level-2', 'title': 'Level 2'},
                    ],
                },
                'scale-shapes': {
                    'title': 'Scale Shapes',
                    'variations': [
                        {'id': 'c-major-pentatonic', 'title': 'C Major Pentatonic'},
                        {'id': 'c-major', 'title': 'C Major'}
                    ]
                },
                'hammers-and-pulls': {
                    'title': 'Hammer-ons and Pull-offs',
                    'variations': [
                        {'id': 'level-one', 'title': 'Level 1'},
                    ],
                }
            }
        }

        self.assertEqual(expected, result)


class TestGetExercise(TestCase):
    def test_get_rhythm_16_notes_level_1_exercise_returns_sequence(self):
        result = get_exercise('rhythm-16th-notes', 'level-1')

        self.assertEqual(Sequence, type(result))

    def test_get_rhythm_16_notes_level_2_exercise_returns_sequence(self):
        result = get_exercise('rhythm-16th-notes', 'level-2')

        self.assertEqual(Sequence, type(result))
