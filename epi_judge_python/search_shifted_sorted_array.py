from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    L, R = 0, len(A) - 1

    while L < R:
        mid = L + (R - L) // 2
        if A[mid] > A[R]:
            L = mid + 1
        else:
            R = mid

    return L

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
