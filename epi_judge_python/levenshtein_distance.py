from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    dist = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
    dist[0] = [n for n in range(len(dist[0]))]
    for n in range(len(dist)):
        dist[n][0] = n

    for i in range(1, len(dist)):
        for j in range(1, len(dist[0])):
            dist[i][j] = min(1 + dist[i][j-1], 1 + dist[i-1][j], (A[j-1] != B[i-1]) + dist[i-1][j-1])

    return dist[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
