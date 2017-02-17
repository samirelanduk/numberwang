from unittest import TestCase
import numerus.stats

class StatsFunctionsImportTests(TestCase):

    def test_mean_imported(self):
        from numerus.stats.functions import mean
        self.assertIs(mean, numerus.stats.mean)


    def test_median_imported(self):
        from numerus.stats.functions import median
        self.assertIs(median, numerus.stats.median)


    def test_mode_imported(self):
        from numerus.stats.functions import mode
        self.assertIs(mode, numerus.stats.mode)
