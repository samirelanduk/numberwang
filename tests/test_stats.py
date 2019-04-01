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
        # Sample spaces
        die_outcomes = stats.SampleSpace(1, 2, 3, 4, 5, 6)
        two_die_outcomes = stats.SampleSpace(*stats.multiply({1, 2, 3, 4, 5, 6}, {1, 2, 3, 4, 5, 6}))
        card_outcomes = stats.SampleSpace(*stats.multiply(["H", "D", "S", "C"], range(13)))
        self.assertEqual(die_outcomes.count, 6)
        self.assertEqual(two_die_outcomes.count, 36)
        self.assertEqual(card_outcomes.count, 52)
        self.assertIn(3, die_outcomes)
        self.assertNotIn(7, die_outcomes)
        self.assertIn((1, 4), two_die_outcomes)
        self.assertNotIn((1, 7), two_die_outcomes)
        self.assertIn(("S", 0), card_outcomes)
        self.assertNotIn(("W", 7), card_outcomes)

        # Events
        roll_5 = die_outcomes.event(5)
        roll_1_or_6 = die_outcomes.event(1, 6)
        roll_even = die_outcomes.event(lambda o: o % 2 == 0)
        self.assertEqual(roll_5.count, 1)
        self.assertEqual(roll_1_or_6.count, 2)
        self.assertEqual(roll_even.count, 3)
        matching = two_die_outcomes.event(lambda o: o[0] == o[1])
        self.assertEqual(matching.count, 6)
        seven = two_die_outcomes.event(lambda o: o[0] + o[1] == 7)
        self.assertEqual(seven.count, 6)
        ace = card_outcomes.event(lambda o: o[1] == 0)
        self.assertEqual(ace.count, 4)

        # Event combinations
        roll_5_or_1_or_6 = roll_5 | roll_1_or_6
        self.assertEqual(roll_5_or_1_or_6.outcomes, {1, 5, 6})
        roll_even_and_1_or_6 = roll_even & roll_1_or_6
        self.assertEqual(roll_even_and_1_or_6.outcomes, {6})
        not_ace = ace.complement
        self.assertEqual(not_ace.count, 48)
        self.assertFalse(roll_even.mutually_exclusive_with(roll_1_or_6))
        self.assertTrue(matching.mutually_exclusive_with(seven))
        self.assertTrue(ace.exhaustive_with(not_ace))
        self.assertFalse(matching.exhaustive_with(seven))

        # Random variables
        fair_die = stats.RandomVariable(die_outcomes)
        self.assertEqual(fair_die(1), 1 / 6)
        self.assertEqual(fair_die(7), 0)
        self.assertEqual(fair_die(roll_5), 1 / 6)
        self.assertEqual(fair_die(roll_1_or_6), 1 / 3)
        unfair_die = stats.RandomVariable(die_outcomes, probabilities={4: 0.2})
        self.assertEqual(unfair_die(1), 0.16)
        self.assertEqual(unfair_die(roll_5), 0.16)
        self.assertEqual(unfair_die(roll_1_or_6), 0.32)
