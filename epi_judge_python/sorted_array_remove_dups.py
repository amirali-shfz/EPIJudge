import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if not A:
        return 0

    jump, i = 0, 0
    cur = A[0] - 1

    while i < len(A):
        while i < len(A) and A[i] == cur:
            jump += 1
            i += 1
        if i < len(A):
            cur = A[i]
            A[i - jump] = A[i]
            i += 1

    return len(A) - jump



@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
