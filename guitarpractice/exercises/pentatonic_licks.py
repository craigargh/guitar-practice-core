import random

from guitarpractice.models import Sequence, GuitarShape
from guitarpractice.shapes.basic_pentatonic_licks import basic_pentatonic_licks


def pentatonic_licks(variation: str = None) -> Sequence:
    variation_map = {
        'level-1': level_one,
        # 'level-2': level_two,
        # 'level-3': level_three,
    }
    variation_function = variation_map[variation]

    return variation_function()


def level_one() -> Sequence:
    lick = random.choice(basic_pentatonic_licks())

    positions = [note.position for note in lick]
    shape = GuitarShape(positions=positions, name='Pentatonic Lick', category='scale')

    return Sequence(notes=lick, shapes=[shape])
