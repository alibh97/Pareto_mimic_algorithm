from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio
from numpy.linalg import norm
import numpy as np
import random


def calculate_total_travel_time(path, nodes):
    current_node = nodes[0]
    travel_time = 0
    for node in path:
        cost_i_to_j = norm(
            np.array([current_node[0], current_node[1]])
            - np.array([node[0], node[1]]))
        travel_time += cost_i_to_j
        current_node = node

    end_node = nodes[no_nodes - 1]

    cost_i_to_j = norm(
        np.array([current_node[0], current_node[1]])
        - np.array([end_node[0], end_node[1]]))

    travel_time += cost_i_to_j

    return travel_time


def two_opt_swap(path, i, k):
    new_path = []
    for c in range(i):
        new_path.append(path[c])

    for c in range(k, i - 1, -1):
        new_path.append(path[c])

    for c in range(k + 1, len(path)):
        new_path.append(path[c])
    return new_path


# this func tell us whether the solution is feasible or not
def is_solution_feasible(solution, nodes):
    answer = True
    for path in solution:
        if calculate_total_travel_time(path, nodes) > Tmax:
            answer = False
            break
    return answer
