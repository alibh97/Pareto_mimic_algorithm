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


from pareto_update.update import update
from swallow.swallow_operator import swallow_operator
from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio

from algorithm1 import algorithm1



if __name__ == '__main__':

    algorithm1()
    # print('n= ', no_nodes, '\np= ', no_paths, '\nTmax= ', Tmax, '\nPoints= ', Points)
    #
    # # line 1 in algorithm 1
    # IS = []  # incumbent solution needs to be empty at first, it's a set of solution(x)s
    #
    # # line 2 in algorithm 1
    # Xb = []  # the best so far solution
    #
    # N = 10  # N is the maximum number of incumbent solutions
    # # line 3 in algorithm 1
    # for counter in range(N):  # N is the maximum number of incumbent solutions
    #     # line 4 in algorithm 1
    #     x = initialization(Points)
    #     print('initil:',x[0])
    #     print('initil:',x[1])
    #     if not (IS.__contains__(x)) and len(x)>0:
    #         IS.append(x)
    #
    #     # line 6 in algorithm 1
    #     if Fx(x) > Fx(Xb):
    #         Xb = list(x)
    # # line 8 in algorithm 1
    # for j in range(1):
    #
    #
    #     # line 9 in algorithm 1
    #     IS_size = len(IS)  # the size of IS (U)
    #
    #     # line 10 in algorithm 1
    #     Q = []  # an  auxiliary set (Q)
    #
    #     # line 11 in algorithm 1
    #     for i in range(IS_size):
    #         # line 12 in algorithm 1
    #         x= mimic_operator(Points, IS[i])
    #         print('mimic: ', x)
    #
    #         # line 13 in algorithm 1
    #         local_search(x, Points)
    #
    #         print('local: ',x)
    #
    #         # line 14 in algorithm 1
    #         swallow_operator(x, Points)
    #         print('swalow: ',x)
    #         # print('swallow: ', x[0])
    #         # print('swallow: ', x[1])
    #
    #         # line 15 in algorithm 1
    #         if not (Q.__contains__(x)):
    #             Q.append(x)
    #
    #         # line 16 in algorithm 1
    #         if Fx(x) > Fx(Xb):
    #             Xb = list(x)
    #         print(j,i)
    #
    #     # todo update
    #     union_of_Q_and_IS=[i for i in IS if i not in Q]
    #     union_of_Q_and_IS+=Q
    #     IS=update(union_of_Q_and_IS,Xb)
    #     for e in IS:
    #         print(e)