from guitarpractice.models import GuitarShape
from guitarpractice.shapes.chord_collections import movable_chords, open_chords
from guitarpractice.shapes.fretboard import note_positions, get_note
from guitarpractice.shapeshifters import shift_vertically


def list_open_chords(root: str, tonality: str):
    all_chords = open_chords()
    matching_shapes = [
        chord
        for chord in all_chords
        if get_note(get_root_position(chord)) == root
        if chord.tonality == tonality
    ]

    return matching_shapes


def list_movable_chord_shapes(tonality: str):
    return [
        chord
        for chord in movable_chords()
        if chord.tonality == tonality
    ]


def list_movable_chords(root: str, tonality: str):
    note_on_each_string = {}
    for note_position in note_positions(root):
        if note_position.string in note_on_each_string.keys():
            continue

        note_on_each_string[note_position.string] = note_position

    shifted_chords = []
    for movable_chord in list_movable_chord_shapes(tonality):
        movable_root_position = get_root_position(movable_chord)
        target_root_position = note_on_each_string[movable_root_position.string]

        shift_distance = target_root_position.fret - movable_root_position.fret

        shifted_shape = shift_vertically_by_root(movable_chord, shift_distance)
        shifted_chords.append(shifted_shape)

    valid_chords = []
    for chord in shifted_chords:

        invalid = any(position.fret <= 0 for position in chord.positions)
        if invalid:
            continue

        valid_chords.append(chord)

    return valid_chords


def shift_vertically_by_root(shape: GuitarShape, root_offset: int):
    lowest_fret = min(position.fret for position in shape.positions)
    new_lowest_fret = lowest_fret + root_offset

    return shift_vertically(shape, new_lowest_fret)


def get_root_position(shape: GuitarShape):
    movable_chord_root_positions = [
        position
        for position in shape.positions
        if position.highlighted
    ]
    return movable_chord_root_positions[0]
