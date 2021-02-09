from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:

    dummy = sublist_head = ListNode(0, L)

    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy.next

    # if not L or L.data != 1:
    #     return L
    #
    # print('')
    # def p(j: ListNode):
    #     x = j
    #     while x:
    #         print(x.data, end='')
    #         if x.next:
    #             print(' -> ', end='')
    #         x = x.next
    #     print('')
    #
    # print('L: ')
    # p(L)
    # print('start: ' + str(start) + ' finish: ' + str(finish))
    #
    # dummy_head = sublist_head = ListNode(0, L)
    # for _ in range(1, start):
    #     sublist_head = sublist_head.next
    #
    # # Reverses sublist.
    # sublist_iter = sublist_head.next
    # print('sublist_head', end=' ')
    # p(sublist_head)
    # print('sublist_iter', end=' ')
    # p(sublist_iter)
    # print('----------------------')
    # for _ in range(finish - start):
    #
    #     temp = sublist_iter.next
    #
    #     print('temp        ', end=' ')
    #     p(temp)
    #
    #     sublist_iter.next = temp.next
    #
    #     print('sublist_iter', end=' ')
    #     p(sublist_iter)
    #
    #     temp.next = sublist_head.next
    #
    #     print('temp        ', end=' ')
    #     p(temp)
    #
    #     sublist_head.next = temp
    #
    #     print('sublist_head', end=' ')
    #     p(sublist_head)
    #
    #     print('')
    #
    # return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
