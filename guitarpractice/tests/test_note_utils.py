from unittest import TestCase

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
            Note(order=1, position=position, duration=Beat(1, 4), elapsed_beats=Beat(3, 4), annotations=['tie']),
            Note(order=2, position=position, duration=Beat(1, 4), elapsed_beats=Beat(1, 1)),
        ]

        self.assertEqual(expected, result)

    def test_odd_length_quarter_note_chord_is_split(self):
        position = FretPosition(string=3, fret=1)
        notes = [
            Note(order=0, position=position, duration=Beat(3), elapsed_beats=Beat(3)),
            Note(order=0, position=position, duration=Beat(3), elapsed_beats=Beat(3)),
            Note(order=1, position=position, duration=Beat(1), elapsed_beats=Beat(4)),
        ]

        result = normalise_note_durations(notes)

        expected = [
            Note(order=0, position=position, duration=Beat(1, 2), elapsed_beats=Beat(1, 2)),
            Note(order=1, position=position, duration=Beat(1, 4), elapsed_beats=Beat(3, 4), annotations=['tie']),
            Note(order=0, position=position, duration=Beat(1, 2), elapsed_beats=Beat(1, 2)),
            Note(order=1, position=position, duration=Beat(1, 4), elapsed_beats=Beat(3, 4), annotations=['tie']),
            Note(order=1, position=position, duration=Beat(1, 4), elapsed_beats=Beat(1, 1)),
        ]

        self.assertEqual(expected, result)
