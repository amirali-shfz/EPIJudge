import collections

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def matches_constraints(node, lower=float('-inf'), higher=float('inf')):
        if not node:
            return True
        if not lower <= node.data <= higher:
            return False
        return matches_constraints(node.left, lower, node.data) and matches_constraints(node.right, node.data, higher)

    return matches_constraints(tree)


def is_binary_tree_bst_bfs(tree: BinaryTreeNode) -> bool:
    Bounds = collections.namedtuple('Bounds', ('lower', 'higher'))
    queue = [(tree, Bounds(float('-inf'), float('inf')))]
    while queue:
        node, bounds = queue.pop()
        if not bounds.lower <= node.data <= bounds.higher:
            return False
        if node.left:
            queue.append((node.left, Bounds(bounds.lower, node.data)))
        if node.right:
            queue.append((node.right, Bounds(node.data, bounds.higher)))

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst_bfs))
