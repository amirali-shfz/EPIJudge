from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    
    def sym(left: BinaryTreeNode, right: BinaryTreeNode):
        if not left and not right:
            return True
        if not (left and right and left.data == right.data):
            return False

        left_sym = sym(left.left, right.right)
        right_sym = sym(left.right, right.left)
        return left_sym and right_sym

    return not tree or sym(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
