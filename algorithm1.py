from numpy.linalg import norm
import numpy as np
import random

from initialization.initialization import initialization
from mimic.mimic_operator import mimic_operator
from local_search.local_search import local_search


from pareto_update.update import update
from swallow.swallow_operator import swallow_operator
from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio


def algorithm1():
    # line 1 in algorithm 1
    IS = []  # incumbent solution needs to be empty at first, it's a set of solution(x)s
    # line 2 in algorithm 1
    Xb = []  # the best so far solution
    N = 10  # N is the maximum number of incumbent solutions
    # line 3 in algorithm 1
    for counter in range(N):  # N is the maximum number of incumbent solutions
        x = initialization(Points) # line 4 in algorithm 1
        if not (IS.__contains__(x)) and len(x)>0: # line 5 in algorithm 1
            IS.append(x)
        if Fx(x) > Fx(Xb):  # line 6 in algorithm 1
            Xb = list(x)
    for j in range(3000):    # line 8 in algorithm 1
        # line 9 in algorithm 1
        IS_size = len(IS)  # the size of IS (U)
        # line 10 in algorithm 1
        Q = []  # an  auxiliary set (Q)
        for i in range(IS_size):   # line 11 in algorithm 1
            x= mimic_operator(Points, IS[i])  # line 12 in algorithm 1
            print('mimic:',x)
            local_search(x, Points)  # line 13 in algorithm 1
            print('local:',x)
            swallow_operator(x, Points) # line 14 in algorithm 1
            print('swalow:',x)
            if not (Q.__contains__(x)): # line 15 in algorithm 1
                Q.append(x)
            if Fx(x) > Fx(Xb):  # line 16 in algorithm 1
                Xb = list(x)
        union_of_Q_and_IS=[i for i in IS if i not in Q]
        union_of_Q_and_IS+=Q
        IS=update(union_of_Q_and_IS,Xb)  # line 18 in algorithm 1
        for i in IS:
            print('update:',i)



# Fx is objective value of solution x, is the total received reward of these paths of x.
def Fx(solution):
    total_received_reward = 0
    for path in solution:
        for node in path:
            total_received_reward += node[2]
    return total_received_reward

