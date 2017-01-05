from unittest import TestCase
import numberwang

class TrigObjectsTests(TestCase):

    def test_sine_law_imported(self):
        from numberwang.trig import sine_law
        self.assertIs(sine_law, numberwang.sine_law)


    def test_cosine_law_imported(self):
        from numberwang.trig import cosine_law
        self.assertIs(cosine_law, numberwang.cosine_law)



class ChecksObjectsTests(TestCase):

    def test_is_numeric_imported(self):
        from numberwang.checks import is_numeric
        self.assertIs(is_numeric, numberwang.is_numeric)
