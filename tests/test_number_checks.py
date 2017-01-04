from unittest import TestCase
from numberwang.checks import is_numeric

class IsNumericTests(TestCase):

    def test_integers_classed_as_numeric(self):
        self.assertTrue(is_numeric(-5))
        self.assertTrue(is_numeric(0))
        self.assertTrue(is_numeric(5))


    def test_floats_classed_as_numeric(self):
        self.assertTrue(is_numeric(-5.34))
        self.assertTrue(is_numeric(0.0))
        self.assertTrue(is_numeric(5.9))


    def test_everything_else_not_classed_as_numeric(self):
        self.assertFalse(is_numeric("string"))
        self.assertFalse(is_numeric(None))
        self.assertFalse(is_numeric(False))
        self.assertFalse(is_numeric(True))
