from unittest import TestCase
import numerus.geometry

class TrigFunctionsImportTests(TestCase):

    def test_sine_law_imported(self):
        from numerus.geometry.trig import sine_law
        self.assertIs(sine_law, numerus.geometry.sine_law)


    def test_cosine_law_imported(self):
        from numerus.geometry.trig import cosine_law
        self.assertIs(cosine_law, numerus.geometry.cosine_law)
