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

        # Variation
        self.assertEqual(heights.max, 187)
        self.assertEqual(heights.min, 176)
        self.assertEqual(heights.range, 11)
        values = stats.Variable(600, 470, 170, 430, 300)
        self.assertEqual(values.mean, 394)
        self.assertEqual(values.deviation(400), 6)
        self.assertEqual(values.deviation(300), -94)
        self.assertEqual(values.variance, 27130)
        self.assertEqual(values.pop_variance, 21704)
        self.assertAlmostEqual(values.st_dev, 165, delta=1)
        self.assertAlmostEqual(values.pop_st_dev, 147, delta=1)

        # Relative standing
        self.assertAlmostEqual(heights.zscore(170), -2.73, delta=0.01)
        values = stats.Variable(*[n * 2 for n in range(200)])
        self.assertEqual(values.percentile(100), 25)
        self.assertEqual(values.percentile(320), 80)
        self.assertEqual(values.quartile(90), 1)
        self.assertEqual(values.quartile(320), 4)
