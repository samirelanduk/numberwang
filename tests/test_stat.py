from unittest import TestCase
from numerus.stat import mean, median, mode

class MeanTests(TestCase):

    def test_can_get_mean(self):
        self.assertEqual(mean(6.5), 6.5)
        self.assertEqual(mean(6, 11, 7), 8)


    def test_mean_requires_values(self):
        with self.assertRaises(TypeError):
            mean()


    def test_mean_inputs_must_be_numeric(self):
        with self.assertRaises(TypeError):
            mean(6, "11")



class MedianTests(TestCase):

    def test_can_get_median(self):
        self.assertEqual(median(2, 9, 11, 5, 6), 6)


    def test_can_get_median_when_even_values(self):
        self.assertEqual(median(2, 9, 11, 5, 6, 27), 7.5)


    def test_median_requires_values(self):
        with self.assertRaises(TypeError):
            median()


    def test_median_inputs_must_be_numeric(self):
        with self.assertRaises(TypeError):
            median(6, "11")



class ModeTests(TestCase):

    def test_can_get_mode(self):
        self.assertEqual(mode(61, 54, 60, 59, 54, 51, 60, 53, 54), 54)


    def test_mode_is_none_when_no_single_most_common(self):
        self.assertIs(mode(61, 54, 60, 59, 54, 51, 60, 53), None)
        self.assertIs(mode(1, 2, 3, 4, 5), None)


    def test_mode_requires_values(self):
        with self.assertRaises(TypeError):
            mode()


    def test_mode_inputs_must_be_numeric(self):
        with self.assertRaises(TypeError):
            mode(6, "11")
