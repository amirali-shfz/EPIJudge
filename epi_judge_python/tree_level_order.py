from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    queue = []

    def traverse(node: BinaryTreeNode, cur_depth):
        if node is None:
            return
        if cur_depth >= len(queue):
            queue.append([])

        queue[cur_depth].append(node.data)
        traverse(node.left, cur_depth + 1)
        traverse(node.right, cur_depth + 1)

    traverse(tree, 0)
    return queue


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
