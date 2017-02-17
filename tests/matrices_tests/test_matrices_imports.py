from unittest import TestCase
import numerus.matrices

class MatrixImportTests(TestCase):

    def test_matrix_imported(self):
        from numerus.matrices.matrix import Matrix
        self.assertIs(Matrix, numerus.matrices.Matrix)


    def test_vertex_imported(self):
        from numerus.matrices.matrix import create_vertex
        self.assertIs(create_vertex, numerus.matrices.create_vertex)
