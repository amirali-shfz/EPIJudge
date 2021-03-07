from typing import List, Tuple

from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    min_heap: List[Tuple[int, int]] = []

    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    for i, it in enumerate(sorted_arrays_iters):
        first = next(it, None)
        if first is not None:
            heapq.heappush(min_heap, (first, i))

    result = []
    while min_heap:
        smallest_value, smallest_index = heapq.heappop(min_heap)
        smallest_iter = sorted_arrays_iters[smallest_index]
        result.append(smallest_value)
        next_element = next(smallest_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_index))

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
