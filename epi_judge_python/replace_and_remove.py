import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    s = ['a', 'b', 'c', 'b', 'c']
    size = 5
    i, write = 0, 0
    while write < size and i < size:
        if s[i] == 'a':
            write += 2
        elif s[i] != 'b':
            write += 1
        i += 1

    print(i)
    print(write)

    i -= 1
    write -= 1

    while i > 0 and write >= 0:
        print('')
        print(i)
        print(write)
        if s[i] == 'a':
            s[write] = 'd'
            if write >= 0:
                s[write - 1] = 'd'
            write -= 2
        elif s[i] != 'b':
            s[write] = s[i]
            write -= 1
        i -= 1



    # while i < size and write >= 0:
    #     print('')
    #     print(i)
    #     print(write)
    #     print('1')
    #     if s[i] == 'a':
    #         print('12')
    #         s[write] = 'd'
    #         print('13')
    #         if write >= 0:
    #             print('14')
    #             s[write - 1] = 'd'
    #         write -= 2
    #     elif s[i] != 'b':
    #         print('15')
    #         s[write] = s[i]
    #         print('16')
    #         write -= 1
    #     i += 1
    # print(s)
    return s




@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
