from unittest import TestCase
from unittest.mock import patch, Mock
from numerus.matrix import Matrix, can_add, can_multiply
from numerus.exceptions import MatrixError

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


    def test_can_add_matrices(self):
        matrix1 = Matrix((1, 2, 3), (4, 5, 6))
        matrix2 = Matrix((1, 2, 3), (4, 5, 6))
        matrix3 = matrix1 + matrix2
        self.assertEqual(matrix3.rows(), ((2, 4, 6), (8, 10, 12)))


    @patch("numerus.matrix.can_add")
    def test_cannot_add_if_function_says_no(self, mock_check):
        mock_check.return_value = False
        matrix1 = Matrix((1, 2, 3), (4, 5, 6))
        matrix2 = Matrix((1, 2, 3), (4, 5, 6))
        with self.assertRaises(MatrixError):
            matrix1 + matrix2


    def test_can_subtract_matrices(self):
        matrix1 = Matrix((-1, 2, 0), (0, 3, 6))
        matrix2 = Matrix((0, -4, 3), (9, -4, -3))
        matrix3 = matrix1 - matrix2
        self.assertEqual(matrix3.rows(), ((-1, 6, -3), (-9, 7, 9)))


    @patch("numerus.matrix.can_add")
    def test_cannot_add_if_function_says_no(self, mock_check):
        mock_check.return_value = False
        matrix1 = Matrix((-1, 2, 0), (0, 3, 6))
        matrix2 = Matrix((0, -4, 3), (9, -4, -3))
        with self.assertRaises(MatrixError):
            matrix1 - matrix2



class MatrixMultiplicationTests(TestCase):

    def test_can_multiply_function(self):
        matrix1 = Mock(Matrix)
        matrix2 = Mock(Matrix)
        matrix1.size.return_value = (4, 3)
        matrix2.size.return_value = (3, 2)
        self.assertTrue(can_multiply(matrix1, matrix2))
        matrix1.size.return_value = (3, 4)
        matrix2.size.return_value = (2, 3)
        self.assertFalse(can_multiply(matrix1, matrix2))
