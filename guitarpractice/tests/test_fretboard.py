from unittest import TestCase

from guitarpractice.models import FretPosition
from guitarpractice.shapes.fretboard import make_fretboard, Tuning, get_note, note_positions


class TestFretboard(TestCase):
    def test_root_notes_are_set_for_each_string(self):
        fretboard = make_fretboard(Tuning('E', 'standard'))

        self.assertEqual('E', fretboard[6][0])
        self.assertEqual('A', fretboard[5][0])
        self.assertEqual('D', fretboard[4][0])
        self.assertEqual('G', fretboard[3][0])
        self.assertEqual('B', fretboard[2][0])
        self.assertEqual('E', fretboard[1][0])

    def test_sixth_string_notes_are_set(self):
        fretboard = make_fretboard(Tuning('E', 'standard'))

        self.assertEqual('E', fretboard[6][0])
        self.assertEqual('F', fretboard[6][1])
        self.assertEqual('F#', fretboard[6][2])
        self.assertEqual('G', fretboard[6][3])
        self.assertEqual('G#', fretboard[6][4])
        self.assertEqual('A', fretboard[6][5])
        self.assertEqual('A#', fretboard[6][6])
        self.assertEqual('B', fretboard[6][7])
        self.assertEqual('C', fretboard[6][8])
        self.assertEqual('C#', fretboard[6][9])
        self.assertEqual('D', fretboard[6][10])
        self.assertEqual('D#', fretboard[6][11])
        self.assertEqual('E', fretboard[6][12])

    def test_fifth_string_notes_are_set(self):
        fretboard = make_fretboard(Tuning('E', 'standard'))

        self.assertEqual('A', fretboard[5][0])
        self.assertEqual('A#', fretboard[5][1])
        self.assertEqual('B', fretboard[5][2])
        self.assertEqual('C', fretboard[5][3])
        self.assertEqual('C#', fretboard[5][4])
        self.assertEqual('D', fretboard[5][5])
        self.assertEqual('D#', fretboard[5][6])
        self.assertEqual('E', fretboard[5][7])
        self.assertEqual('F', fretboard[5][8])
        self.assertEqual('F#', fretboard[5][9])
        self.assertEqual('G', fretboard[5][10])
        self.assertEqual('G#', fretboard[5][11])
        self.assertEqual('A', fretboard[5][12])

    def test_get_note_returns_note_name(self):
        note = get_note(FretPosition(string=4, fret=5), Tuning('E', 'standard'))

        self.assertEqual('G', note)

    def test_note_positions_returns_all_positions_for_a_note(self):
        positions = note_positions('A', Tuning('E', 'standard'))

        expected_positions = [
            FretPosition(string=6, fret=5),
            FretPosition(string=5, fret=0),
            FretPosition(string=5, fret=12),
            FretPosition(string=4, fret=7),
            FretPosition(string=3, fret=2),
            FretPosition(string=2, fret=10),
            FretPosition(string=1, fret=5),
        ]

        self.assertEqual(positions, expected_positions)
