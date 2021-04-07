import operator
from typing import List
import random
from test_framework import generic_test


# [1, 2, 8, 5, 3, 9]    pivot = 3 @ 4
# [3, 2, 8, 5, 1, 9]
# [3, 2, 1, 5, 8, 9]
#

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:

    def partition_around(left, right, pivot):
        pivot_value = A[pivot]
        new_pivot_index = left
        A[pivot], A[right] = A[right], A[pivot]
        for i in range(left, right):
            if operator.gt(A[i], pivot_value):
                A[i], A[new_pivot_index] = A[new_pivot_index], A[i]
                new_pivot_index += 1
        A[new_pivot_index], A[right] = A[right], A[new_pivot_index]
        return new_pivot_index

    left_idx, right_idx = 0, len(A) - 1

    while left_idx <= right_idx:
        random_pivot = random.randint(left_idx, right_idx)
        pivot_idx = partition_around(left_idx, right_idx, random_pivot)
        if pivot_idx > k-1:
            right_idx = pivot_idx
        elif pivot_idx < k-1:
            left_idx = pivot_idx
        else:
            return A[pivot_idx]




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
