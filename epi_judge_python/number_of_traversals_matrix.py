from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    M = [[1] * n] + [[0] * n for _ in range(m-1)]
    for i in range(m):
        M[i][0] = 1

    for i in range(1, m):
        for j in range(1, n):
            M[i][j] = M[i-1][j] + M[i][j-1]

    return M[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
