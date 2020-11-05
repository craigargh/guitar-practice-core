from unittest import TestCase

from guitarpractice.annotators import hammer_on_asc, pull_off_desc, down_pick_on_the_beat
from guitarpractice.constants import HAMMER_ON, PULL_OFF, DOWN_PICK, UP_PICK
from guitarpractice.models import Note, FretPosition, Beat


class TestHammerOnAsc(TestCase):
    def test_hammer_on_tie_is_added_to_asc_positions(self):
        notes = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = hammer_on_asc(notes)

        expected = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2), tie=HAMMER_ON),
        ]

        self.assertEqual(expected, result)

    def test_hammer_on_tie_is_not_added_to_desc_positions(self):
        notes = [
            Note(order=0, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = hammer_on_asc(notes)

        expected = [
            Note(order=0, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        self.assertEqual(expected, result)

    def test_hammer_on_is_not_added_after_string_change(self):
        notes = [
            Note(order=0, position=FretPosition(string=6, fret=5), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(string=5, fret=5), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = hammer_on_asc(notes)

        expected = [
            Note(order=0, position=FretPosition(string=6, fret=5), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(string=5, fret=5), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        self.assertEqual(expected, result)

    def test_hammer_on_tie_is_not_added_to_up_or_down_picked_note(self):
        notes = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2),
                 annotations=[DOWN_PICK]),
            Note(order=1, position=FretPosition(8, 6), duration=Beat(1), elapsed_beats=Beat(2), annotations=[UP_PICK]),
        ]

        result = hammer_on_asc(notes)

        expected = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2),
                 annotations=[DOWN_PICK]),
            Note(order=1, position=FretPosition(8, 6), duration=Beat(1), elapsed_beats=Beat(2), annotations=[UP_PICK]),
        ]

        self.assertEqual(expected, result)


class TestPullOffDesc(TestCase):
    def test_pull_off_tie_is_added_to_desc_positions(self):
        notes = [
            Note(order=0, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = pull_off_desc(notes)

        expected = [
            Note(order=0, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(2), tie=PULL_OFF),
        ]

        self.assertEqual(expected, result)

    def test_pull_off_tie_is_not_added_to_asc_positions(self):
        notes = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = pull_off_desc(notes)

        expected = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        self.assertEqual(expected, result)

    def test_pull_off_is_not_added_after_string_change(self):
        notes = [
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(string=6, fret=5), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = pull_off_desc(notes)

        expected = [
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(string=6, fret=5), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        self.assertEqual(expected, result)

    def test_hammer_on_is_note_added_to_down_picked_or_up_picked_notes(self):
        notes = [
            Note(order=0, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(2),
                 annotations=[DOWN_PICK]),
            Note(order=2, position=FretPosition(4, 6), duration=Beat(1), elapsed_beats=Beat(2),
                 annotations=[UP_PICK]),
        ]

        result = pull_off_desc(notes)

        expected = [
            Note(order=0, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(2),
                 annotations=[DOWN_PICK]),
            Note(order=2, position=FretPosition(4, 6), duration=Beat(1), elapsed_beats=Beat(2),
                 annotations=[UP_PICK]),
        ]

        self.assertEqual(expected, result)


class TestDownPickOnTheBeat(TestCase):
    def test_down_pick_annotation_is_added_to_first_note_of_each_beat(self):
        notes = [
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(5, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(7, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
        ]

        result = down_pick_on_the_beat(notes)

        expected = [
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(1, 8),
                 annotations=[DOWN_PICK]),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(3, 8),
                 annotations=[DOWN_PICK]),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(5, 8),
                 annotations=[DOWN_PICK]),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(7, 8),
                 annotations=[DOWN_PICK]),
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
        ]

        self.assertEqual(expected, result)
