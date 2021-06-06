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

    paths = [None] * no_paths

    # line 2 , Algorithm 2
    for i in range(no_paths):
        remaining_time = Tmax  # time limit of path

        # construct the ith path
        # line 4 , Algorithm 2
        paths[i] = []

        # line 5 , Algorithm 2
        while True:
            # line 6 , Algorithm 2
            flag = False

            # line 14 , Algorithm 2
            if not flag:
                # line 15 , Algorithm 2
                # number of unvisited feasible nodes (μ)
                if paths[i].__len__() == 0:
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

                    # the next node is randomly chosen from the best l nodes in terms of their static preference values
                    best_l_nodes = current_node_favorite_nodes[0:minimum]

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
                paths[i].append(next_node)

                # line 24 , Algorithm 2
                current_node = next_node
            else:
                break
    return paths


def mimic_operator(nodes, solution):
    # line 1 , Algorithm 2
    # set currentNode := 0
    current_node = nodes[0]

    fav_nodes = favorite_nodes(nodes)  # make a list of favorite nodes for each node

    unvisited_nodes = nodes[1:(no_nodes - 1)]  # all unvisited nodes except 0 and n+1

    paths = [None] * no_paths

    # line 2 , Algorithm 2
    for i in range(no_paths):
        remaining_time = Tmax  # time limit of path

        # construct the ith path
        # line 4 , Algorithm 2
        paths[i] = []

        # line 5 , Algorithm 2
        while True:
            # line 6 , Algorithm 2
            flag = False

            # line 7 , Algorithm 2
            r = random.uniform(0, 1)  # a uniformly distributed random number r ∈ [0, 1]
            print('r= ',r)
            # line 8 , Algorithm 2
            if r < similarity_ratio:  # similarity ratio ( α )
                # line 9 , Algorithm 2
                # set node := the next node of currentNode in xI(solution passed to this function)
                node = find_next(solution, current_node)
                print('next node of :',current_node,' is: ',node)
                print('feasible? ',is_feasible(current_node, node, remaining_time))
                # line 10 , Algorithm 2
                if is_feasible(current_node, node, remaining_time):
                    # calculate the cost ( time ) of going from current node, to next node
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
                if paths[i].__len__() == 0:
                    # always for finding the number of unvisited feasible nodes, if
                    # the path was empty we assume the current node is 0
                    no_unvisited_feasible_nodes = find_no_unvisited_feasible(unvisited_nodes, remaining_time, nodes[0])
                else:
                    no_unvisited_feasible_nodes = find_no_unvisited_feasible(unvisited_nodes, remaining_time,
                                                                             current_node)
                print('no un fe nodes: ',no_unvisited_feasible_nodes)
                # line 16 , Algorithm 2
                # minimum(l) is the min of μ and γ (Integer Parameter)
                minimum = min(no_unvisited_feasible_nodes, integer_parameter)

                # line 17 , Algorithm 2
                if minimum > 0:
                    # line 18 , Algorithm 2
                    # get favorite nodes of current node
                    current_node_favorite_nodes = fav_nodes[current_node[3]]

                    # the next node is randomly chosen from the best l nodes in terms of their static preference values
                    best_l_nodes = current_node_favorite_nodes[0:minimum]

                    # randomly choose from best l (l=minimum of  μ and γ) nodes
                    index = int(random.random() * minimum)
                    node = best_l_nodes[index]

                    # line 19 , Algorithm 2
                    next_node = nodes[node[0]]
                    print('next is: ',next_node)
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
                paths[i].append(next_node)

                # line 24 , Algorithm 2
                current_node = next_node
            else:
                break
        print('remaining time: ',remaining_time)
    return paths


# this func deletes the chosen next node from all node's favorite nodes, and update fav_nodes list
def delete_from_favorite(favorite__nodes, next_node):
    for nodes in favorite__nodes:
        for node in nodes:
            if node[0] == next_node[3]:
                nodes.remove(node)


# this func tell us whether the node is feasible or not
def is_feasible(current_node, node, remaining_time):
    if len(node) ==0 :
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
            flag = False
        if path.__contains__(node):
            index = list(path).index(node)
            size_of_path = len(list(path))

            if index + 1 < size_of_path:  # so the next node is in this path
                next_node = path[index + 1]
            else:  # the next node is in the next path so the flag will be true
                flag = True
    return next_node


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
        print(mimic_operator(Points,x))
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
