from unittest import TestCase
from numerus.matrix import Matrix, can_add

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


    def test_matrix_cannot_be_empty(self):
        with self.assertRaises(TypeError):
            Matrix()
        with self.assertRaises(TypeError):
            Matrix([], [])


    def test_sequences_must_be_equal_in_length(self):
        with self.assertRaises(ValueError):
            Matrix([1, 2, 3], [4, 5])


    def test_matrix_repr(self):
        matrix = Matrix((1, 2, 3), (4, 5, 6))
        self.assertEqual(str(matrix), "<Matrix (2×3)>")



class MatrixRowsAndColumnsTests(TestCase):

    def test_can_get_rows(self):
        matrix = Matrix((1, 2, 3), (4, 5, 6))
        self.assertEqual(matrix.rows(), ((1, 2, 3), (4, 5, 6)))


    def test_can_get_columns(self):
        matrix = Matrix((1, 2, 3), (4, 5, 6))
        self.assertEqual(matrix.columns(), ((1, 4), (2, 5), (3, 6)))


    def test_can_get_size(self):
        matrix = Matrix((1, 2, 3), (4, 5, 6))
        self.assertEqual(matrix.size(), (2, 3))



class MatrixAdditionTests(TestCase):

    def test_can_add_function(self):
        matrix1 = Matrix((1, 2, 3), (4, 5, 6))
        matrix2 = Matrix((1, 2, 3), (4, 5, 6))
        self.assertTrue(can_add(matrix1, matrix2))
        matrix2 = Matrix((1, 2, 3, 3.5), (4, 5, 6, 6.5))
        self.assertFalse(can_add(matrix1, matrix2))
