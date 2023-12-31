from local_search.operators.two_opt import two_opt_operator

from local_search.operators.exchange import exchange_operator

from local_search.operators.cross import cross_operator

from local_search.operators.relocate import relocate_operator

from local_search.operators.insertion import insertion_operator

from local_search.operators.exchange_unvisited import exchange_unvisited_operator


def local_search(solutio, nodes):  # local search operator
    first_step_local_search(solutio, nodes)  # first step of local search
    second_step_local_search(solutio, nodes)  # second step of local search
# first step of local search
def first_step_local_search(solutio, nodes):
    while True:
        tmp_solution = list(solutio)
        two_opt_operator(solutio, nodes)
        exchange_operator(solutio, nodes)
        cross_operator(solutio, nodes)
        relocate_operator(solutio, nodes)
        # once all these operators cannot find an improved solution , the first step stops and the second step begins.
        if tmp_solution == solutio:
            break
# second step of local search
def second_step_local_search(solutio, nodes):
    while True:
        tmp_sol = []
        for i in range(len(solutio)):
            tmp_sol.append(solutio[i][:])
        insertion_operator(solutio, nodes)
        exchange_unvisited_operator(solutio, nodes)
        # Once both of the operators,used in the second step cannot find a better solution, local search stops
        if tmp_sol == solutio:
            break

