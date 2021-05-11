from typing import List

from test_framework import generic_test
import collections


def fill_surrounded_regions(board: List[List[str]]) -> None:
    Coord = collections.namedtuple('Coord', ('x', 'y'))

    def get_white_edge_coords(x_len, y_len):
        return [Coord(x, y) for y in range(y_len) for x in [0, x_len-1] if board[x][y] == "W"] + \
               [Coord(x, y) for x in range(x_len) for y in [0, y_len-1] if board[x][y] == "W"]
    edge_coords = get_white_edge_coords(len(board), len(board[0]))

    q = collections.deque(edge_coords)

    while q:
        c = q.popleft()
        board[c.x][c.y] = "R"
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = c.x + d[0], c.y + d[1]
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == "W":
                q.append(Coord(new_x, new_y))

    for x in range(len(board)):
        for y in range(len(board[0])):
            board[x][y] = "W" if board[x][y] == "R" else "B"

    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
