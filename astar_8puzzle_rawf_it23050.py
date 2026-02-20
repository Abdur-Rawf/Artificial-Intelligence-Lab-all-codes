"""
Lab: 8-Puzzle using A* Search
Customized by: Rawf (Student ID: it23050)

Note: Core function names `is_valid`, `is_goal`, `manhattan`, `astar` kept unchanged.
"""

import heapq
from typing import List, Tuple, Set

N_RAWF_IT23050 = 3

# moves: left, right, up, down
row_rawf = [0, 0, -1, 1]
col_rawf = [-1, 1, 0, 0]


def is_valid(x: int, y: int) -> bool:
    return 0 <= x < N_RAWF_IT23050 and 0 <= y < N_RAWF_IT23050


def is_goal(board: List[List[int]]) -> bool:
    goal_rawf_it23050 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal_rawf_it23050


def manhattan(board: List[List[int]]) -> int:
    h_rawf_it23050 = 0
    for i_rawf in range(N_RAWF_IT23050):
        for j_rawf in range(N_RAWF_IT23050):
            val_rawf = board[i_rawf][j_rawf]
            if val_rawf != 0:
                goal_r_rawf = (val_rawf - 1) // N_RAWF_IT23050
                goal_c_rawf = (val_rawf - 1) % N_RAWF_IT23050
                h_rawf_it23050 += abs(i_rawf - goal_r_rawf) + abs(j_rawf - goal_c_rawf)
    return h_rawf_it23050


def _board_key_rawf(board: List[List[int]]) -> Tuple[Tuple[int, ...], ...]:
    return tuple(map(tuple, board))


def astar(start_board: List[List[int]], x: int, y: int) -> None:
    """
    Prints the depth (number of moves) when a goal is found.
    """
    pq_rawf = []  # priority queue: (f, g, board, blank_x, blank_y)
    visited_rawf: Set[Tuple[Tuple[int, ...], ...]] = set()

    g_rawf = 0
    h_rawf = manhattan(start_board)
    f_rawf = g_rawf + h_rawf
    heapq.heappush(pq_rawf, (f_rawf, g_rawf, start_board, x, y))
    visited_rawf.add(_board_key_rawf(start_board))

    while pq_rawf:
        f_rawf, g_rawf, board_rawf, bx_rawf, by_rawf = heapq.heappop(pq_rawf)

        if is_goal(board_rawf):
            print("Solution found at depth:", g_rawf)
            for r_rawf in board_rawf:
                print(r_rawf)
            return

        for i_rawf in range(4):
            nx_rawf = bx_rawf + row_rawf[i_rawf]
            ny_rawf = by_rawf + col_rawf[i_rawf]

            if is_valid(nx_rawf, ny_rawf):
                new_board_rawf = [r[:] for r in board_rawf]
                new_board_rawf[bx_rawf][by_rawf], new_board_rawf[nx_rawf][ny_rawf] = (
                    new_board_rawf[nx_rawf][ny_rawf],
                    new_board_rawf[bx_rawf][by_rawf],
                )

                key_rawf = _board_key_rawf(new_board_rawf)
                if key_rawf not in visited_rawf:
                    visited_rawf.add(key_rawf)
                    new_g_rawf = g_rawf + 1
                    new_h_rawf = manhattan(new_board_rawf)
                    new_f_rawf = new_g_rawf + new_h_rawf
                    heapq.heappush(pq_rawf, (new_f_rawf, new_g_rawf, new_board_rawf, nx_rawf, ny_rawf))

    print("No solution found")


if __name__ == "__main__":
    start_board_rawf_it23050 = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
    # blank position is (2, 1) for this board
    astar(start_board_rawf_it23050, 2, 1)
