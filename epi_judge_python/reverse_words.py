import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # TODO - you fill in here.
    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]
    i = 0
    while i < len(s):
        l, r = i, i
        while r < len(s) and s[r] != ' ':
            r += 1
        i = r + 1
        r = (r - 1) if (r >= len(s) or s[r] == ' ') else r
        while l < r:
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
