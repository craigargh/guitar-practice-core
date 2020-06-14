from typing import List, Callable

from .models import GuitarShape, Sequence, Note, FretPosition


def make_sequence(
        shapes: List[GuitarShape],
        rhythm: List[float] = None,
        shape_shifters: List[Callable] = None,
        pick_patterns: List[Callable] = None
) -> Sequence:
    notes = [
        Note(start_beat=index + 1, position=position, duration=1)
        for index, position in enumerate(positions_generator(shapes))
    ]
    return Sequence(notes=notes, annotations=[], shapes=shapes)


def positions_generator(shapes: List[GuitarShape]) -> List[FretPosition]:
    for shape in shapes:
        for position in shape.positions:
            yield position
