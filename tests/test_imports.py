from unittest import TestCase
import numerus

class GeometryImportTests(TestCase):

    def test_sine_law_imported(self):
        from numerus.geometry import sine_law
        self.assertIs(sine_law, numerus.sine_law)


    def test_cosine_law_imported(self):
        from numerus.geometry import cosine_law
        self.assertIs(cosine_law, numerus.cosine_law)


    def test_translate_imported(self):
        from numerus.geometry import translate
        self.assertIs(translate, numerus.translate)


    def test_rotate_imported(self):
        from numerus.geometry import rotate
        self.assertIs(rotate, numerus.rotate)



class MatrixImportTests(TestCase):

    def test_matrix_imported(self):
        from numerus.matrices import Matrix
        self.assertIs(Matrix, numerus.Matrix)


    def test_vertex_imported(self):
        from numerus.matrices import create_vertex
        self.assertIs(create_vertex, numerus.create_vertex)



class StatsImportTests(TestCase):

    def test_mean_imported(self):
        from numerus.stats import mean
        self.assertIs(mean, numerus.mean)


    def test_median_imported(self):
        from numerus.stats import median
        self.assertIs(median, numerus.median)


    def test_mode_imported(self):
        from numerus.stats import mode
        self.assertIs(mode, numerus.mode)



class ChecksImportTests(TestCase):

    def test_is_numeric_imported(self):
        from numerus.checks import is_numeric
        self.assertIs(is_numeric, numerus.is_numeric)


    def test_are_numeric_imported(self):
        from numerus.checks import are_numeric
        self.assertIs(are_numeric, numerus.are_numeric)
