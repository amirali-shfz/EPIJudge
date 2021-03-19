from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    def binary_tree_helper(pre_new: List[int], in_new: List[int]):
        if not in_new and not pre_new:
            return None

        node = BinaryTreeNode(pre_new[0])
        if len(in_new) == 1:
            return node
        root_index = in_new.index(node.data)
        in_left = in_new[:root_index]
        in_right = in_new[root_index + 1:]
        node.left = binary_tree_helper(pre_new[1:len(in_left)+1], in_left)
        node.right = binary_tree_helper(pre_new[len(in_left)+1:], in_right)
        return node
    return binary_tree_helper(preorder, inorder)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
