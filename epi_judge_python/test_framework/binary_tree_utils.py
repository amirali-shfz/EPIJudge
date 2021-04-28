import collections

from test_framework.test_failure import PropertyName, TestFailure


class TreePath:
    def __init__(self, prev=None, to_left=False):
        self._prev = prev
        self._to_left = to_left

    def with_left(self):
        return TreePath(self, True)

    def with_right(self):
        return TreePath(self, False)

    def __str__(self):
        result = []
        node = self

        while node:
            result.append('->left' if node._to_left else '->right')
            node = node._prev

        result.reverse()
        result[0] = 'root'

        return ''.join(result)


def generate_preorder(tree):
    result = []
    s = [tree]

    while s:
        node = s.pop()
        if not node:
            continue

        result.append(node.data)
        s.append(node.right)
        s.append(node.left)

    return result


def generate_inorder(tree):
    result = []
    s = [tree]
    initial = True

    if not tree:
        return result

    while s:
        node = s.pop()

        if initial:
            initial = False
        else:
            result.append(node.data)
            node = node.right

        while node:
            s.append(node)
            node = node.left

    return result


def generate_postorder(tree):
    result = []
    s = [tree]

    while s:
        node = s.pop()
        if not node:
            continue

        result.append(node.data)
        s.append(node.left)
        s.append(node.right)

    result.reverse()

    return result


def find_node(tree, val):
    s = [tree]

    while s:
        node = s.pop()

        if not node:
            continue

        if node.data == val:
            return node

        s.append(node.left)
        s.append(node.right)

    return None


def must_find_node(tree, val):
    result = find_node(tree, val)
    if result is None:
        raise RuntimeError('{} was not found in the tree'.format(val))
    return result


def equal_binary_trees(tree1, tree2):
    s = [(tree1, tree2)]

    while s:
        node1, node2 = s.pop()

        if (node1 is None) != (node2 is None):
            return False

        if node1:
            if node1.data != node2.data:
                return False
            s.append((node1.left, node2.left))
            s.append((node1.right, node2.right))

    return True


def assert_equal_binary_trees(expected, result):
    s = [(expected, result, TreePath())]

    while s:
        expected, result, path = s.pop()

        expected_data = expected.data if expected is not None else None
        result_data = result.data if result is not None else None

        if expected_data != result_data:
            raise TestFailure() \
                .with_property(PropertyName.RESULT, result) \
                .with_property(PropertyName.EXPECTED, expected) \
                .with_mismatch_info(path, expected_data, result_data)

        if expected is not None and result is not None:
            s.append((expected.left, result.left, path.with_left()))
            s.append((expected.right, result.right, path.with_right()))


def binary_tree_to_string_pretty(root, val="data", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    return '\n'.join(lines)


def binary_tree_to_string(tree):
    result = ''
    nodes = collections.deque()
    visited = set()
    first = True
    null_nodes_pending = 0

    result += '['
    nodes.append(tree)

    while nodes:
        node = nodes.popleft()
        if id(node) in visited:
            raise RuntimeError('Detected a cycle in the tree')
        if node:
            if first:
                first = False
            else:
                result += ', '

            while null_nodes_pending:
                result += 'null, '
                null_nodes_pending -= 1

            result += '"{}"'.format(node.data)

            visited.add(id(node))
            nodes.append(node.left)
            nodes.append(node.right)
        else:
            null_nodes_pending += 1

    result += ']'
    return result


def binary_tree_height(tree):
    s = [(tree, 1)]
    height = 0

    while s:
        node, node_height = s.pop()
        if not node:
            continue

        height = max(height, node_height)
        s.append((node.right, node_height + 1))
        s.append((node.left, node_height + 1))

    return height


def binary_tree_size(tree):
    s = [tree]
    size = 0

    while s:
        node = s.pop()
        if not node:
            continue

        size += 1
        s.append(node.right)
        s.append(node.left)

    return size


# Python framework specific functions


def is_object_tree_type(tree):
    return tree and hasattr(tree, 'data') and \
           hasattr(tree, 'left') and hasattr(tree, 'right')


def convert_binary_tree_to_binary_tree_with_parent(tree):
    s = [(tree, None)]

    while s:
        node, parent = s.pop()
        if not node:
            continue

        node.parent = parent
        s.append((node.right, node))
        s.append((node.left, node))

    return tree


def strip_parent_link(tree):
    s = [tree]

    while s:
        node = s.pop()
        if node is None:
            continue

        node.parent = None
        s.append(node.left)
        s.append(node.right)


if __name__ == '__main__':
    from binary_tree_node import BinaryTreeNode as N

    tree = N(1, N(2, N(4), N(5, N(8), None)),
             N(3, N(6, None, N(9)), N(7, None, N(10, N(11), N(12)))))

    assert generate_inorder(tree) == [4, 2, 8, 5, 1, 6, 9, 3, 7, 11, 10, 12]
    assert generate_preorder(tree) == [1, 2, 4, 5, 8, 3, 6, 9, 7, 10, 11, 12]
    assert generate_postorder(tree) == [4, 8, 5, 2, 9, 6, 11, 12, 10, 7, 3, 1]

    path = TreePath().with_left().with_left().with_right().with_left()
    assert str(path) == "root->left->left->right->left"
