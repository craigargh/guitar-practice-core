from unittest import TestCase

from guitarpractice.annotators import hammer_on_asc, pull_off_desc, down_pick_on_the_beat, down_pick_alternating_beats, \
    palm_mute_open, palm_mute_single, shape_name
from guitarpractice.constants import HAMMER_ON, PULL_OFF, DOWN_PICK, UP_PICK, PALM_MUTE
from guitarpractice.models import Note, FretPosition, Beat, GuitarShape


class TestHammerOnAsc(TestCase):
    def test_hammer_on_tie_is_added_to_asc_positions(self):
        notes = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = hammer_on_asc(notes, None)

        expected = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2), slur=HAMMER_ON),
        ]

        self.assertEqual(expected, result)

    def test_hammer_on_tie_is_not_added_to_desc_positions(self):
        notes = [
            Note(order=0, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = hammer_on_asc(notes, None)

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

        result = hammer_on_asc(notes, None)

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

        result = hammer_on_asc(notes, None)

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

        result = pull_off_desc(notes, None)

        expected = [
            Note(order=0, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(2), slur=PULL_OFF),
        ]

        self.assertEqual(expected, result)

    def test_pull_off_tie_is_not_added_to_asc_positions(self):
        notes = [
            Note(order=0, position=FretPosition(5, 6), duration=Beat(1), elapsed_beats=Beat(1)),
            Note(order=1, position=FretPosition(7, 6), duration=Beat(1), elapsed_beats=Beat(2)),
        ]

        result = pull_off_desc(notes, None)

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

        result = pull_off_desc(notes, None)

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

        result = pull_off_desc(notes, None)

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
            Note(order=1, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
            Note(order=2, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
            Note(order=3, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
            Note(order=4, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(5, 8)),
            Note(order=5, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
            Note(order=6, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(7, 8)),
            Note(order=7, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
            Note(order=8, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(9, 8)),
        ]

        result = down_pick_on_the_beat(notes, None)

        expected = [
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(1, 8),
                 annotations=[DOWN_PICK]),
            Note(order=1, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
            Note(order=2, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(3, 8),
                 annotations=[DOWN_PICK]),
            Note(order=3, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
            Note(order=4, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(5, 8),
                 annotations=[DOWN_PICK]),
            Note(order=5, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
            Note(order=6, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(7, 8),
                 annotations=[DOWN_PICK]),
            Note(order=7, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
            Note(order=8, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(9, 8),
                 annotations=[DOWN_PICK]),
        ]

        self.assertEqual(expected, result)


class TestDownAlternatingBeats(TestCase):
    def test_down_pick_annotation_is_added_to_evey_other_beat(self):
        notes = [
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(1, 8)),
            Note(order=1, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
            Note(order=2, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
            Note(order=3, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
            Note(order=4, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(5, 8)),
            Note(order=5, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
            Note(order=6, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(7, 8)),
            Note(order=7, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
            Note(order=8, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(9, 8)),
        ]

        result = down_pick_alternating_beats(notes, None)

        expected = [
            Note(order=0, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(1, 8),
                 annotations=[DOWN_PICK]),
            Note(order=1, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(2, 8)),
            Note(order=2, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(3, 8)),
            Note(order=3, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(4, 8)),
            Note(order=4, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(5, 8),
                 annotations=[DOWN_PICK]),
            Note(order=5, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(6, 8)),
            Note(order=6, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(7, 8)),
            Note(order=7, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(8, 8)),
            Note(order=8, position=FretPosition(string=5, fret=5), duration=Beat(1, 8), elapsed_beats=Beat(9, 8),
                 annotations=[DOWN_PICK]),
        ]

        self.assertEqual(expected, result)


class TestPalmMuteOpen(TestCase):
    def test_open_strings_are_palm_muted(self):
        notes = [
            Note(position=FretPosition(0, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(0, 5), duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=FretPosition(0, 4), duration=Beat(1), elapsed_beats=Beat(3), order=2),
            Note(position=FretPosition(0, 3), duration=Beat(1), elapsed_beats=Beat(4), order=3),
            Note(position=FretPosition(0, 2), duration=Beat(1), elapsed_beats=Beat(5), order=4),
            Note(position=FretPosition(0, 1), duration=Beat(1), elapsed_beats=Beat(6), order=5),
        ]

        result = palm_mute_open(notes, None)

        expected = [
            Note(position=FretPosition(0, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 5), duration=Beat(1), elapsed_beats=Beat(2), order=1,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 4), duration=Beat(1), elapsed_beats=Beat(3), order=2,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 3), duration=Beat(1), elapsed_beats=Beat(4), order=3,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 2), duration=Beat(1), elapsed_beats=Beat(5), order=4,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 1), duration=Beat(1), elapsed_beats=Beat(6), order=5,
                 annotations=[PALM_MUTE]),
        ]

        self.assertEqual(expected, result)

    def test_single_notes_are_not_palm_muted(self):
        notes = [
            Note(position=FretPosition(1, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(2, 5), duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=FretPosition(3, 4), duration=Beat(1), elapsed_beats=Beat(3), order=2),
            Note(position=FretPosition(4, 3), duration=Beat(1), elapsed_beats=Beat(4), order=3),
            Note(position=FretPosition(5, 2), duration=Beat(1), elapsed_beats=Beat(5), order=4),
            Note(position=FretPosition(6, 1), duration=Beat(1), elapsed_beats=Beat(6), order=5),
        ]

        result = palm_mute_open(notes, None)

        expected = [
            Note(position=FretPosition(1, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(2, 5), duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=FretPosition(3, 4), duration=Beat(1), elapsed_beats=Beat(3), order=2),
            Note(position=FretPosition(4, 3), duration=Beat(1), elapsed_beats=Beat(4), order=3),
            Note(position=FretPosition(5, 2), duration=Beat(1), elapsed_beats=Beat(5), order=4),
            Note(position=FretPosition(6, 1), duration=Beat(1), elapsed_beats=Beat(6), order=5),
        ]

        self.assertEqual(expected, result)

    def test_chords_are_not_palm_muted(self):
        notes = [
            Note(position=FretPosition(0, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(0, 5), duration=Beat(1), elapsed_beats=Beat(1), order=0),
        ]

        result = palm_mute_open(notes, None)

        expected = [
            Note(position=FretPosition(0, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(0, 5), duration=Beat(1), elapsed_beats=Beat(1), order=0),
        ]

        self.assertEqual(expected, result)


class TestPalmMuteSingle(TestCase):
    def test_open_strings_are_palm_muted(self):
        notes = [
            Note(position=FretPosition(0, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(0, 5), duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=FretPosition(0, 4), duration=Beat(1), elapsed_beats=Beat(3), order=2),
            Note(position=FretPosition(0, 3), duration=Beat(1), elapsed_beats=Beat(4), order=3),
            Note(position=FretPosition(0, 2), duration=Beat(1), elapsed_beats=Beat(5), order=4),
            Note(position=FretPosition(0, 1), duration=Beat(1), elapsed_beats=Beat(6), order=5),
        ]

        result = palm_mute_single(notes, None)

        expected = [
            Note(position=FretPosition(0, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 5), duration=Beat(1), elapsed_beats=Beat(2), order=1,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 4), duration=Beat(1), elapsed_beats=Beat(3), order=2,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 3), duration=Beat(1), elapsed_beats=Beat(4), order=3,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 2), duration=Beat(1), elapsed_beats=Beat(5), order=4,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(0, 1), duration=Beat(1), elapsed_beats=Beat(6), order=5,
                 annotations=[PALM_MUTE]),
        ]

        self.assertEqual(expected, result)

    def test_single_notes_are_palm_muted(self):
        notes = [
            Note(position=FretPosition(1, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(2, 5), duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=FretPosition(3, 4), duration=Beat(1), elapsed_beats=Beat(3), order=2),
            Note(position=FretPosition(4, 3), duration=Beat(1), elapsed_beats=Beat(4), order=3),
            Note(position=FretPosition(5, 2), duration=Beat(1), elapsed_beats=Beat(5), order=4),
            Note(position=FretPosition(6, 1), duration=Beat(1), elapsed_beats=Beat(6), order=5),
        ]

        result = palm_mute_single(notes, None)

        expected = [
            Note(position=FretPosition(1, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(2, 5), duration=Beat(1), elapsed_beats=Beat(2), order=1,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(3, 4), duration=Beat(1), elapsed_beats=Beat(3), order=2,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(4, 3), duration=Beat(1), elapsed_beats=Beat(4), order=3,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(5, 2), duration=Beat(1), elapsed_beats=Beat(5), order=4,
                 annotations=[PALM_MUTE]),
            Note(position=FretPosition(6, 1), duration=Beat(1), elapsed_beats=Beat(6), order=5,
                 annotations=[PALM_MUTE]),
        ]

        self.assertEqual(expected, result)

    def test_chords_are_not_palm_muted(self):
        notes = [
            Note(position=FretPosition(0, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(0, 5), duration=Beat(1), elapsed_beats=Beat(1), order=0),
        ]

        result = palm_mute_single(notes, None)

        expected = [
            Note(position=FretPosition(0, 6), duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=FretPosition(0, 5), duration=Beat(1), elapsed_beats=Beat(1), order=0),
        ]

        self.assertEqual(expected, result)


class TestShapeName(TestCase):
    def test_shape_name_is_added_to_annotations(self):
        positions = [
            FretPosition(0, 6),
            FretPosition(2, 5),
        ]
        notes = [
            Note(position=positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0),
        ]
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', positions=positions, short_name='E5')
        ]

        result = shape_name(notes, shapes)

        expected = [
            Note(position=positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0, annotations=['label:E5']),
            Note(position=positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0, annotations=['label:E5']),
        ]

        self.assertEqual(expected, result)

    def test_repeated_shapes_are_not_labeled(self):
        positions = [
            FretPosition(0, 6),
            FretPosition(2, 5),
        ]
        notes = [
            Note(position=positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=positions[0], duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=positions[1], duration=Beat(1), elapsed_beats=Beat(2), order=1),
        ]
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', positions=positions, short_name='E5')
        ]

        result = shape_name(notes, shapes)

        expected = [
            Note(position=positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0, annotations=['label:E5']),
            Note(position=positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0, annotations=['label:E5']),
            Note(position=positions[0], duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=positions[1], duration=Beat(1), elapsed_beats=Beat(2), order=1),
        ]

        self.assertEqual(expected, result)

    def test_chord_changes_are_labeled(self):
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', short_name='E5', positions=[
                FretPosition(0, 6),
                FretPosition(2, 5),
            ]),
            GuitarShape(category='chord', name='F5 Power Chord', short_name='F5', positions=[
                FretPosition(1, 6),
                FretPosition(3, 5),
            ]),
        ]

        notes = [
            Note(position=shapes[0].positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=shapes[0].positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=shapes[1].positions[0], duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=shapes[1].positions[1], duration=Beat(1), elapsed_beats=Beat(2), order=1),
        ]

        result = shape_name(notes, shapes)

        expected = [
            Note(position=shapes[0].positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[0].positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[1].positions[0], duration=Beat(1), elapsed_beats=Beat(2), order=1,
                 annotations=['label:F5']),
            Note(position=shapes[1].positions[1], duration=Beat(1), elapsed_beats=Beat(2), order=1,
                 annotations=['label:F5']),
        ]

        self.assertEqual(expected, result)

    def test_repeated_chords_are_labelled_after_chord_change(self):
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', short_name='E5', positions=[
                FretPosition(0, 6),
                FretPosition(2, 5),
            ]),
            GuitarShape(category='chord', name='F5 Power Chord', short_name='F5', positions=[
                FretPosition(1, 6),
                FretPosition(3, 5),
            ]),
        ]

        notes = [
            Note(position=shapes[0].positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=shapes[0].positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=shapes[1].positions[0], duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=shapes[1].positions[1], duration=Beat(1), elapsed_beats=Beat(2), order=1),
            Note(position=shapes[0].positions[0], duration=Beat(1), elapsed_beats=Beat(3), order=2),
            Note(position=shapes[0].positions[1], duration=Beat(1), elapsed_beats=Beat(3), order=2),
        ]

        result = shape_name(notes, shapes)

        expected = [
            Note(position=shapes[0].positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[0].positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0,
                 annotations=['label:E5']),
            Note(position=shapes[1].positions[0], duration=Beat(1), elapsed_beats=Beat(2), order=1,
                 annotations=['label:F5']),
            Note(position=shapes[1].positions[1], duration=Beat(1), elapsed_beats=Beat(2), order=1,
                 annotations=['label:F5']),
            Note(position=shapes[0].positions[0], duration=Beat(1), elapsed_beats=Beat(3), order=2,
                 annotations=['label:E5']),
            Note(position=shapes[0].positions[1], duration=Beat(1), elapsed_beats=Beat(3), order=2,
                 annotations=['label:E5']),
        ]

        self.assertEqual(expected, result)

    def test_shape_name_is_not_added_if_short_name_is_none(self):
        positions = [
            FretPosition(0, 6),
            FretPosition(2, 5),
        ]
        notes = [
            Note(position=positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0),
        ]
        shapes = [
            GuitarShape(category='chord', name='E5 Power Chord', positions=positions)
        ]

        result = shape_name(notes, shapes)

        expected = [
            Note(position=positions[0], duration=Beat(1), elapsed_beats=Beat(1), order=0),
            Note(position=positions[1], duration=Beat(1), elapsed_beats=Beat(1), order=0),
        ]

        self.assertEqual(expected, result)
