# Sudoku Solver

A simple Sudoku solver implemented in Python using a recursive backtracking algorithm.

The project focuses on a concise and educational implementation of the Sudoku-solving process. Given a valid and solvable 9×9 Sudoku puzzle, the solver fills the board in-place until a complete solution is obtained.

## Features

* Pure Python implementation
* Recursive backtracking algorithm
* No external dependencies
* Simple and easy-to-read codebase
* Unit tests using Python's built-in `unittest` framework

## Project Structure

```text
sudoku-solver/
├── README.md
├── sudoku_solver/
│   ├── __init__.py
│   └── solver.py
└── tests/
    └── __init__.py
    └── test_solver.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/sudoku-solver.git
cd sudoku-solver
```

## Usage

Import the `solve` function and provide a Sudoku board represented as a list of lists. Empty cells are denoted by `0`.

```python
from sudoku_solver import solve

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solve(board)

for row in board:
    print(row)
```

Output:

```text
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]
```

## Assumptions

The solver assumes that:

* The input board is a valid Sudoku puzzle.
* The puzzle has at least one solution.
* The board is represented as a 9×9 grid.
* Empty cells are represented by `0`.

Input validation is intentionally omitted to keep the implementation focused on the solving algorithm itself.

## Running Tests

The project uses Python's built-in `unittest` framework.

Run all tests from the project root with:

```bash
python -m unittest discover tests
```

## Algorithm

The solver uses recursive backtracking:

1. Find the next empty cell.
2. Try each digit from 1 to 9.
3. Check whether the digit satisfies Sudoku constraints.
4. Recursively continue solving the remaining board.
5. If a choice leads to a contradiction, backtrack and try another digit.

This approach systematically explores the search space until a complete solution is found.

## Educational Purpose

This project was created as a compact example of a constraint-satisfaction problem solved through backtracking. It is intended to be easy to read, modify, and extend for learning purposes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
