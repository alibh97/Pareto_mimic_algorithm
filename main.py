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
    for line in f:
        x, y, s = line.split('\t')  # extract x coordinate , y coordinate and score from rest of the lines
        nodes.append([float(x), float(y), int(s)])  # append nodes to nodes list
    return n, p, tmax, nodes  # return extracted variables


def initialization(nodes, no_paths):  # initialization func, construct m(no_paths) paths
    m_constructed_paths=[]  # the result of this func, m paths
    for i in range(no_paths):
        path=[]     # the path which will be made in this iteration and will be added to the final result list
        current_node = nodes[0]  # current node
        for j in range(len(nodes)-1):
            path.append(current_node)
            if j == 0:

                unvisited_feasible_nodes = len(nodes) - 2  # number of unvisited feasible nodes (μ)
                integer_parameter = 10  # an integer parameter (γ)
                minimum = min(unvisited_feasible_nodes, integer_parameter)  # minimum(l) is the min of μ and γ

                cost = 0  # the travel time of an edge
                reward = 0  # the reward of a node

                static_preference_values_start_node = static_preference_values(nodes, j)  # spvs of starting node

                sorted_static_preference_values_start_node = sorted(
                    static_preference_values_start_node.items(), key=lambda x: x[1], reverse=True)  # sort the dic of spvs,
                # in descending order

                # the next node is randomly chosen from the best min nodes in terms of their static preference values
                best_l_nodes = sorted_static_preference_values_start_node[0:min]
                next_node = best_l_nodes[random.random() * min]
                current_node = nodes[next_node[0]]

    x = []
    return x


# for any node i (1<= i <=n ) ,the nodes except 0, i,and n + 1 ,
# are sorted in descending order according to their static preference values,
# and then the first L nodes are stored into a list of node i,
# where L a sufficient large integer (in our experiment, L is chosen as 50).
def favorite_nodes(nodes):
    static_preference_values = []

    for i in range(1, len(nodes) - 1):
        spvs = static_preference_values(nodes, i)  # static preference values of other nodes for node i
        sorted_spvs=sorted(
            spvs.items(), key=lambda x: x[1], reverse=True)  # sort in descending order according to spvs
        L=50
        first_L_nodes=sorted_spvs[0:L]


# suppose current node is i ,static preference value of node j , is r_j / c_ij ,
# r_j is the reward of node j , and c_ij is the travel time of edge(i,j)
def static_preference_values(nodes, index):
    spvs = {}  # static preference values of nodes based on current node
    for j in range(1, len(nodes) - 1):
        if j != index:
            a = np.array([nodes[index][0], nodes[index][1]])  # coordinate of point we are in
            b = np.array(
                [nodes[j][0], nodes[j][1]])  # coordinate of point we want calculate it's static preference value
            c_ij = norm(a - b)  # distance between two nodes , as the travel time of the edge

            r_j = nodes[j][2]  # reward of node j

            spv = r_j / c_ij  # static preference value of node j

            spvs[j] = spv
    return spvs


if __name__ == '__main__':
    n, p, Tmax, Points = read_file('p1.2.b.txt')  # extract variables from the file ,
    # N is the number of vertices
    # P is the number of paths
    # Tmax is the available time budget per path
    # points is a list of nodes(points) with their x & y coordinates and scores

    # print('n= ', N,'\np= ',P,'\nTmax= ',Tmax,'\nPoints= ',Points)
    counter=1
    while(counter<31):
        print("norm "+str(counter)+"is: ")
        print(norm(np.array([Points[0][0], Points[0][1]]) - np.array([Points[counter][0], Points[counter][1]])))
        if norm(np.array([Points[0][0], Points[0][1]]) - np.array([Points[counter][0], Points[counter][1]]))<=5:
            print("YEEEESSSSSSSS   "+str(counter)+"")

        counter+=1

    print(norm(np.array([Points[27][0],Points[27][1]])-np.array([Points[31][0],Points[31][1]])))
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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
