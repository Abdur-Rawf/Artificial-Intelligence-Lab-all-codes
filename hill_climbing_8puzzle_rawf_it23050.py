"""
Lab: 8-Puzzle using Hill Climbing (Manhattan Distance)
Customized by: Rawf (Student ID: it23050)

Note: Core names kept unchanged:
- class p8_board
- is_valid, is_goal, manhattan, hill_climbing
"""

from typing import List, Tuple

N_RAWF_IT23050 = 3


class p8_board:
    def __init__(self, board: List[List[int]], x: int, y: int, h: int):
        self.board = board
        self.x = x
        self.y = y
        self.h = h


row_rawf = [0, 0, -1, 1]
column_rawf = [-1, 1, 0, 0]


def is_valid(x: int, y: int) -> bool:
    return 0 <= x < N_RAWF_IT23050 and 0 <= y < N_RAWF_IT23050


def is_goal(board: List[List[int]]) -> bool:
    goal_rawf_it23050 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == goal_rawf_it23050


def manhattan(board: List[List[int]]) -> int:
    goal_pos_rawf = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
    }
    distance_rawf_it23050 = 0
    for i_rawf in range(N_RAWF_IT23050):
        for j_rawf in range(N_RAWF_IT23050):
            val_rawf = board[i_rawf][j_rawf]
            if val_rawf != 0:
                gx_rawf, gy_rawf = goal_pos_rawf[val_rawf]
                distance_rawf_it23050 += abs(i_rawf - gx_rawf) + abs(j_rawf - gy_rawf)
    return distance_rawf_it23050


def hill_climbing(start: List[List[int]], x: int, y: int) -> None:
    current_rawf = p8_board(start, x, y, manhattan(start))

    while True:
        if is_goal(current_rawf.board):
            print("Goal Found using Hill Climbing")
            for r_rawf in current_rawf.board:
                print(r_rawf)
            return

        neighbors_rawf = []
        for i_rawf in range(4):
            new_x_rawf = current_rawf.x + row_rawf[i_rawf]
            new_y_rawf = current_rawf.y + column_rawf[i_rawf]

            if is_valid(new_x_rawf, new_y_rawf):
                new_board_rawf = [r[:] for r in current_rawf.board]
                new_board_rawf[current_rawf.x][current_rawf.y], new_board_rawf[new_x_rawf][new_y_rawf] = (
                    new_board_rawf[new_x_rawf][new_y_rawf],
                    new_board_rawf[current_rawf.x][current_rawf.y],
                )

                h_rawf = manhattan(new_board_rawf)
                neighbors_rawf.append(p8_board(new_board_rawf, new_x_rawf, new_y_rawf, h_rawf))

        if not neighbors_rawf:
            print("No valid neighbors found")
            return

        best_rawf = min(neighbors_rawf, key=lambda s: s.h)

        if best_rawf.h >= current_rawf.h:
            print("Stuck at Local Maximum")
            for r_rawf in current_rawf.board:
                print(r_rawf)
            return

        current_rawf = best_rawf


if __name__ == "__main__":
    start_board_rawf_it23050 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8],
    ]
    # blank position is (2, 1) for this board
    hill_climbing(start_board_rawf_it23050, 2, 1)
