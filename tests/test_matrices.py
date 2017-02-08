from unittest import TestCase
from numerus.matrix import Matrix

class MatrixCreationTests(TestCase):

    def test_can_make_matrix(self):
        matrix = Matrix([1, 2, 3], [4, 5, 6])
        self.assertEqual(matrix._rows, ([1, 2, 3], [4, 5, 6]))
