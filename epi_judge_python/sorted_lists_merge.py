from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def merge_two_sorted_lists(l: Optional[ListNode],
                           r: Optional[ListNode]) -> Optional[ListNode]:
    dummy_head = ListNode()
    dummy = dummy_head
    while l and r:
        if l.data < r.data:
            dummy.next = l
            l = l.next
        else:
            dummy.next = r
            r = r.next
        dummy = dummy.next
    if l:
        dummy.next = l
    elif r:
        dummy.next = r

    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
