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
    constructed_paths = []  # the result of this function

    fav_nodes = favorite_nodes(nodes)  # make a list of favorite nodes for each node


    # find unvisited feasible nodes based on the start node (node 0)
    starting_unvisited_feasible_nodes = find_unvisited_feasible(nodes[1:(len(nodes) - 1)], [nodes[0]])



    # at most m path ( m = number of path = number of vehicles)
    for i in range(no_paths):
        current_node = nodes[0]  # a path always starts with node 0, so the current node is node 0
        path = [
            current_node]  # the path which will be made in this iteration and will be added to the final result list(
        # m_constructed_paths)

        integer_parameter = 10  # The integer parameter (γ)

        # number of unvisited feasible nodes (μ)
        no_unvisited_feasible_nodes = len(starting_unvisited_feasible_nodes)

        minimum = min(no_unvisited_feasible_nodes, integer_parameter)  # minimum(l) is the min of μ and γ
        # if l (l=minimum) is nonzero,then the next node is randomly chosen from the
        # best l (l=minimum) nodes in terms of their static preference values
        while minimum != 0:
            # for node 0 , we do differently and not doing in favorite nodes way
            print(current_node)
            if current_node[3] == 0:
                # randomly choose from unvisited feasible nodes
                index = int(random.random() * no_unvisited_feasible_nodes)
                next_node = starting_unvisited_feasible_nodes[index]
                current_node = next_node  # replace current node by next node
                path.append(current_node)  # add it to the path

                # pop the new node from starting unvisited feasible nodes, because in a solution ,
                # any node can be visited at most one time
                starting_unvisited_feasible_nodes.pop(index)

                # why we need this variable? because in the following,
                # we find unvisited feasible nodes based on middle nodes (node i to node n)
                middle_unvisited_feasible_nodes = find_unvisited_feasible(starting_unvisited_feasible_nodes, path)
                # number of unvisited feasible nodes (μ)
                no_unvisited_feasible_nodes = len(middle_unvisited_feasible_nodes)

                # minimum(l) is the min of μ and γ (Integer Parameter)
                minimum = min(no_unvisited_feasible_nodes, integer_parameter)
            # for other nodes we do based on favorite nodes
            else:
                # get favorite nodes of current node
                current_node_favorite_nodes = fav_nodes[current_node[3] - 1]

                # the next node is randomly chosen from the best l nodes in terms of their static preference values
                best_l_nodes = current_node_favorite_nodes[0:minimum]

                # randomly choose from best l (l=minimum of  μ and γ) nodes
                index = int(random.random() * minimum)
                next_node = best_l_nodes[index]
                current_node = nodes[next_node[0]]
                path.append(current_node)

                starting_unvisited_feasible_nodes.pop(index)

                middle_unvisited_feasible_nodes = find_unvisited_feasible(middle_unvisited_feasible_nodes, path)

                # number of unvisited feasible nodes (μ)
                no_unvisited_feasible_nodes = len(middle_unvisited_feasible_nodes)

                # minimum(l) is the min of μ and γ (Integer Parameter)
                minimum = min(no_unvisited_feasible_nodes, integer_parameter)


        # if l ( l= minimum) is zero, one path is finished at the ending route
        path.append(nodes[len(nodes)-1])  # add ending node to path

        if len(path)>2:
            constructed_paths.append(path)

        if len(starting_unvisited_feasible_nodes)==0:
            break

    return constructed_paths



# for any node i (1<= i <=n ) ,the nodes except 0, i,and n + 1 ,
# are sorted in descending order according to their static preference values,
# and then the first L nodes are stored into a list of node i,
# where L a sufficient large integer (in our experiment, L is chosen as 50).
def favorite_nodes(nodes):
    result = []  # the result is a list of 'First L Nodes' for each node i ( 1 <= i <= n)

    for i in range(1, len(nodes) - 1):
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


# this function finds unvisited feasible nodes out of unvisited feasible nodes so far and return them
def find_unvisited_feasible(unvisited_feasible_so_far, path):
    current_node = path[len(path) - 1]

    # calculate the cost of path from start to current node
    cost_start_to_i = 0
    for i in range(len(path)):
        if (i + 1) <= (len(path) - 1):
            a = np.array([path[i][0], path[i][1]])
            b = np.array([path[i + 1][0], path[i + 1][1]])
            c_ab = norm(a - b)  # cost going from a to b
            cost_start_to_i += c_ab

    unvisited_feasible_nodes = []  # this list will be returned
    for unvisited in unvisited_feasible_so_far:
        # calculate cost of going from current node to node j (1 <= j <= n)
        cost_i_to_j = norm(
            np.array([current_node[0], current_node[1]]) - np.array([unvisited[0], unvisited[1]]))

        # calculate cost of going from node j to ending node(n+1) (1 <= j <= n)
        cost_j_to_ending_node = norm(
            np.array([unvisited[0], unvisited[1]]) - np.array([Points[no_nodes - 1][0], Points[no_nodes - 1][1]]))

        cost_i_to_j_to_ending_node = cost_i_to_j + cost_j_to_ending_node

        # if cost of going from current node(i) to j (1 <= j <= n) to ending node(n+1) be less than Tmax,
        # then node j is a feasible node
        if cost_i_to_j_to_ending_node + cost_start_to_i <= Tmax:
            unvisited_feasible_nodes.append(unvisited)
    return unvisited_feasible_nodes


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


if __name__ == '__main__':
    no_nodes, no_paths, Tmax, Points = read_file('p1.2.b.txt')  # extract variables from the file ,
    # first is the number of vertices
    # seconds is the number of paths
    # Tmax is the available time budget per path
    # points is a list of nodes(points) with their x & y coordinates and scores
    print('n= ', no_nodes,'\np= ',no_paths,'\nTmax= ',Tmax,'\nPoints= ',Points)
    print(initialization(Points))
    # ss(Points,0)
    # static_preference_values_start_node = static_preference_values(Points, 0)  # spvs of starting node
    #
    # sorted_static_preference_values_start_node = sorted(
    #     static_preference_values_start_node.items(), key=lambda x: x[1],
    #     reverse=True)
    # print(sorted_static_preference_values_start_node)
    # counter = 1
    # while (counter < 31):
    #     print("norm " + str(counter) + "is: ")
    #     print(norm(np.array([Points[0][0], Points[0][1]]) - np.array([Points[counter][0], Points[counter][1]])))
    #     if norm(np.array([Points[0][0], Points[0][1]]) - np.array([Points[counter][0], Points[counter][1]])) <= 5:
    #         print("YEEEESSSSSSSS   " + str(counter) + "")
    #
    #     counter += 1
    #
    # print(norm(np.array([Points[27][0], Points[27][1]]) - np.array([Points[31][0], Points[31][1]])))

    # dic=dict([(1,21),(2,30),(3,15),(4,9),(5,32)])
    #
    # sort_orders = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    # line 1 in algorithm 1
    IS = []  # incumbent solution needs to be empty at first, it's a set of solution(x)s

    # line 2 in algorithm 1
    Xb = []  # the best so far solution

    # line 3 in algorithm 1
    # for i in range(N) :   # N is the maximum number of incumbent solutions
    #     # line 4 in algorithm 1
    #     x = initialization()
    #
    #     # line 5 in algorithm 1
    #     IS.append(x)

    # print(find_unvisited_feasible(Points[1:31],[Points[0]]))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
