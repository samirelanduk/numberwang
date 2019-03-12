import numerus.stats as stats
from unittest import TestCase

class Tests(TestCase):

    def test(self):
        # Variable creation
        heights = stats.Variable(181, 176, 187, 185, 180)
        self.assertEqual(heights.values, (181, 176, 187, 185, 180))
        self.assertEqual(heights[1], 176)
        self.assertEqual(heights.length, 5)

        # Central tendency
        self.assertEqual(heights.mean, 181.8)
        self.assertEqual(stats.Variable().mean, None)
        self.assertEqual(heights.median, 181)
        self.assertEqual(stats.Variable(1, 2, 3, 4).median, 2.5)
        self.assertEqual(stats.Variable().median, None)
        self.assertEqual(stats.Variable(1, 2, 3, 1).mode, 1)
        self.assertEqual(stats.Variable(1, 1, 1, 1).mode, 1)
        self.assertEqual(heights.mode, None)
        self.assertEqual(stats.Variable().mode, None)
