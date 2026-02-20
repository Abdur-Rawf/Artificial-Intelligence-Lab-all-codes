"""
Algorithms: Best-First Search for 8-Puzzle (using Manhattan distance)
Customized by: Rawf (Student ID: it23050) 

Note: Core algorithm function names (manhattan_distance, best_first_search, etc.)
kept unchanged (important).
"""

import heapq
from typing import List, Tuple, Dict, Set


goal_state_rawf_it23050: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Movement vectors (left, right, up, down)
row_rawf = [0, 0, -1, 1]
col_rawf = [-1, 1, 0, 0]


def manhattan_distance(current: List[List[int]], goal: List[List[int]]) -> int:
    pos_rawf_it23050: Dict[int, Tuple[int, int]] = {}
    for i_rawf in range(3):
        for j_rawf in range(3):
            pos_rawf_it23050[goal[i_rawf][j_rawf]] = (i_rawf, j_rawf)

    dist_rawf_it23050 = 0
    for i_rawf in range(3):
        for j_rawf in range(3):
            value_rawf = current[i_rawf][j_rawf]
            if value_rawf != 0:
                x_goal_rawf, y_goal_rawf = pos_rawf_it23050[value_rawf]
                dist_rawf_it23050 += abs(i_rawf - x_goal_rawf) + abs(j_rawf - y_goal_rawf)

    return dist_rawf_it23050


def find_blank(board: List[List[int]]) -> Tuple[int, int]:
    for i_rawf in range(3):
        for j_rawf in range(3):
            if board[i_rawf][j_rawf] == 0:
                return i_rawf, j_rawf
    raise ValueError("Invalid board: no blank (0) found.")


def board_to_tuple(board: List[List[int]]) -> Tuple[Tuple[int, ...], ...]:
    return tuple(tuple(r_rawf) for r_rawf in board)


def best_first_search(start: List[List[int]]) -> None:
    pq_rawf = []
    visited_rawf: Set[Tuple[Tuple[int, ...], ...]] = set()

    h_start_rawf = manhattan_distance(start, goal_state_rawf_it23050)
    heapq.heappush(pq_rawf, (h_start_rawf, start))

    while pq_rawf:
        h_rawf, current_rawf = heapq.heappop(pq_rawf)

        print("Heuristic =", h_rawf)
        for r_rawf in current_rawf:
            print(r_rawf)
        print()

        if current_rawf == goal_state_rawf_it23050:
            print("Goal Reached!")
            return

        visited_rawf.add(board_to_tuple(current_rawf))

        x_blank_rawf, y_blank_rawf = find_blank(current_rawf)

        for k_rawf in range(4):
            nx_rawf, ny_rawf = x_blank_rawf + row_rawf[k_rawf], y_blank_rawf + col_rawf[k_rawf]

            if 0 <= nx_rawf < 3 and 0 <= ny_rawf < 3:
                new_board_rawf = [r[:] for r in current_rawf]
                new_board_rawf[x_blank_rawf][y_blank_rawf], new_board_rawf[nx_rawf][ny_rawf] = (
                    new_board_rawf[nx_rawf][ny_rawf],
                    new_board_rawf[x_blank_rawf][y_blank_rawf],
                )

                if board_to_tuple(new_board_rawf) not in visited_rawf:
                    h_new_rawf = manhattan_distance(new_board_rawf, goal_state_rawf_it23050)
                    heapq.heappush(pq_rawf, (h_new_rawf, new_board_rawf))


if __name__ == "__main__":
    start_state_rawf_it23050 = [[1, 2, 3], [4, 6, 0], [7, 5, 8]]
    best_first_search(start_state_rawf_it23050)
