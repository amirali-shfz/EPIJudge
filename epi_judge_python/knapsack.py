import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    max_val = [[0] * (capacity+1) for _ in items]

    for item in range(len(items)):
        for available_capacity in range(capacity+1):
            without_item = max_val[item-1][available_capacity]
            with_item = (max_val[item-1][available_capacity-items[item].weight] + items[item].value
                         if items[item].weight <= available_capacity else 0)
            max_val[item][available_capacity] = max(without_item, with_item)

    return max_val[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
