"""
Algorithms: BFS for 8-Puzzle (queue-based)
Customized by: Rawf (Student ID: it23050)

Note: Core algorithm function name `bfs` kept unchanged (important).
"""

from collections import deque


def bfs(start_state_rawf_it23050: str) -> str:
    goal_state_rawf_it23050 = "123456780"

    queue_rawf = deque([start_state_rawf_it23050])
    visited_rawf_it23050 = []

    while queue_rawf:
        current_state_rawf = queue_rawf.popleft()

        if current_state_rawf == goal_state_rawf_it23050:
            return "Goal Reached: " + current_state_rawf

        if current_state_rawf not in visited_rawf_it23050:
            visited_rawf_it23050.append(current_state_rawf)

            blank_index_rawf = current_state_rawf.index('0')

            # Move UP
            if blank_index_rawf > 2:
                next_state_list_rawf = list(current_state_rawf)
                next_state_list_rawf[blank_index_rawf], next_state_list_rawf[blank_index_rawf - 3] = (
                    next_state_list_rawf[blank_index_rawf - 3],
                    next_state_list_rawf[blank_index_rawf],
                )
                queue_rawf.append("".join(next_state_list_rawf))

            # Move DOWN
            if blank_index_rawf < 6:
                next_state_list_rawf = list(current_state_rawf)
                next_state_list_rawf[blank_index_rawf], next_state_list_rawf[blank_index_rawf + 3] = (
                    next_state_list_rawf[blank_index_rawf + 3],
                    next_state_list_rawf[blank_index_rawf],
                )
                queue_rawf.append("".join(next_state_list_rawf))

            # Move LEFT
            if blank_index_rawf % 3 != 0:
                next_state_list_rawf = list(current_state_rawf)
                next_state_list_rawf[blank_index_rawf], next_state_list_rawf[blank_index_rawf - 1] = (
                    next_state_list_rawf[blank_index_rawf - 1],
                    next_state_list_rawf[blank_index_rawf],
                )
                queue_rawf.append("".join(next_state_list_rawf))

            # Move RIGHT
            if blank_index_rawf % 3 != 2:
                next_state_list_rawf = list(current_state_rawf)
                next_state_list_rawf[blank_index_rawf], next_state_list_rawf[blank_index_rawf + 1] = (
                    next_state_list_rawf[blank_index_rawf + 1],
                    next_state_list_rawf[blank_index_rawf],
                )
                queue_rawf.append("".join(next_state_list_rawf))

    return "No Solution Found"


if __name__ == "__main__":
    start_state_rawf_it23050 = "123406758"
    print(bfs(start_state_rawf_it23050))
