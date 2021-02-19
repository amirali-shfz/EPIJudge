from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    p_map = {'{': '}', '[': ']', '(': ')'}

    for p in s:
        if p in p_map:
            stack.append(p)
        else:
            if not (stack and p == p_map[stack.pop()]):
                return False

    return len(stack) == 0

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
