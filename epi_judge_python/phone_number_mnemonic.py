from typing import List

from test_framework import generic_test, test_utils

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

def phone_mnemonic(phone_number: str) -> List[str]:
    nums = []

    def attach(cur, rem):
        if rem == '':
            nums.append(cur)
            return
        for c in MAPPING[int(rem[0])]:
            attach(cur + c, rem[1:])

    attach('', phone_number)
    return nums


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
