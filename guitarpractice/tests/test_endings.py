from unittest import TestCase

from guitarpractice.endings import fill_remaining_with_repeated_patterns
from guitarpractice.models import Note, Beat, FretPosition


class TestFillRemainingWithRepeatedPatterns(TestCase):
    def test_notes_are_repeated_until_bar_is_complete(self):
        notes = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
        ]

        result = fill_remaining_with_repeated_patterns(notes)

        expected = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1, 4)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1, 2)),
            Note(order=2, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(3, 4)),
            Note(order=3, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1, 1)),
        ]

        self.assertEqual(expected, result)

    def test_notes_are_repeated_until_bar_is_complete_sixteenth_notes(self):
        notes = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(1, 16)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(2, 16)),
            Note(order=2, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(3, 16)),
            Note(order=3, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(4, 16)),
        ]

        result = fill_remaining_with_repeated_patterns(notes)

        expected = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(1, 16)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(2, 16)),
            Note(order=2, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(3, 16)),
            Note(order=3, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(4, 16)),
            Note(order=4, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(5, 16)),
            Note(order=5, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(6, 16)),
            Note(order=6, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(7, 16)),
            Note(order=7, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(8, 16)),
            Note(order=8, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(9, 16)),
            Note(order=9, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(10, 16)),
            Note(order=10, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(11, 16)),
            Note(order=11, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(12, 16)),
            Note(order=12, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(13, 16)),
            Note(order=13, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(14, 16)),
            Note(order=14, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(15, 16)),
            Note(order=15, position=FretPosition(5, 6), duration=Beat(1, 16), elapsed_beats=Beat(16, 16)),
        ]

        self.assertEqual(expected, result)

    def test_rest_note_is_added_if_repeating_doesnt_fill_bar_perfectly(self):
        self.fail()

    def only_notes_from_last_bar_are_used_if_multiple_bars(self):
        self.fail()

    def chords_are_repeated_correctly(self):
        self.fail()
