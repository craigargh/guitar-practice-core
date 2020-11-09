from unittest import TestCase, skip

from guitarpractice import constants
from guitarpractice.models import Note, FretPosition, Beat
from guitarpractice.note_utils import group_notes, normalise_note_durations


class TestGroupNotes(TestCase):
    def test_individual_notes_are_returned_in_order(self):
        position = FretPosition(string=3, fret=1)

        duration = Beat(1)
        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2)),
            Note(order=3, position=position, duration=duration, elapsed_beats=Beat(3)),
            Note(order=4, position=position, duration=duration, elapsed_beats=Beat(4)),
        ]

        result = group_notes(notes)

        expected = {
            1: [Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1))],
            2: [Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2))],
            3: [Note(order=3, position=position, duration=duration, elapsed_beats=Beat(3))],
            4: [Note(order=4, position=position, duration=duration, elapsed_beats=Beat(4))],
        }

        self.assertEqual(expected, result)

    def test_chords_are_grouped_together(self):
        position = FretPosition(string=3, fret=1)

        duration = Beat(1)
        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1)),
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(2)),
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(3)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(4)),
        ]

        result = group_notes(notes)

        expected = {
            1: [
                Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1)),
                Note(order=1, position=position, duration=duration, elapsed_beats=Beat(2)),
                Note(order=1, position=position, duration=duration, elapsed_beats=Beat(3))
            ],
            2: [Note(order=2, position=position, duration=duration, elapsed_beats=Beat(4))],
        }

        self.assertEqual(expected, result)


class TestNormaliseNoteDurations(TestCase):
    def test_odd_length_quarter_note_is_split(self):
        position = FretPosition(string=3, fret=1)
        notes = [
            Note(order=0, position=position, duration=Beat(3), elapsed_beats=Beat(3)),
            Note(order=1, position=position, duration=Beat(1), elapsed_beats=Beat(4)),
        ]

        result = normalise_note_durations(notes)

        expected = [
            Note(order=0, position=position, duration=Beat(1, 2), elapsed_beats=Beat(1, 2)),
            Note(order=1, position=position, duration=Beat(1, 4), elapsed_beats=Beat(3, 4), tie=constants.TIE),
            Note(order=2, position=position, duration=Beat(1, 4), elapsed_beats=Beat(1, 1)),
        ]

        self.assertEqual(expected, result)

    def test_ties_are_not_added_to_rests(self):
        position = FretPosition(string=3, fret=1)
        notes = [
            Note(order=0, position=None, duration=Beat(3, rest=True), elapsed_beats=Beat(3)),
            Note(order=1, position=position, duration=Beat(1), elapsed_beats=Beat(4)),
        ]

        result = normalise_note_durations(notes)

        expected = [
            Note(order=0, position=None, duration=Beat(1, 2, rest=True), elapsed_beats=Beat(1, 2)),
            Note(order=1, position=None, duration=Beat(1, 4, rest=True), elapsed_beats=Beat(3, 4)),
            Note(order=2, position=position, duration=Beat(1, 4), elapsed_beats=Beat(1, 1)),
        ]

        self.assertEqual(expected, result)

    def test_split_beats_are_in_ascending_order_if_not_at_start_of_bar(self):
        position = FretPosition(string=3, fret=1)
        notes = [
            Note(order=0, position=position, duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=position, duration=Beat(3), elapsed_beats=Beat(4)),
        ]

        result = normalise_note_durations(notes)

        expected = [
            Note(order=0, position=position, duration=Beat(1, 4), elapsed_beats=Beat(1, 4)),
            Note(order=1, position=position, duration=Beat(1, 4), elapsed_beats=Beat(2, 4)),
            Note(order=2, position=position, duration=Beat(2, 4), elapsed_beats=Beat(1, 1), tie=constants.TIE),
        ]

        self.assertEqual(expected, result)

    def test_odd_length_quarter_note_chord_is_split(self):
        position = FretPosition(string=3, fret=1)
        notes = [
            Note(order=0, position=FretPosition(string=3, fret=1), duration=Beat(3, 4), elapsed_beats=Beat(3)),
            Note(order=0, position=FretPosition(string=2, fret=1), duration=Beat(3, 4), elapsed_beats=Beat(3)),
            Note(order=1, position=position, duration=Beat(1), elapsed_beats=Beat(4)),
        ]

        result = normalise_note_durations(notes)

        expected = [
            Note(order=0, position=FretPosition(string=3, fret=1), duration=Beat(1, 2), elapsed_beats=Beat(1, 2)),
            Note(order=0, position=FretPosition(string=2, fret=1), duration=Beat(1, 2), elapsed_beats=Beat(1, 2)),
            Note(order=1, position=FretPosition(string=3, fret=1), duration=Beat(1, 4), elapsed_beats=Beat(3, 4),
                 tie=constants.TIE),
            Note(order=1, position=FretPosition(string=2, fret=1), duration=Beat(1, 4), elapsed_beats=Beat(3, 4),
                 tie=constants.TIE),
            Note(order=2, position=position, duration=Beat(1, 4), elapsed_beats=Beat(1, 1)),
        ]

        self.assertEqual(expected, result)

    def test_hammer_on_tie_is_kept_on_first_note(self):
        position = FretPosition(string=3, fret=1)
        notes = [
            Note(order=0, position=position, duration=Beat(3), elapsed_beats=Beat(3), tie=constants.HAMMER_ON),
            Note(order=1, position=position, duration=Beat(1), elapsed_beats=Beat(4)),
        ]

        result = normalise_note_durations(notes)

        expected = [
            Note(order=0, position=position, duration=Beat(1, 2), elapsed_beats=Beat(1, 2), tie=constants.HAMMER_ON),
            Note(order=1, position=position, duration=Beat(1, 4), elapsed_beats=Beat(3, 4), tie=constants.TIE),
            Note(order=2, position=position, duration=Beat(1, 4), elapsed_beats=Beat(1, 1)),
        ]

        self.assertEqual(expected, result)

    def test_normalise_note_durations_keeps_correct_duration_for_triplets(self):
        position = FretPosition(string=3, fret=1)
        notes = [
            Note(order=0, position=position, duration=Beat(1, 12), elapsed_beats=Beat(1, 12)),
            Note(order=1, position=position, duration=Beat(1, 12), elapsed_beats=Beat(2, 12)),
            Note(order=2, position=position, duration=Beat(1, 12), elapsed_beats=Beat(3, 12)),
        ]

        result = normalise_note_durations(notes)

        expected = [
            Note(order=0, position=position, duration=Beat(1, 12), elapsed_beats=Beat(1, 12)),
            Note(order=1, position=position, duration=Beat(1, 12), elapsed_beats=Beat(2, 12)),
            Note(order=2, position=position, duration=Beat(1, 12), elapsed_beats=Beat(3, 12)),
        ]

        self.assertEqual(expected, result)
