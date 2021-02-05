from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(l: Optional[ListNode],
                           r: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = tail = ListNode()
    while l and r:
        if l.data < r.data:
            tail.next = l
            l = l.next
        else:
            tail.next = r
            r = r.next
        tail = tail.next
    
    tail.next = l or r

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
