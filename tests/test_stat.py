from unittest import TestCase
from numerus.stat import mean

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
