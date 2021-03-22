from typing import Iterator, List

from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    min_heap, result = [], []

    val = next(sequence, None)
    while k and val is not None:
        heapq.heappush(min_heap, val)
        val = next(sequence, None)
        k -= 1

    while min_heap:
        result.append(heapq.heappop(min_heap))
        if val is not None:
            heapq.heappush(min_heap, val)
        val = next(sequence, None)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
