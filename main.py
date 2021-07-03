# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math
from numpy.linalg import norm
import numpy as np
import random

from initialization.initialization import initialization
from mimic.mimic_operator import mimic_operator
from local_search.local_search import local_search
from swallow.swallow_operator import swallow_operator
from local_search.operators.two_opt import two_opt_operator
from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


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
        two_opt_operator(x,Points)
        print('two_opt: ', x)
        # local_search(x, Points)
        # two_opt_operator(x, Points)
        # print('two_opt: ', x)
        # exchange_operator(x, Points)
        # print('exchange: ', x)
        # cross_operator(x, Points)
        # print('cross: ', x)
        # relocate_operator(x, Points)
        # print('relocat: ', x)
        # insertion_operator(x, Points)
        # print('insertion: ', x)
        # exchange_unvisited_operator(x, Points)
        # print('unvisited: ', x)
        # print(calculate_total_travel_time(x[0], Points))
        # print(calculate_total_travel_time(x[1], Points))
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
