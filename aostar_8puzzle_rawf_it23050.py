"""
Lab: 8-Puzzle using AO* (AND-OR) style heuristic search
Customized by: Rawf (Student ID: it23050)

Note: Core class/method names kept unchanged:
- EightPuzzleAOStar
- get_manhattan_distance
- get_neighbors
- solve
"""

import copy
from typing import List, Tuple


class EightPuzzleAOStar:
    def __init__(self, start: List[List[int]], goal: List[List[int]]):
        self.start_rawf_it23050 = start
        self.goal_rawf_it23050 = goal
        # Kept for compatibility with the original report structure
        self.heuristic_dict_rawf = {}
        self.parent_rawf = {}

    def get_manhattan_distance(self, state: List[List[int]]) -> int:
        distance_rawf_it23050 = 0
        for i_rawf in range(3):
            for j_rawf in range(3):
                if state[i_rawf][j_rawf] != 0:
                    x_goal_rawf, y_goal_rawf = divmod(state[i_rawf][j_rawf] - 1, 3)
                    distance_rawf_it23050 += abs(x_goal_rawf - i_rawf) + abs(y_goal_rawf - j_rawf)
        return distance_rawf_it23050

    def get_neighbors(self, state: List[List[int]]) -> List[List[List[int]]]:
        neighbors_rawf = []
        x_rawf, y_rawf = next(
            (r, c)
            for r, row_list_rawf in enumerate(state)
            for c, v_rawf in enumerate(row_list_rawf)
            if v_rawf == 0
        )
        moves_rawf: List[Tuple[Tuple[int, int], str]] = [
            ((x_rawf - 1, y_rawf), "Up"),
            ((x_rawf + 1, y_rawf), "Down"),
            ((x_rawf, y_rawf - 1), "Left"),
            ((x_rawf, y_rawf + 1), "Right"),
        ]

        for (nx_rawf, ny_rawf), _move_name_rawf in moves_rawf:
            if 0 <= nx_rawf < 3 and 0 <= ny_rawf < 3:
                new_state_rawf = copy.deepcopy(state)
                new_state_rawf[x_rawf][y_rawf], new_state_rawf[nx_rawf][ny_rawf] = (
                    new_state_rawf[nx_rawf][ny_rawf],
                    new_state_rawf[x_rawf][y_rawf],
                )
                neighbors_rawf.append(new_state_rawf)

        return neighbors_rawf

    def solve(self) -> bool:
        # In the provided lab writeup, AO* is demonstrated similarly to a heuristic best-first expansion.
        open_list_rawf = [(self.get_manhattan_distance(self.start_rawf_it23050), self.start_rawf_it23050)]
        visited_rawf = []

        print("Searching for solution...")
        while open_list_rawf:
            open_list_rawf.sort(key=lambda t: t[0])
            h_rawf, current_rawf = open_list_rawf.pop(0)

            if current_rawf == self.goal_rawf_it23050:
                print("Goal Reached!")
                for r_rawf in current_rawf:
                    print(r_rawf)
                return True

            visited_rawf.append(current_rawf)

            for neighbor_rawf in self.get_neighbors(current_rawf):
                if neighbor_rawf not in visited_rawf:
                    cost_rawf = self.get_manhattan_distance(neighbor_rawf)
                    open_list_rawf.append((cost_rawf, neighbor_rawf))

        return False


if __name__ == "__main__":
    start_state_rawf_it23050 = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
    goal_state_rawf_it23050 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    solver_rawf = EightPuzzleAOStar(start_state_rawf_it23050, goal_state_rawf_it23050)
    solver_rawf.solve()
