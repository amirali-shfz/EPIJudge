import collections

from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    d = collections.Counter(s)
    return sum([v % 2 for v in d.values()]) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
