import unittest

from sudoku_solver import solve


class TestSudokuSolver(unittest.TestCase):
    def test_solver(self):
        example_sudoku = [
            [6, 8, 0, 4, 0, 2, 0, 9, 7],
            [7, 0, 0, 3, 0, 8, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [9, 3, 0, 0, 0, 0, 0, 6, 2],
            [0, 0, 0, 0, 7, 0, 0, 0, 0],
            [1, 7, 0, 0, 0, 0, 0, 4, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 9, 0, 6, 0, 0, 4],
            [3, 4, 0, 1, 0, 7, 0, 8, 6],
        ]

        answer = [
            [6, 8, 5, 4, 1, 2, 3, 9, 7],
            [7, 9, 2, 3, 6, 8, 4, 5, 1],
            [4, 1, 3, 7, 9, 5, 6, 2, 8],
            [9, 3, 8, 5, 4, 1, 7, 6, 2],
            [5, 2, 4, 6, 7, 9, 8, 1, 3],
            [1, 7, 6, 8, 2, 3, 5, 4, 9],
            [8, 6, 1, 2, 3, 4, 9, 7, 5],
            [2, 5, 7, 9, 8, 6, 1, 3, 4],
            [3, 4, 9, 1, 5, 7, 2, 8, 6],
        ]

        solved_board = solve(example_sudoku)
        self.assertEqual(solved_board, answer)


if __name__ == "__main__":
    unittest.main()
