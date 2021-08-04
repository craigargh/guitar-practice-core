from unittest import TestCase

from guitarpractice.models import FretPosition
from guitarpractice.shapes.chord import list_movable_chords


class TestListMovableChords(TestCase):
    def test_all_movable_chords_are_listed_for_note(self):
        chords = list_movable_chords('C', 'maj')

        self.assertEqual(len(chords), 5)

    def test_only_chords_with_same_tonality_are_included(self):
        chords = list_movable_chords('C', 'maj')

        self.assertEqual(chords[0].tonality, 'maj')
        self.assertEqual(chords[1].tonality, 'maj')
        self.assertEqual(chords[2].tonality, 'maj')
        self.assertEqual(chords[3].tonality, 'maj')
        self.assertEqual(chords[4].tonality, 'maj')

    def test_chord_position_is_shifted_to_match_root_note(self):
        chords = list_movable_chords('C', 'maj')

        expected_positions = [
            FretPosition(string=6, fret=8, finger=1, highlighted=True),
            FretPosition(string=5, fret=10, finger=3),
            FretPosition(string=4, fret=10, finger=4, highlighted=True),
            FretPosition(string=3, fret=9, finger=2),
            FretPosition(string=2, fret=8, finger=1),
            FretPosition(string=1, fret=8, finger=1, highlighted=True),
        ]

        self.assertEqual(expected_positions, chords[0].positions)
