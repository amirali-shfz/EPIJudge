from test_framework import generic_test
import functools
import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if num_as_string == '0':
        return num_as_string
    neg = num_as_string[0] == '-'
    num_as_string = num_as_string[neg:]
    num = functools.reduce(lambda a, b: a * b1 + string.hexdigits.index(b.lower()), num_as_string, 0)

    base = 1
    while num >= base:
        base *= b2
    base /= b2

    sol = []
    while base >= 1:
        dig = string.hexdigits[int(num // base)].upper()
        sol.append(dig)
        num %= base
        base /= b2

    return ('-' if neg else '') + ''.join(sol)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
