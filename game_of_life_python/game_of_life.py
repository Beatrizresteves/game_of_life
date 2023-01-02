import os
from time import sleep
from random import randint


def gen_grid(rows, cols):
    return [[0] * cols for r in range(rows)]


def randomize_grid(grid):
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            grid[r][c] = randint(0, 1)


def get_neighbors(matrix, x, y):
    s = 0 if matrix[x][y] == 0 else -1
    for _x in range(-1, 2):
        for _y in range(-1, 2):
            __x = x + _x
            __y = y + _y
            if (__x >= 0 and __y >= 0) and (__x < len(matrix) and __y < len(matrix[0])):
                s += matrix[__x][__y]
    return s


def print_grid(grid):
    for row in grid:
        for c in row:
            print("." if c == 0 else "#", end='')
        print()


def update_matrix(matrix):
    new_matrix = gen_grid(len(matrix), len(matrix[0]))
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            v = get_neighbors(matrix, r, c)
            new_matrix[r][c] = int(
                (matrix[r][c] == 0 and v == 3)
                or (matrix[r][c] == 1 and (not (v < 2 or v > 3)))
            )
    return new_matrix


def main():
    grid = gen_grid(9, 9)
    grid[3][4] = 1
    grid[4][4] = 1
    grid[5][4] = 1
    grid[4][3] = 1
    grid[4][5] = 1
    randomize_grid(grid)
    try:
        while True:
            print_grid(grid)
            grid = update_matrix(grid)
            sleep(0.3)
            os.system('clear')
    except KeyboardInterrupt:
        print('interrupted!')


if __name__ == '__main__':
    main()

