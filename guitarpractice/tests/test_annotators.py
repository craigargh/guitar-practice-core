from unittest import TestCase

from guitarpractice.annotators import hammer_on_asc, pull_off_desc
from guitarpractice.constants import HAMMER_ON, PULL_OFF
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

    def test_hammer_on_is_not_added_after_string_change(self):
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
