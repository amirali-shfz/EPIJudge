from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L

    even = even_iter = ListNode()
    odd = odd_iter = ListNode()

    even_iter, odd_iter = even_iter.next, odd_iter.next
    while L and even_iter and odd_iter:
        if L.data % 2 == 0:
            even_iter, even_iter, L = L, even_iter.next, L.next
        else:
            odd_iter, odd_iter, L = L, odd_iter.next, L.next

    # even_iter.next = odd

    return odd




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
