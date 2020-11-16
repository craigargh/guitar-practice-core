from guitarpractice.models import Sequence
from .metal_power_chords import metal_power_chords
from .pentatonic_licks import pentatonic_licks
from .rhythm_divisions import rhythm_divisions
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
                    {'id': 'level-3', 'title': 'Level 3'},
                ],
                'callable': rhythm_sixteenth_notes
            },
            'hammers-and-pulls': {
                'title': 'Hammer-ons and Pull-offs',
                'variations': [
                    {'id': 'level-1', 'title': 'Level 1'},
                    {'id': 'level-2', 'title': 'Level 2'},
                    {'id': 'level-3', 'title': 'Level 3'},
                ],
                'callable': technique_hammers_pulls
            },
            'scale-shapes': {
                'title': 'Scale Shapes',
                'variations': [
                    {'id': 'major-pentatonic', 'title': 'Major Pentatonic Scale'},
                    {'id': 'major', 'title': 'Major Scale'},
                ],
                'callable': scale_shapes
            },
            'rhythm-divisions': {
                'title': 'Rhythm Divisions',
                'variations': [
                    {'id': 'level-1', 'title': 'Level 1'},
                    {'id': 'level-2', 'title': 'Level 2'},
                    # {'id': 'level-3', 'title': 'Level 3'},
                ],
                'callable': rhythm_divisions
            },
            'pentatonic-licks': {
                'title': 'Pentatonic Licks',
                'variations': [
                    {'id': 'level-1', 'title': 'Level 1'},
                ],
                'callable': pentatonic_licks
            },
            'metal-power-chords': {
                'title': 'Metal Power Chords',
                'variations': [
                    {'id': 'level-1', 'title': 'Level 1'},
                ],
                'callable': metal_power_chords
            },
        }
    }
