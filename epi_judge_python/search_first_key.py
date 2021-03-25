from typing import List
import bisect
from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    result, L, R = -1, 0, len(A) - 1

    while L <= R:
        mid = L + (R - L) // 2
        if A[mid] < k:
            L = mid + 1
        elif A[mid] == k:
            result = mid
            R = mid - 1
        else:
            R = mid - 1

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
