from typing import List, Callable

from .models import GuitarShape, Sequence, Note, FretPosition, Beat


def make_sequence(
        shapes: List[GuitarShape],
        shape_shifters: List[Callable] = None,
        pick_pattern: Callable = None,
        rhythm: List[Beat] = None,
) -> Sequence:
    beat = Beat(duration=1)
    notes = [
        Note(start_beat=index + 1, position=position, beat=beat)
        for index, position in enumerate(positions_generator(shapes))
    ]
    return Sequence(notes=notes, shapes=shapes)


def positions_generator(shapes: List[GuitarShape]) -> List[FretPosition]:
    for shape in shapes:
        for position in shape.positions:
            yield position
