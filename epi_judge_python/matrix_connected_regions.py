from typing import List

from test_framework import generic_test
import collections

Cord = collections.namedtuple('Cord', ('x', 'y'))


def flip_color(X: int, Y: int, image: List[List[bool]]) -> None:
    val = image[X][Y]

    def flip(c):
        if not (0 <= c.x < len(image) and 0 <= c.y < len(image[0]) and image[c.x][c.y] == val):
            return
        image[c.x][c.y] = not image[c.x][c.y]
        [flip(Cord(c.x+d[0], c.y+d[1])) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

    flip(Cord(X, Y))
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
