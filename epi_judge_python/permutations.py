from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    def permute(cur, remaining):
        if not remaining:
            sol.append(cur)
            return
        for num in remaining:
            new_cur = list(cur)
            new_cur.append(num)
            new_rem = list(remaining)
            new_rem.remove(num)
            permute(new_cur, new_rem)

    sol = []
    permute([], A)
    return sol


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
