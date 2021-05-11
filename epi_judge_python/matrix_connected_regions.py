from typing import List

from test_framework import generic_test
import collections

Cord = collections.namedtuple('Cord', ('x', 'y'))


def flip_color_dfs(X: int, Y: int, image: List[List[bool]]) -> None:
    val = image[X][Y]

    def flip(c):
        if not (0 <= c.x < len(image) and 0 <= c.y < len(image[0]) and image[c.x][c.y] == val):
            return
        image[c.x][c.y] = not image[c.x][c.y]
        [flip(Cord(c.x+d[0], c.y+d[1])) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

    flip(Cord(X, Y))
    return


def flip_color(X: int, Y: int, image: List[List[bool]]) -> None:
    val, q = image[X][Y], collections.deque()
    q.append(Cord(X, Y))
    while q:
        c = q.popleft()
        image[c.x][c.y] = not val
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = c.x+d[0], c.y+d[1]
            if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) and image[new_x][new_y] == val:
                q.append(Cord(new_x, new_y))

    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
