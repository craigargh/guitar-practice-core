from guitarpractice.models import GuitarShape, FretPosition


def shift_vertically(shape: GuitarShape, lowest_fret: int) -> GuitarShape:
    current_lowest_fret = min(
        position.fret
        for position in shape.positions
    )
    frets_to_move = lowest_fret - current_lowest_fret

    new_positions = []

    for position in shape.positions:
        new_fret = position.fret + frets_to_move

        new_position = FretPosition(
            fret=new_fret,
            string=position.string,
            highlighted=position.highlighted,
            finger=position.finger,
        )
        new_positions.append(new_position)

    shape.positions = new_positions
    return shape
