import collections

from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_counter = collections.Counter(letter_text)
    magazine_counter = collections.Counter(magazine_text)
    for key in letter_counter.keys():
        if letter_counter[key] > magazine_counter[key]:
            return False
    return True


def is_letter_constructible_from_magazine_pythonic(letter_text: str,
                                                   magazine_text: str) -> bool:
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
