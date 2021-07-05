from file_content import no_nodes, no_paths, Tmax, Points, integer_parameter, similarity_ratio
from numpy.linalg import norm
import numpy as np
import random


# insert a node with largest dpv in solution
def insertion(nodes, solution, unvisited_nodes):
    sorted_largest_dpv_unvisited_nodes = dynamic_preference_values(solution, unvisited_nodes, nodes)
    # insert an unvisited node with the largest dynamic preference value
    unvisited_node_with_largest_dpv = nodes[sorted_largest_dpv_unvisited_nodes[0][0]]
    # index of best position for insert
    path_index = sorted_largest_dpv_unvisited_nodes[0][1][0]
    node_index = sorted_largest_dpv_unvisited_nodes[0][1][1]
    # inserted into the best position of the incumbent solution
    solution[path_index].insert(node_index, unvisited_node_with_largest_dpv)
    # update list of unvisited nodes
    unvisited_nodes.remove(unvisited_node_with_largest_dpv)

    # return the path which the node has been inserted in
    return path_index


# calculates dynamic preference value for nodes in the solution in descending order
def dynamic_preference_values(solution, unvisited_nodes, nodes):
    # list of dynamic preference values with node id's and best position index
    dpvs = []

    for node in unvisited_nodes:
        # ΔT (x, i, k) be the increment of travel time caused by
        # inserting i into the kth best position

        # calculate and sort delta Ts ( ΔT (x, i, k) ) based on increment of travel time in ascending order
        sorted_delta_t_for_node = calculate_delta(solution, node, nodes)

        # in my opinion best position is the position witch increases least amount of travel time
        # ΔT (x, i, 1)
        delta_t_best_position = sorted_delta_t_for_node[0][2]

        # ΔT (x, i, 3)
        if len(sorted_delta_t_for_node) > 2:
            delta_t_3th_best_position = sorted_delta_t_for_node[2][2]
        else:
            delta_t_3th_best_position = 0

        while True:
            # u ∈ (0, 1] is a uniformly distributed random number
            u = random.uniform(0, 1)
            if u != 0:
                break

        # r is reward of node i
        r = node[2]

        # The dynamic preference value of node i, denoted as D(x, i), is defined as
        # follows:
        # D(x, i) = (ΔT (x, i, 3) − ΔT (x, i, 1)) · r_i ^ u

        # ΔT (x, i, 3) − ΔT (x, i, 1) is the difference of travel time
        # obtained by inserting i into the third best and the best position.

        # dynamic preference value of node i
        dpv = (delta_t_3th_best_position - delta_t_best_position) * pow(r, u)

        # make a list with node id and the index of best position to insert in solution and dynamic preference value
        # of the node
        path_index = sorted_delta_t_for_node[0][0]
        node_index = sorted_delta_t_for_node[0][1]

        id_index_dpv = [node[3], [path_index, node_index], dpv]

        # add above list to dynamic preference values list
        dpvs.append(id_index_dpv)

    # dpvs list is sorted based on dpv of the nodes in descending order
    dpvs.sort(reverse=True, key=lambda e: e[2])
    return dpvs


def calculate_delta(solution, unvisited_node, nodes):
    delta_t = []
    solution_travel_time = 0
    for path in solution:
        solution_travel_time += calculate_total_travel_time(path, nodes)

    for path in solution:
        for i in range(len(path) + 1):
            tmp_path = list(path)

            tmp_path.insert(i, unvisited_node)

            new_solution_travel_time = calculate_total_travel_time(tmp_path, nodes)
            for path2 in solution:
                if path2 != path:
                    new_solution_travel_time += calculate_total_travel_time(path2, nodes)

            increment_of_travel_time = new_solution_travel_time - solution_travel_time

            # make the index
            path_index = solution.index(path)
            node_index = i
            delta_t.append([path_index, node_index, increment_of_travel_time])
    # SORT in ascending order according to increment of travel time
    delta_t.sort(key=lambda e: e[2])
    return delta_t


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


# this func tell us whether the solution is feasible or not
def is_solution_feasible(solution, nodes):
    answer = True
    for path in solution:
        if calculate_total_travel_time(path, nodes) > Tmax:
            answer = False
            break
    return answer
