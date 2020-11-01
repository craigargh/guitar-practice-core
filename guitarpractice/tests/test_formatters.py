from unittest import TestCase, skip

from guitarpractice.formatters import to_vextab
from guitarpractice.models import Sequence, Note, FretPosition, Beat, GuitarShape


class TestVexTabFormatter(TestCase):
    def test_positions_are_converted_to_string(self):
        positions = [
            FretPosition(string=3, fret=1),
            FretPosition(string=4, fret=2),
            FretPosition(string=5, fret=3),
            FretPosition(string=6, fret=4),
        ]

        duration = Beat(1)
        notes = [
            Note(order=0, position=positions[0], duration=duration, elapsed_beats=Beat(1)),
            Note(order=1, position=positions[1], duration=duration, elapsed_beats=Beat(2)),
            Note(order=2, position=positions[2], duration=duration, elapsed_beats=Beat(3)),
            Note(order=3, position=positions[3], duration=duration, elapsed_beats=Beat(4)),
        ]

        shapes = [
            GuitarShape(name='shape1', positions=positions, category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :q 1/3 :q 2/4 :q 3/5 :q 4/6 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_whole_notes_have_a_w_duration(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(4, 4)

        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1, 1)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2, 1)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :w 5/6 | :w 5/6 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_half_notes_have_a_h_duration(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(2, 4)

        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(2, 4)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(4, 4)),
            Note(order=3, position=position, duration=duration, elapsed_beats=Beat(6, 4)),
            Note(order=4, position=position, duration=duration, elapsed_beats=Beat(8, 4)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :h 5/6 :h 5/6 | :h 5/6 :h 5/6 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_quarter_notes_have_a_q_duration(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(1, 4)

        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1, 4)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2, 4)),
            Note(order=3, position=position, duration=duration, elapsed_beats=Beat(3, 4)),
            Note(order=4, position=position, duration=duration, elapsed_beats=Beat(4, 4)),
            Note(order=5, position=position, duration=duration, elapsed_beats=Beat(5, 4)),
            Note(order=6, position=position, duration=duration, elapsed_beats=Beat(6, 4)),
            Note(order=7, position=position, duration=duration, elapsed_beats=Beat(7, 4)),
            Note(order=8, position=position, duration=duration, elapsed_beats=Beat(8, 4)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :q 5/6 :q 5/6 :q 5/6 :q 5/6 | :q 5/6 :q 5/6 :q 5/6 :q 5/6 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_eighth_notes_have_a_8_duration(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(1, 8)

        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1, 8)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2, 8)),
            Note(order=3, position=position, duration=duration, elapsed_beats=Beat(3, 8)),
            Note(order=4, position=position, duration=duration, elapsed_beats=Beat(4, 8)),
            Note(order=5, position=position, duration=duration, elapsed_beats=Beat(5, 8)),
            Note(order=6, position=position, duration=duration, elapsed_beats=Beat(6, 8)),
            Note(order=7, position=position, duration=duration, elapsed_beats=Beat(7, 8)),
            Note(order=8, position=position, duration=duration, elapsed_beats=Beat(8, 8)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :8 5/6 :8 5/6 :8 5/6 :8 5/6 :8 5/6 :8 5/6 :8 5/6 :8 5/6 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_sixteenth_notes_have_a_16_duration(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(1, 16)

        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1, 16)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2, 16)),
            Note(order=3, position=position, duration=duration, elapsed_beats=Beat(3, 16)),
            Note(order=4, position=position, duration=duration, elapsed_beats=Beat(4, 16)),
            Note(order=5, position=position, duration=duration, elapsed_beats=Beat(5, 16)),
            Note(order=6, position=position, duration=duration, elapsed_beats=Beat(6, 16)),
            Note(order=7, position=position, duration=duration, elapsed_beats=Beat(7, 16)),
            Note(order=8, position=position, duration=duration, elapsed_beats=Beat(8, 16)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :16 5/6 :16 5/6 :16 5/6 :16 5/6 :16 5/6 :16 5/6 :16 5/6 :16 5/6 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_thirty_second_notes_have_a_32_duration(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(1, 32)

        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1, 32)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2, 32)),
            Note(order=3, position=position, duration=duration, elapsed_beats=Beat(3, 32)),
            Note(order=4, position=position, duration=duration, elapsed_beats=Beat(4, 32)),
            Note(order=5, position=position, duration=duration, elapsed_beats=Beat(5, 32)),
            Note(order=6, position=position, duration=duration, elapsed_beats=Beat(6, 32)),
            Note(order=7, position=position, duration=duration, elapsed_beats=Beat(7, 32)),
            Note(order=8, position=position, duration=duration, elapsed_beats=Beat(8, 32)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :32 5/6 :32 5/6 :32 5/6 :32 5/6 :32 5/6 :32 5/6 :32 5/6 :32 5/6 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_tab_bars_are_added_every_four_beats(self):
        positions = [
            FretPosition(string=3, fret=1),
            FretPosition(string=4, fret=2),
            FretPosition(string=5, fret=3),
        ]

        notes = [
            Note(order=0, position=positions[0], duration=Beat(2, 4), elapsed_beats=Beat(2, 4)),
            Note(order=1, position=positions[1], duration=Beat(2, 4), elapsed_beats=Beat(4, 4)),
            Note(order=2, position=positions[2], duration=Beat(4, 4), elapsed_beats=Beat(2, 1)),
        ]

        shapes = [
            GuitarShape(name='shape1', positions=positions, category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :h 1/3 :h 2/4 | :w 3/5 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_tabs_are_split_into_mutliple_staves_every_two_bars(self):
        position = FretPosition(string=3, fret=1)

        notes = [
            Note(order=0, position=position, duration=Beat(1, 1), elapsed_beats=Beat(1, 1)),
            Note(order=1, position=position, duration=Beat(1, 1), elapsed_beats=Beat(2, 1)),
            Note(order=2, position=position, duration=Beat(1, 1), elapsed_beats=Beat(3, 1)),
            Note(order=3, position=position, duration=Beat(1, 1), elapsed_beats=Beat(4, 1)),
            Note(order=4, position=position, duration=Beat(1, 1), elapsed_beats=Beat(5, 1)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :w 1/3 | :w 1/3 |\n'
            '\n'
            'tabstave notation=false\n'
            'notes :w 1/3 | :w 1/3 |\n'
            '\n'
            'tabstave notation=false\n'
            'notes :w 1/3 =:|'
        )
        self.assertEqual(expected, vextab)

    def test_rests_are_added_to_the_tab(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(1, 4)
        rest = Beat(1, 4, rest=True)

        notes = [
            Note(order=0, position=position, duration=duration, elapsed_beats=Beat(1, 4)),
            Note(order=1, position=position, duration=rest, elapsed_beats=Beat(2, 4)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(3, 4)),
            Note(order=3, position=position, duration=rest, elapsed_beats=Beat(4, 4)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :q 5/6 :q ## :q 5/6 :q ## =:|'
        )
        self.assertEqual(expected, vextab)

    def test_chords_are_converted_to_tab(self):
        position = FretPosition(string=6, fret=0)
        duration = Beat(1, 4)

        notes = [
            Note(order=1, position=FretPosition(3, 6), duration=duration, elapsed_beats=Beat(1, 4)),
            Note(order=1, position=FretPosition(5, 5), duration=duration, elapsed_beats=Beat(1, 4)),
            Note(order=1, position=FretPosition(5, 4), duration=duration, elapsed_beats=Beat(1, 4)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2, 4)),
            Note(order=3, position=FretPosition(5, 6), duration=duration, elapsed_beats=Beat(3, 4)),
            Note(order=3, position=FretPosition(7, 5), duration=duration, elapsed_beats=Beat(3, 4)),
            Note(order=3, position=FretPosition(7, 4), duration=duration, elapsed_beats=Beat(3, 4)),
            Note(order=4, position=position, duration=duration, elapsed_beats=Beat(4, 4)),

        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :q (3/6.5/5.5/4) :q 0/6 :q (5/6.7/5.7/4) :q 0/6 =:|'
        )
        self.assertEqual(expected, vextab)

    @skip
    def test_half_note_triplets_are_marked_in_the_tab(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(1, 3)

        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(1, 3)),
            Note(order=2, position=position, duration=duration, elapsed_beats=Beat(2, 3)),
            Note(order=3, position=position, duration=duration, elapsed_beats=Beat(3, 3)),
            Note(order=4, position=position, duration=duration, elapsed_beats=Beat(4, 3)),
            Note(order=5, position=position, duration=duration, elapsed_beats=Beat(5, 3)),
            Note(order=6, position=position, duration=duration, elapsed_beats=Beat(6, 3)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :h 5/6 :h 5/6 :h 5/6 ^3^ | :h 5/6 :h 5/6 :h 5/6 ^3^ =:|'
        )

        self.assertEqual(expected, vextab)

    def test_quarter_note_triplets_are_marked_in_the_tab(self):
        pass

    def test_sixteenth_note_triplets_are_marked_in_the_tab(self):
        pass

    def test_thirty_second_note_triplets_are_marked_in_the_tab(self):
        pass

    def test_notation_is_true_when_tuplets_are_included_as_a_workaround(self):
        pass

    def test_odd_length_quarter_notes_are_split_with_tie(self):
        position = FretPosition(string=6, fret=5)
        duration = Beat(3, 4)

        notes = [
            Note(order=1, position=position, duration=duration, elapsed_beats=Beat(3, 4)),
        ]
        shapes = [
            GuitarShape(name='shape1', positions=[position], category='scale')
        ]
        sequence = Sequence(notes=notes, shapes=shapes)

        vextab = to_vextab(sequence)

        expected = (
            'tabstave notation=false\n'
            'notes =|: :h 5/6 T:q: 5/6 =:|'
        )

        self.assertEqual(expected, vextab)

    def test_odd_length_quarter_note_chords_are_split_with_tie(self):
        beat = Beat(3, 8)

        expected = (
            'tabstave notation=false\n'
            'notes (12/5.12/4) :8 T(12/5.12/4) '
        )
        self.fail("Write the test")
