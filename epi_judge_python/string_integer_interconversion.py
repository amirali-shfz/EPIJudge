from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools
import string


def int_to_string(x: int) -> str:
    neg = (x < 0)
    x = abs(x)
    mapping = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9'
    }
    s = ''
    while True:
        s += mapping[x % 10]
        if x == 0:
            break
        x //= 10

    if neg:
        s += '-'
    s = s[::-1]
    return s


def string_to_int(s: str) -> int:
    sign = -1 if s[0] == '-' else 1
    s = s.strip('-+')
    x = 0
    for index, i in enumerate(s):
        num = ord(i) - ord('0')
        x += (num * (10 ** (len(s) - index - 1)))

    return x * sign

    # x += [((ord(i) - ord('0'))*(10**(len(s)-index-1))) for index, i in enumerate(s)]


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
