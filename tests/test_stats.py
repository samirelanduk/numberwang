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



class ProbabilityTests(TestCase):

    def test_combinatorics(self):
        # How many ways of arranging six objects are there?
        self.assertEqual(stats.permutations(6), 720)

        # How many ways of arranging three of five objects are there?
        self.assertEqual(stats.permutations(6, 3), 120)

        # How many combinations of six objects are there?
        self.assertEqual(stats.combinations(6), 1)
        self.assertEqual(stats.combinations(6, 5), 6)
        self.assertEqual(stats.combinations(6, 4), 15)
        self.assertEqual(stats.combinations(6, 3), 20)
        self.assertEqual(stats.combinations(6, 2), 15)

        # How many outcomes are there of a three-stage experiment?
        self.assertEqual(stats.multiplications(6), 6)
        self.assertEqual(stats.multiplications(6, 3), 18)
        self.assertEqual(stats.multiplications(6, 6, 3), 108)

        # These permutations and combinations etc. can actually be produced
        options = ["A", "B", "C", "D", "E"]
        self.assertEqual(set(stats.permutate(options, 2)), set((
         ("A", "B"), ("B", "A"), ("A", "C"), ("C", "A"), ("A", "D"),
         ("D", "A"), ("A", "E"), ("E", "A"), ("B", "C"), ("C", "B"),
         ("B", "D"), ("D", "B"), ("B", "E"), ("E", "B"), ("C", "D"),
         ("D", "C"), ("C", "E"), ("E", "C"), ("D", "E"), ("E", "D")
        )))
        combinations = tuple(stats.combine(options, 2))
        self.assertEqual(len(combinations), 10)
        for set_ in (
         set(["A", "B"]), set(["A", "C"]), set(["A", "D"]), set(["A", "E"]),
         set(["B", "C"]), set(["B", "D"]), set(["B", "E"]), set(["C", "D"]),
         set(["C", "E"]), set(["D", "E"])
        ):
            self.assertIn(set_, combinations)
        self.assertEqual(tuple(stats.multiply(options, options)), (
         ("A", "A"), ("A", "B"), ("A", "C"), ("A", "D"), ("A", "E"),
         ("B", "A"), ("B", "B"), ("B", "C"), ("B", "D"), ("B", "E"),
         ("C", "A"), ("C", "B"), ("C", "C"), ("C", "D"), ("C", "E"),
         ("D", "A"), ("D", "B"), ("D", "C"), ("D", "D"), ("D", "E"),
         ("E", "A"), ("E", "B"), ("E", "C"), ("E", "D"), ("E", "E")
        ))


    def test_events(self):
        # Rolling a fair die
        var = stats.RandomVariable(1, 2, 3, 4, 5, 6)
        self.assertEqual(var.sample_space, {1, 2, 3, 4, 5, 6})
        self.assertEqual(var(1), 1/6)
        self.assertEqual(var(6), 1/6)

        event_3_or_5 = stats.Event(3, 5)
        self.assertEqual(var(event_3_or_5), 1 / 3)
        event_even = stats.Event(callable=lambda o: o % 2)
        self.assertEqual(var(event_even), 0.5)
