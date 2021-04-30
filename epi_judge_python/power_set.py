from typing import List

from test_framework import generic_test, test_utils


# 
def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def add_remainder(cur, rem):
        sol.append(cur)
        for i, num in enumerate(rem):
            new_cur = list(cur)
            new_cur.append(num)
            add_remainder(new_cur, rem[i+1:])

    sol = []
    add_remainder([], input_set)
    return sol


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
