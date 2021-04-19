import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(left: BinaryTreeNode,
        right: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    left_parents = set()
    right_parents = set()

    while left or right:
        if left == right:
            return left

        if left:
            left_parents.add(left)
            left = left.parent
        if right:
            right_parents.add(right)
            right = right.parent

        if left in right_parents:
            return left
        if right in left_parents:
            return right



@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'lowest_common_ancestor_close_ancestor.py',
            'lowest_common_ancestor.tsv', lca_wrapper))
