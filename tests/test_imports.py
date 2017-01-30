from unittest import TestCase
import numerus

class TrigObjectsTests(TestCase):

    def test_sine_law_imported(self):
        from numerus.geometry import sine_law
        self.assertIs(sine_law, numerus.sine_law)


    def test_cosine_law_imported(self):
        from numerus.geometry import cosine_law
        self.assertIs(cosine_law, numerus.cosine_law)



class ChecksObjectsTests(TestCase):

    def test_is_numeric_imported(self):
        from numerus.checks import is_numeric
        self.assertIs(is_numeric, numerus.is_numeric)
