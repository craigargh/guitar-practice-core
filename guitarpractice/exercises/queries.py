from guitarpractice.models import Sequence
from .rhythm_sixteenth_notes import rhythm_sixteenth_notes


def list_exercises() -> dict:
    exercise_list = _exercise_map()

    for exercise in exercise_list['exercises'].values():
        del exercise['callable']

    return exercise_list


def get_exercise(exercise_type: str, variation: str) -> Sequence:
    exercise_function = _exercise_map().get('exercises').get(exercise_type).get('callable')
    return exercise_function(variation)


def _exercise_map():
    return {
        'exercises': {
            'rhythm-16th-notes': {
                'title': 'Rhythm 16th Notes',
                'variations': {
                    'id': 'level-1',
                    'title': 'Level 1'
                },
                'callable': rhythm_sixteenth_notes
            }
        }
    }
