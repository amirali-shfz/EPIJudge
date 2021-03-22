from typing import List, Tuple

from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap: List[Tuple[int, int]] = []

    sorted_arrays_iterators = [iter(x) for x in sorted_arrays]
    for index, it in enumerate(sorted_arrays_iterators):
        val = next(it)
        if val is not None:
            heapq.heappush(min_heap, (val, index))

    result = []
    while min_heap:
        val, index = heapq.heappop(min_heap)
        result.append(val)
        next_it = next(sorted_arrays_iterators[index], None)
        if next_it is not None:
            heapq.heappush(min_heap, (next_it, index))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
