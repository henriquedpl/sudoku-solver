from itertools import product


example_sudoku = [
    [6, 8, 0,   4, 0, 2,   0, 9, 7],
    [7, 0, 0,   3, 0, 8,   0, 0, 1],
    [0, 0, 0,   0, 0, 0,   0, 0, 0],

    [9, 3, 0,   0, 0, 0,   0, 6, 2],
    [0, 0, 0,   0, 7, 0,   0, 0, 0],
    [1, 7, 0,   0, 0, 0,   0, 4, 9],

    [0, 0, 0,   0, 0, 0,   0, 0, 0],
    [2, 0, 0,   9, 0, 6,   0, 0, 4],
    [3, 4, 0,   1, 0, 7,   0, 8, 6]
]


def get_forbidden_numbers(s, i, j):
    line_numbers = [s[i][y] for y in range(0,9) if y != j]
    col_numbers = [s[x][j] for x in range(0,9) if x != i]
    square_numbers = [
        s[x[0]][x[1]] for x in product(
            list(range(int(i/3)*3, int(i/3)*3 + 3)),
            list(range(int(j/3)*3, int(j/3)*3 + 3))
        ) if (x[0],x[1]) != (i,j)
    ]
    return set(line_numbers + col_numbers + square_numbers)

def print_sudoku(s):
    for line in s:
        print(' '.join([str(x) for x in line]))

def get_next_square(i, j, fixed):
    j += 1
    if j == 9:
        j = 0
        i += 1
    if (i, j) in fixed:
        return get_next_square(i, j, fixed)
    return (i,j)

def solve(s):
    fixed = set()
    squares = []
    i, j = 0, 0
    while (i,j) != (8, 8):
        if s[i][j] in range(1, 10):
            fixed.add((i,j))
        elif not squares:
            squares.append({
                'pos': (i,j),
                'used': []
            })
        j += 1
        if j == 9:
            i += 1
            j = 0


    i, j = 0, 0
    if (i, j) in fixed:
        i,j = get_next_square(i, j, fixed)
    while (i, j) != (9, 0):
        current_square = squares[-1]
        i, j = current_square['pos']
        if len(current_square['used']) >= 9:
            s[i][j] = 0
            squares = squares[:-1]
            continue
        s[i][j] = 1 + len(current_square['used'])
        current_square['used'].append(s[i][j])
        forbidden_numbers = get_forbidden_numbers(s, i, j)
        if s[i][j] not in forbidden_numbers:
            i, j = get_next_square(i, j, fixed)
            squares.append(
                {
                    'pos': (i, j),
                    'used': []
                }
            )
    print_sudoku(s)
