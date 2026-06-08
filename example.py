from sudoku_solver import solve

# Example from a book called "Sudoku impossible lvl 10"
# fortunately, for the algorithm I wrote, no sudoku board is impossible
board = [
    [8, 0, 0, 4, 0, 7, 0, 0, 1],
    [0, 0, 3, 0, 1, 0, 4, 0, 0],
    [0, 4, 0, 0, 0, 0, 0, 6, 0],
    [7, 0, 0, 0, 2, 0, 0, 0, 8],
    [0, 2, 0, 1, 0, 3, 0, 5, 0],
    [5, 0, 0, 0, 4, 0, 0, 0, 9],
    [0, 5, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 9, 0, 6, 0, 5, 0, 0],
    [3, 0, 0, 8, 0, 5, 0, 0, 2],
]

solved = solve(board)
for i in range(len(solved)):
    if i % 3 == 0:
        print("-" * 17)
    line_str = [str(x) for x in solved[i]]
    line_str[2] = f"{line_str[2]} | "
    line_str[5] = f"{line_str[5]} | "
    line_str[8] = f"{line_str[8]} | "
    print("".join(line_str))
print("-" * 17)
