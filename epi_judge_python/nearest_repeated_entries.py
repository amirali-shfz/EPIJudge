import collections
from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    last_seen, closest = {}, -1

    for i in range(len(paragraph)):
        if paragraph[i] in last_seen:
            closest = min(i - last_seen[paragraph[i]], closest) if closest != -1 else i - last_seen[paragraph[i]]
        last_seen[paragraph[i]] = i
    return closest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
