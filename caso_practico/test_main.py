import unittest
from main import matrix_generator, rows_sum, columns_sum

class TestMatriz(unittest.TestCase):
    def test_matrix_generator(self):
        matrix = matrix_generator(3)
        self.assertEqual(len(matrix), 3)
        self.assertEqual(len(matrix[0]), 3)

    def test_rows_sum(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        row_sum = rows_sum(matrix)
        self.assertEqual(row_sum, [6, 15, 24])

    def test_columns_sum(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        column_sum = columns_sum(matrix)
        self.assertEqual(column_sum, [12, 15, 18])

if __name__ == "__main__":
    unittest.main()
