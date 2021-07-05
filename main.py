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
from local_search.operators.exchange import exchange_operator
from local_search.operators.cross import cross_operator
from local_search.operators.relocate import relocate_operator
from pareto_update.update import update
from swallow.swallow_operator import swallow_operator
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
    for counter in range(N):  # N is the maximum number of incumbent solutions
        # line 4 in algorithm 1
        x = initialization(Points)

        if not (IS.__contains__(x)):
            IS.append(x)

        # line 6 in algorithm 1
        if Fx(x) > Fx(Xb):
            Xb = list(x)

    # line 8 in algorithm 1
    for j in range(1):


        # line 9 in algorithm 1
        IS_size = len(IS)  # the size of IS (U)

        # line 10 in algorithm 1
        Q = []  # an  auxiliary set (Q)

        # line 11 in algorithm 1
        for i in range(IS_size):
            # line 12 in algorithm 1
            x= mimic_operator(Points, IS[i])
            print('mimic: ', x)

            # line 13 in algorithm 1
            local_search(x, Points)
            print('local: ',x)
            # line 14 in algorithm 1
            swallow_operator(x, Points)
            print('swalow: ',x)
            # print('swallow: ', x[0])
            # print('swallow: ', x[1])

            # line 15 in algorithm 1
            if not (Q.__contains__(x)):
                Q.append(x)

            # line 16 in algorithm 1
            if Fx(x) > Fx(Xb):
                Xb = list(x)
            print(j,i)

        # todo update
        union_of_Q_and_IS=[i for i in IS if i not in Q]
        union_of_Q_and_IS+=Q
        IS=update(union_of_Q_and_IS,Xb)
        for e in IS:
            print(e)