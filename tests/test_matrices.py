from unittest import TestCase
from numerus.matrix import Matrix

class MatrixCreationTests(TestCase):

    def test_can_make_matrix(self):
        matrix = Matrix((1, 2, 3), (4, 5, 6))
        self.assertEqual(matrix._rows, ((1, 2, 3), (4, 5, 6)))


    def test_all_sequences_converted_to_tuple(self):
        matrix = Matrix([1, 2, 3], (4, 5, 6))
        self.assertEqual(matrix._rows, ((1, 2, 3), (4, 5, 6)))


    def test_matrix_needs_sequences(self):
        with self.assertRaises(TypeError):
            Matrix([1, 2, 3], "456")
