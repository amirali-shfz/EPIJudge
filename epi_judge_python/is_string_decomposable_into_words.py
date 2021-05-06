import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    lengths = [-1] * len(domain)
    for i in range(len(lengths)):
        if domain[:i+1] in dictionary:
            lengths[i] = i+1
        if lengths[i] == -1:
            for j in range(i):
                if lengths[j] != -1 and domain[j+1: i+1] in dictionary:
                    lengths[i] = i - j

    sol = []
    if lengths[-1] != -1:
        right = len(lengths) - 1
        while right >= 0:
            sol.append(domain[right + 1 - lengths[right]:right + 1])
            right -= lengths[right]
        sol = sol[::-1]
    return sol


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
