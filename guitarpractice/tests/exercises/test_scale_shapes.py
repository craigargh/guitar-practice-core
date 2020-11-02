from unittest import TestCase

from guitarpractice.shapes import major_scale_shapes, pentatonic_scale_shapes


class TestCMajor(TestCase):
    def test_e_phrygian_has_fifteen_positions(self):
        shape = major_scale_shapes.e_phrygian()

        self.assertEqual(15, len(shape.positions))

    def test_f_lydian_has_fifteen_positions(self):
        shape = major_scale_shapes.f_lydian()

        self.assertEqual(15, len(shape.positions))

    def test_g_mixolydian_has_fifteen_positions(self):
        shape = major_scale_shapes.g_mixolydian()

        self.assertEqual(15, len(shape.positions))

    def test_a_aeolian_has_fifteen_positions(self):
        shape = major_scale_shapes.a_aeolian()

        self.assertEqual(15, len(shape.positions))

    def test_b_locrian_has_fifteen_positions(self):
        shape = major_scale_shapes.b_locrian()

        self.assertEqual(15, len(shape.positions))

    def test_c_ionian_has_fifteen_positions(self):
        shape = major_scale_shapes.c_ionian()

        self.assertEqual(15, len(shape.positions))

    def test_d_dorian_has_fifteen_positions(self):
        shape = major_scale_shapes.d_dorian()

        self.assertEqual(15, len(shape.positions))


class TestCMajorPentatonic(TestCase):
    def test_c_major_has_11_positions(self):
        shape = pentatonic_scale_shapes.c_major()

        self.assertEqual(11, len(shape.positions))

    def test_d_dorian_has_11_positions(self):
        shape = pentatonic_scale_shapes.d_dorian()

        self.assertEqual(11, len(shape.positions))

    def test_e_phrygian_has_11_positions(self):
        shape = pentatonic_scale_shapes.e_phrygian()

        self.assertEqual(11, len(shape.positions))

    def test_g_mixolydian_has_11_positions(self):
        shape = pentatonic_scale_shapes.g_mixolydian()

        self.assertEqual(11, len(shape.positions))

    def test_a_minor_has_11_positions(self):
        shape = pentatonic_scale_shapes.a_minor()

        self.assertEqual(11, len(shape.positions))
