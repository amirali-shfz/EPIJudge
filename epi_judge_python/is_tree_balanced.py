from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def traverse(node: BinaryTreeNode):
        if not node:
            return BalancedStatusWithHeight(True, -1)
        left = traverse(node.left)
        if not left.balanced:
            return left
        right = traverse(node.right)
        if not right.balanced:
            return right

        is_balanced = abs(left.height - right.height) <= 1
        return BalancedStatusWithHeight(is_balanced, max(left.height, right.height) + 1)

    return traverse(tree).balanced

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
