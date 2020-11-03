from guitarpractice.models import Sequence
from .rhythm_sixteenth_notes import rhythm_sixteenth_notes
from .scale_shapes import scale_shapes
from .technique_hammers_pulls import technique_hammers_pulls


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
                'variations': [
                    {'id': 'level-1', 'title': 'Level 1'},
                    {'id': 'level-2', 'title': 'Level 2'},
                ],
                'callable': rhythm_sixteenth_notes
            },
            'scale-shapes': {
                'title': 'Scale Shapes',
                'variations': [
                    {'id': 'c-major-pentatonic', 'title': 'C Major Pentatonic'},
                    {'id': 'c-major', 'title': 'C Major'},
                ],
                'callable': scale_shapes
            },
            'hammers-and-pulls': {
                'title': 'Hammer-ons and Pull-offs',
                'variations': [
                    {'id': 'level-one', 'title': 'Level 1'},
                    {'id': 'level-two', 'title': 'Level 2'},
                ],
                'callable': technique_hammers_pulls
            }
        }
    }


"""
Exercise ideas:
- 16th notes
- Gallops and reverse gallops
- Power chords
"""