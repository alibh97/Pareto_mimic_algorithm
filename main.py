# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
from numpy.linalg import norm
import numpy as np
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def read_file(name):
    f = open(name, 'r')  # open file
    n = int(f.readline().removeprefix('n '))  # read n = number of vertices
    p = int(f.readline().removeprefix('m '))  # read p = number of paths
    tmax = float(f.readline().removeprefix('tmax '))  # read Tmax = available time budget per path

    nodes = []  # a list to append the nodes(points) in it
    index = 0  # make index for nodes

    for line in f:
        x, y, s = line.split('\t')  # extract x coordinate , y coordinate and score from rest of the lines
        nodes.append([float(x), float(y), int(s), index])  # append nodes to nodes list
        index += 1
    return n, p, tmax, nodes  # return extracted variables


def initialization(nodes):  # initialization func, construct at most m(no_paths) paths
    # line 1 , Algorithm 2
    # set currentNode := 0
    current_node = nodes[0]

    fav_nodes = favorite_nodes(nodes)  # make a list of favorite nodes for each node

    unvisited_nodes = nodes[1:(no_nodes - 1)]  # all unvisited nodes except 0 and n+1

    paths = []

    # line 2 , Algorithm 2
    for i in range(no_paths):
        remaining_time = Tmax  # time limit of path

        # construct the ith path
        # line 4 , Algorithm 2
        path = []

        # line 5 , Algorithm 2
        while True:
            # line 6 , Algorithm 2
            flag = False

            # line 14 , Algorithm 2
            if not flag:
                # line 15 , Algorithm 2
                # number of unvisited feasible nodes (μ)
                if path.__len__() == 0:
                    # always for finding the number of unvisited feasible nodes, if
                    # the path was empty we assume the current node is 0
                    no_unvisited_feasible_nodes = find_no_unvisited_feasible(unvisited_nodes, remaining_time, nodes[0])
                else:
                    no_unvisited_feasible_nodes = find_no_unvisited_feasible(unvisited_nodes, remaining_time,
                                                                             current_node)

                # line 16 , Algorithm 2
                # minimum(l) is the min of μ and γ (Integer Parameter)
                minimum = min(no_unvisited_feasible_nodes, integer_parameter)
                # line 17 , Algorithm 2
                if minimum > 0:
                    # line 18 , Algorithm 2
                    # get favorite nodes of current node
                    current_node_favorite_nodes = fav_nodes[current_node[3]]
                    # find feasible favorite nodes of current node
                    current_node_feasible_favorite_nodes = find_feasibles(current_node_favorite_nodes, remaining_time,
                                                                          current_node)
                    # the next node is randomly chosen from the best l nodes in terms of their static preference values
                    best_l_nodes = current_node_feasible_favorite_nodes[0:minimum]

                    # randomly choose from best l (l=minimum of  μ and γ) nodes
                    index = int(random.random() * minimum)
                    node = best_l_nodes[index]

                    # line 19 , Algorithm 2
                    next_node = nodes[node[0]]
                    flag = True

                    # calculate the cost ( time ) of going from current node, to next node
                    cost_i_to_j = norm(
                        np.array([current_node[0], current_node[1]]) - np.array([next_node[0], next_node[1]]))

                    remaining_time -= cost_i_to_j  # update remaining time

                    unvisited_nodes.remove(next_node)  # update unvisited nodes
                    delete_from_favorite(fav_nodes, next_node)  # update favorite nodes

            # line 22 , Algorithm 2
            if flag:
                # line 23 , Algorithm 2
                path.append(next_node)

                # line 24 , Algorithm 2
                current_node = next_node
            else:
                break
        paths.append(path)
    return paths


def mimic_operator(nodes, solution):
    # line 1 , Algorithm 2
    # set currentNode := 0
    current_node = nodes[0]

    fav_nodes = favorite_nodes(nodes)  # make a list of favorite nodes for each node

    unvisited_nodes = nodes[1:(no_nodes - 1)]  # all unvisited nodes except 0 and n+1

    paths = []

    # line 2 , Algorithm 2
    for i in range(no_paths):
        remaining_time = Tmax  # time limit of path

        # construct the ith path
        # line 4 , Algorithm 2
        path = []

        # line 5 , Algorithm 2
        while True:
            # line 6 , Algorithm 2
            flag = False

            # line 7 , Algorithm 2
            r = random.uniform(0, 1)  # a uniformly distributed random number r ∈ [0, 1]
            # line 8 , Algorithm 2
            if r < similarity_ratio:  # similarity ratio ( α )
                # line 9 , Algorithm 2
                # set node := the next node of currentNode in xI(solution passed to this function)
                node, is_for_next_path = find_next(solution, current_node)

                # line 10 , Algorithm 2
                if is_feasible(current_node, node, remaining_time, paths, path):
                    # calculate the cost ( time ) of going from current node, to next node
                    if path.__len__() == 0:
                        # if the node be the first node of path , the current node is cone 0
                        cost_i_to_j = norm(
                            np.array([nodes[0][0], nodes[0][1]]) - np.array([node[0], node[1]]))
                    else:
                        cost_i_to_j = norm(
                            np.array([current_node[0], current_node[1]]) - np.array([node[0], node[1]]))

                    remaining_time -= cost_i_to_j  # update remaining time
                    unvisited_nodes.remove(node)  # update unvisited nodes
                    delete_from_favorite(fav_nodes, node)
                    # line 11 , Algorithm 2
                    next_node = node
                    flag = True

            # line 14 , Algorithm 2
            if not flag:
                # line 15 , Algorithm 2
                # number of unvisited feasible nodes (μ)
                if path.__len__() == 0:
                    # always for finding the number of unvisited feasible nodes, if
                    # the path was empty we assume the current node is 0
                    no_unvisited_feasible_nodes = find_no_unvisited_feasible(unvisited_nodes, remaining_time, nodes[0])
                else:
                    no_unvisited_feasible_nodes = find_no_unvisited_feasible(unvisited_nodes, remaining_time,
                                                                             current_node)
                # line 16 , Algorithm 2
                # minimum(l) is the min of μ and γ (Integer Parameter)
                minimum = min(no_unvisited_feasible_nodes, integer_parameter)
                # line 17 , Algorithm 2
                if minimum > 0:
                    # line 18 , Algorithm 2
                    # get favorite nodes of current node
                    current_node_favorite_nodes = fav_nodes[current_node[3]]

                    # find feasible favorite nodes of current node
                    current_node_feasible_favorite_nodes = find_feasibles(current_node_favorite_nodes, remaining_time,
                                                                          current_node)

                    # the next node is randomly chosen from the best l nodes in terms of their static preference values
                    best_l_nodes = current_node_feasible_favorite_nodes[0:minimum]

                    # randomly choose from best l (l=minimum of  μ and γ) nodes
                    index = int(random.random() * minimum)
                    node = best_l_nodes[index]

                    # line 19 , Algorithm 2
                    next_node = nodes[node[0]]
                    flag = True

                    # calculate the cost ( time ) of going from current node, to next node
                    cost_i_to_j = norm(
                        np.array([current_node[0], current_node[1]]) - np.array([next_node[0], next_node[1]]))

                    remaining_time -= cost_i_to_j  # update remaining time

                    unvisited_nodes.remove(next_node)  # update unvisited nodes
                    delete_from_favorite(fav_nodes, next_node)  # update favorite nodes

            # line 22 , Algorithm 2
            if flag:
                # line 23 , Algorithm 2
                path.append(next_node)

                # line 24 , Algorithm 2
                current_node = next_node
            else:
                break
        paths.append(path)
    return paths


# def local_search(nodes,solution):

# exchange unvisited operator
def exchange_unvisited_operator(solution, nodes):
    # find unvisited nodes
    unvisited_nodes = list(nodes[1:len(nodes) - 1])
    for path in solution:
        unvisited_nodes = [i for i in unvisited_nodes if i not in path]

    find_better_solution = True
    while find_better_solution:
        flag = False

        for path in solution:
            if flag:
                break
            for node in path:
                if flag:
                    break
                for unvisited in unvisited_nodes:
                    tmp_path = list(path)
                    tmp_path[path.index(node)] = unvisited

                    if calculate_total_travel_time(tmp_path,nodes) <= Tmax:  # it is feasible
                        if unvisited[2] > node[2]:  # so it can increase total
                            # received reward
                            solution[solution.index(path)] = tmp_path
                            unvisited_nodes.remove(unvisited)
                            flag = True
                            break
                    else:
                        if unvisited_nodes.index(unvisited) == (len(unvisited_nodes) - 1) and \
                                path.index(node) == (len(path) - 1) and solution.index(path) == (len(solution) - 1):
                            find_better_solution = False


def insertion_operator(solution, nodes):
    # find unvisited nodes
    unvisited_nodes = list(nodes[1:len(nodes) - 1])
    for path in solution:
        unvisited_nodes = [i for i in unvisited_nodes if i not in path]

    while True:
        feasible_nodes = find_feasibles_for_insert(solution, unvisited_nodes, nodes)
        if len(feasible_nodes) == 0:
            # there is no feasible node to be inserted
            break

        sorted_largest_dpv_feasible_nodes = dynamic_preference_values(solution, feasible_nodes, nodes)

        # At each step, the feasible node with the largest dynamic
        # preference value is chosen and inserted into the best position of the incumbent solution
        feasible_node_with_largest_dpv = nodes[sorted_largest_dpv_feasible_nodes[0][0]]

        # index of best position for insert
        path_index = sorted_largest_dpv_feasible_nodes[0][1][0]
        node_index = sorted_largest_dpv_feasible_nodes[0][1][1]

        # inserted into the best position of the incumbent solution
        solution[path_index].insert(node_index, feasible_node_with_largest_dpv)

        # update list of unvisited nodes
        unvisited_nodes.remove(feasible_node_with_largest_dpv)


def dynamic_preference_values(solution, feasible_nodes, nodes):
    # list of dynamic preference values with node id's and best position index
    dpvs = []

    for node in feasible_nodes:
        # ΔT (x, i, k) be the increment of travel time caused by
        # inserting i into the kth best position

        # calculate and sort delta Ts ( ΔT (x, i, k) ) based on increment of travel time in ascending order
        sorted_delta_t_for_node = calculate_delta(solution, node, nodes)

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


# ΔT (x, i, k) be the increment of travel time caused by
# inserting i into the kth best position
def calculate_delta(solution, feasible_node, nodes):
    delta_t = []
    solution_travel_time = 0
    for path in solution:
        solution_travel_time += calculate_total_travel_time(path, nodes)

    for path in solution:
        for i in range(len(path) + 1):
            tmp_path = list(path)

            tmp_path.insert(i, feasible_node)

            new_path_travel_time = calculate_total_travel_time(tmp_path, nodes)

            if new_path_travel_time <= Tmax:
                new_solution_travel_time = new_path_travel_time

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


def find_feasibles_for_insert(solution, unvisited_nodes, nodes):
    feasible_nodes = []
    for node in unvisited_nodes:
        flag = False
        for path in solution:
            if flag:
                break
            tmp_path = list(path)
            for i in range(len(path) + 1):
                tmp_path.insert(i, node)
                new_path_time = calculate_total_travel_time(tmp_path, nodes)
                if new_path_time <= Tmax:
                    feasible_nodes.append(node)
                    flag = True
                    break
                else:
                    tmp_path = list(path)

    return feasible_nodes


# relocate operator
def relocate_operator(solution, nodes):
    finding_better_solution = True
    while finding_better_solution:
        flag = False
        for path1 in solution:
            if flag:
                break
            travel_time_path1 = calculate_total_travel_time(path1, nodes)
            for node1 in path1:
                if flag:
                    break
                relocate_node = node1
                current_path1 = list(path1)
                current_path1.remove(relocate_node)
                new_travel_time_path1 = calculate_total_travel_time(current_path1, nodes)
                reduction_time_path1 = travel_time_path1 - new_travel_time_path1
                for path2 in solution:
                    if flag:
                        break
                    if path1 != path2:
                        travel_time_path2 = calculate_total_travel_time(path2, nodes)
                        for i in range(len(path2) + 1):
                            current_path2 = list(path2)
                            current_path2.insert(i, relocate_node)
                            new_travel_time_path2 = calculate_total_travel_time(current_path2, nodes)
                            increased_time_path2 = new_travel_time_path2 - travel_time_path2
                            if increased_time_path2 < reduction_time_path1 and \
                                    new_travel_time_path2 <= Tmax and \
                                    new_travel_time_path1 <= Tmax:
                                solution[solution.index(path1)] = current_path1
                                solution[solution.index(path2)] = current_path2
                                flag = True
                                break
                            else:
                                if i == len(path2) and \
                                        solution.index(path2) == (len(solution) - 2) and \
                                        path1.index(node1) == (len(path1) - 1) and \
                                        solution.index(path1) == (len(solution) - 1):
                                    finding_better_solution = False
    return solution


# cross move operator
def cross_operator(solution, nodes):
    finding_better_solution = True
    while finding_better_solution:
        flag = False
        for path1 in solution:
            if flag:
                break
            smallest_travel_time_path1 = calculate_total_travel_time(path1, nodes)
            for i in range(len(path1) + 1):
                if flag:
                    break
                path1_slice1 = path1[0:i]
                path1_slice2 = path1[i:]

                for path2 in solution:
                    if flag:
                        break
                    if path1 != path2:
                        smallest_travel_time_path2 = calculate_total_travel_time(path2, nodes)

                        for k in range(len(path2) + 1):
                            path2_slice1 = path2[0:k]
                            path2_slice2 = path2[k:]

                            tmp_path1 = path1_slice1 + path2_slice2
                            tmp_path2 = path2_slice1 + path1_slice2

                            new_travel_time1 = calculate_total_travel_time(tmp_path1, nodes)
                            new_travel_time2 = calculate_total_travel_time(tmp_path2, nodes)
                            if ((new_travel_time1 < smallest_travel_time_path1 and
                                 new_travel_time2 < smallest_travel_time_path2) or
                                    (new_travel_time1 < smallest_travel_time_path2 and
                                     new_travel_time2 < smallest_travel_time_path1)):
                                solution[solution.index(path1)] = tmp_path1
                                solution[solution.index(path2)] = tmp_path2
                                flag = True
                                break
                            else:
                                if k == len(path2) and \
                                        solution.index(path2) == (len(solution) - 2) and \
                                        i == len(path1) and \
                                        solution.index(path1) == (len(solution) - 1):
                                    finding_better_solution = False
    return solution


# exchange move operator
def exchange_operator(solution, nodes):
    flag2 = False
    while True:
        flag = False
        for path1 in solution:
            if flag:
                break
            smallest_travel_time_path1 = calculate_total_travel_time(path1, nodes)
            current_path1 = list(path1)
            for node1 in path1:
                if flag:
                    break
                index_node_in_path1 = path1.index(node1)
                for path2 in solution:
                    if flag:
                        break
                    if path1 != path2:
                        current_path2 = list(path2)
                        smallest_travel_time_path2 = calculate_total_travel_time(path2, nodes)
                        for node2 in path2:
                            index_node2_in_path2 = path2.index(node2)

                            current_path1[index_node_in_path1] = node2
                            current_path2[index_node2_in_path2] = node1
                            new_travel_time1 = calculate_total_travel_time(current_path1, nodes)
                            new_travel_time2 = calculate_total_travel_time(current_path2, nodes)
                            if new_travel_time1 < smallest_travel_time_path1 and \
                                    new_travel_time2 < smallest_travel_time_path2:
                                solution[solution.index(path1)] = current_path1
                                solution[solution.index(path2)] = current_path2
                                flag = True
                                break
                            else:
                                if path2.index(node2) == (len(path2) - 1) and \
                                        solution.index(path2) == (len(solution) - 2) and \
                                        path1.index(node1) == (len(path1) - 1) and \
                                        solution.index(path1) == (len(solution) - 1):
                                    flag2 = True

                                current_path1 = list(path1)
                                current_path2 = list(path2)
        if flag2:
            break
    return solution


# 2_opt operator in local search
def two_opt_operator(solution, nodes):
    for path in solution:

        smallest_travel_time = calculate_total_travel_time(path, nodes)
        no_nodes_to_swap = len(path)
        current_path = path
        while True:
            flag = False
            c = 0
            for i in range(no_nodes_to_swap - 1):
                if flag:
                    break
                for k in range(i + 1, no_nodes_to_swap):
                    new_path = two_opt_swap(path, i, k)
                    new_travel_time = calculate_total_travel_time(new_path, nodes)
                    if new_travel_time < smallest_travel_time:
                        smallest_travel_time = new_travel_time
                        solution[solution.index(current_path)] = new_path
                        current_path = new_path

                        flag = True
                        break
                c = i
            if c == (no_nodes_to_swap - 2):
                break

    return solution


def two_opt_swap(path, i, k):
    new_path = []
    for c in range(i):
        new_path.append(path[c])

    for c in range(k, i - 1, -1):
        new_path.append(path[c])

    for c in range(k + 1, len(path)):
        new_path.append(path[c])
    return new_path


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


# this func deletes the chosen next node from all node's favorite nodes, and update fav_nodes list
def delete_from_favorite(favorite__nodes, next_node):
    for nodes in favorite__nodes:
        for node in nodes:
            if node[0] == next_node[3]:
                nodes.remove(node)


# this func find feasible nodes out of favorite nodes of current node
def find_feasibles(current_node_favorite_nodes, remaining_time, current_node):
    current_node_feasible_favorite_nodes = []
    for favorite_node in current_node_favorite_nodes:
        cost_i_to_j = norm(
            np.array([current_node[0], current_node[1]])
            - np.array([Points[favorite_node[0]][0], Points[favorite_node[0]][1]]))

        cost_j_to_end = norm(
            np.array([Points[favorite_node[0]][0], Points[favorite_node[0]][1]]) - np.array(
                [Points[no_nodes - 1][0], Points[no_nodes - 1][1]]))

        # if condition be TRUE, so this favorite node is feasible
        if (cost_i_to_j + cost_j_to_end) <= remaining_time:
            current_node_feasible_favorite_nodes.append(favorite_node)

    return current_node_feasible_favorite_nodes


# this func tell us whether the node is feasible or not
def is_feasible(current_node, node, remaining_time, paths, path):
    if path.__contains__(node):
        return False
    for p in paths:
        if p.__contains__(node):
            return False
    if len(node) == 0:
        return False
    cost_i_to_j = norm(
        np.array([current_node[0], current_node[1]])
        - np.array([node[0], node[1]]))

    cost_j_to_end = norm(
        np.array([node[0], node[1]]) - np.array([Points[no_nodes - 1][0], Points[no_nodes - 1][1]]))
    if (cost_i_to_j + cost_j_to_end) <= remaining_time:
        return True
    else:
        return False


# this func, finds next node in a solution
def find_next(solution, node):
    next_node = []  # result of this func
    flag = False  # this flag will be true in case the next node be the first item of the next path
    for path in solution:
        # when node 0, the next node is the first node of first path
        if node[3] == 0:
            next_node = path[0]
            break
        if flag:
            next_node = path[0]
            break
        if path.__contains__(node):
            index = list(path).index(node)
            size_of_path = len(list(path))

            if index + 1 < size_of_path:  # so the next node is in this path
                next_node = path[index + 1]
            else:  # the next node is in the next path so the flag will be true
                flag = True
    return next_node, flag


# for any node i (1<= i <=n ) ,the nodes except 0, i,and n + 1 ,
# are sorted in descending order according to their static preference values,
# and then the first L nodes are stored into a list of node i,
# where L a sufficient large integer (in our experiment, L is chosen as 50).
def favorite_nodes(nodes):
    result = []  # the result is a list of 'First L Nodes' for each node i ( 1 <= i <= n)

    for i in range(len(nodes) - 1):
        spvs = static_preference_values(nodes, i)  # static preference values of other nodes for node i
        sorted_spvs = sorted(
            spvs.items(), key=lambda x: x[1], reverse=True)  # sort in descending order according to spvs
        L = 50
        first_L_nodes = sorted_spvs[0:L]
        result.append(first_L_nodes)
    return result


# suppose current node is i ,static preference value of node j , is r_j / c_ij ,
# r_j is the reward of node j , and c_ij is the travel time of edge(i,j)
def static_preference_values(nodes, index):
    spvs = {}  # static preference values of nodes based on current node
    for j in range(1, len(nodes) - 1):
        if j != index:
            a = np.array([nodes[index][0], nodes[index][1]])  # coordinate of current node
            b = np.array(
                [nodes[j][0], nodes[j][1]])  # coordinate of point we want calculate it's static preference value
            c_ij = norm(a - b)  # distance between two nodes , as the travel time of the edge

            r_j = nodes[j][2]  # reward of node j

            spv = r_j / c_ij  # static preference value of node j

            spvs[j] = spv
    return spvs


# this function finds number of unvisited feasible nodes out of unvisited nodes so far and return it
def find_no_unvisited_feasible(unvisited_so_far, remaining_time, current_node):
    no_unvisited_feasible_nodes = 0  # this will be returned as result

    for unvisited in unvisited_so_far:
        # calculate cost of going from current node i to next node j (1 <= j <= n)
        cost_i_to_j = norm(
            np.array([current_node[0], current_node[1]]) - np.array([unvisited[0], unvisited[1]]))

        # calculate cost of going from next node j to ending node n+1 (1 <= j <= n)
        cost_j_to_end = norm(
            np.array([unvisited[0], unvisited[1]]) - np.array([Points[no_nodes - 1][0], Points[no_nodes - 1][1]]))

        # if cost of going from current node(i) to next node j (1 <= j <= n) plus
        # cost of going from next node j to ending node n+1, be less than remaining time,
        # then node j is a feasible node
        if (cost_i_to_j + cost_j_to_end) <= remaining_time:
            no_unvisited_feasible_nodes += 1

    return no_unvisited_feasible_nodes


def ss(nodes, index):
    a = np.array([nodes[index][0], nodes[index][1]])  # coordinate of current node
    b = np.array(
        [nodes[17][0], nodes[17][1]])  # coordinate of point we want calculate it's static preference value
    c_ij = norm(a - b)  # distance between two nodes , as the travel time of the edge
    print("cost: " + str(c_ij))
    r_j = nodes[17][2]  # reward of node j
    print("rew: " + str(r_j))
    spv = r_j / c_ij  # static preference value of node j
    print("spv: " + str(spv))


# Fx is objective value of solution x, is the total received reward of these paths of x.
def Fx(solution):
    total_received_reward = 0
    for path in solution:
        for node in path:
            total_received_reward += node[2]
    return total_received_reward


if __name__ == '__main__':
    no_nodes, no_paths, Tmax, Points = read_file('p1.2.r.txt')  # extract variables from the file ,
    # first is the number of vertices , n
    # seconds is the number of paths , m
    # Tmax is the available time budget per path
    # points is a list of nodes(points) with their x & y coordinates and scores

    integer_parameter = 10  # The integer parameter (γ)
    similarity_ratio = 0.95  # similarity ratio ( α )

    print('n= ', no_nodes, '\np= ', no_paths, '\nTmax= ', Tmax, '\nPoints= ', Points)

    # line 1 in algorithm 1
    IS = []  # incumbent solution needs to be empty at first, it's a set of solution(x)s

    # line 2 in algorithm 1
    Xb = []  # the best so far solution

    N = 10  # N is the maximum number of incumbent solutions
    # line 3 in algorithm 1
    for counter in range(1):  # N is the maximum number of incumbent solutions
        # line 4 in algorithm 1
        x = initialization(Points)

        print('round ', counter, 'x= ', x)
        x = mimic_operator(Points, x)
        print('mimic: ', x)
        two_opt_operator(x, Points)
        print('two_opt: ', x)
        exchange_operator(x, Points)
        print('exchange: ', x)
        cross_operator(x, Points)
        print('cross: ', x)
        relocate_operator(x, Points)
        print('relocat: ', x)
        insertion_operator(x, Points)
        print('insertion: ', x)
        exchange_unvisited_operator(x,Points)
        print('unvisited: ',x)
        print(calculate_total_travel_time(x[0], Points))
        print(calculate_total_travel_time(x[1], Points))
        # line 5 in algorithm 1
        if not (IS.__contains__(x)):
            IS.append(x)

        # line 6 in algorithm 1
        if Fx(x) > Fx(Xb):
            Xb = x

    # line 8 in algorithm 1
    for j in range(3000):
        # line 9 in algorithm 1
        IS_size = len(IS)  # the size of IS (U)

        # line 10 in algorithm 1
        auxiliary_set = []  # an  auxiliary set (Q)

        # line 11 in algorithm 1
        # for i in range(IS_size):
        #     # line 12 in algorithm 1
        #     x=


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def localSearch(solution, nodes):
    two_opt_operator(solution, nodes)
    exchange_operator(solution, nodes)
    cross_operator(solution, nodes)
    relocate_operator(solution, nodes)
