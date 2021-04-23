from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    cur, aind, bind, intersection = None, 0, 0, []

    while aind < len(A) and bind < len(B):
        if A[aind] < B[bind]:
            aind += 1
        elif A[aind] > B[bind]:
            bind += 1
        else:
            if A[aind] != cur:
                intersection.append(A[aind])
                cur = A[aind]
            aind, bind = aind + 1, bind + 1

    return intersection


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
