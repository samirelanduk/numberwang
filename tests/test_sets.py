from unittest import TestCase
import numerus

class Test(TestCase):

    def test(self):
        # Natural numbers
        self.assertIn(3, numerus.naturals)
        self.assertNotIn(0, numerus.naturals)
        self.assertNotIn(-1, numerus.naturals)
        self.assertNotIn(3.5, numerus.naturals)

        # Whole numbers
        self.assertIn(3, numerus.wholes)
        self.assertIn(0, numerus.wholes)
        self.assertNotIn(-1, numerus.wholes)
        self.assertNotIn(3.5, numerus.wholes)

        # Integers
        self.assertIn(3, numerus.integers)
        self.assertIn(0, numerus.integers)
        self.assertIn(-1, numerus.integers)
        self.assertNotIn(3.5, numerus.integers)

        # Rational numbers
        self.assertIn(3, numerus.rationals)
        self.assertIn(0, numerus.rationals)
        self.assertIn(-1, numerus.rationals)
        self.assertIn(3.5, numerus.rationals)
