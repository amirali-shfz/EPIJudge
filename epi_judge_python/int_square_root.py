from test_framework import generic_test


def square_root(k: int) -> int:
    L, R = 0, int("9" * ((len(str(k)) // 2) + 1))
    while L <= R:
        mid = L + (R - L) // 2
        val = mid ** 2
        if val < k:
            L = mid + 1
        elif val > k:
            R = mid - 1
        else:
            return mid

    return R


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
