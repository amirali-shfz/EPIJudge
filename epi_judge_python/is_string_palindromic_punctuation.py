from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1

    def isalpha(c):
        return (ord('a') <= ord(c.lower()) <= ord('z')) or (ord('0') <= ord(c) <= ord('9'))

    while l < r:
        if not isalpha(s[l]):
            l += 1
        elif not isalpha(s[r]):
            r -= 1
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l, r = l+1, r-1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
