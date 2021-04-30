from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:

    def place_queen(row):
        if row == n:
            result.append(list(board))
            return
        for column in range(n):
            if all(abs(column - c) not in (0, row - r) for r, c in enumerate(board[:row])):
                board[row] = column
                place_queen(row + 1)

    result = []
    board = [0] * n
    place_queen(0)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
