import numerus.stats as stats
from unittest import TestCase

class Tests(TestCase):

    def test(self):
        heights = stats.Variable(181, 176, 187, 185, 180)
        self.assertEqual(heights.values, (181, 176, 187, 185, 180))
        self.assertEqual(heights[1], 176)
        self.assertEqual(heights.length, 5)
