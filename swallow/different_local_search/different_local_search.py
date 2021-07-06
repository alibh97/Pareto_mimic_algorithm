from swallow.different_local_search.operators.two_opt import two_opt_operator
from swallow.different_local_search.operators.exchange import exchange_operator
from swallow.different_local_search.operators.cross import cross_operator
from swallow.different_local_search.operators.relocate import relocate_operator
import swallow.functions as functions


# todo the main local search needs to be changed
def different_local_search(solution,index_of_route_Rl,nodes):

    two_opt_operator(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if functions.is_solution_feasible(solution,nodes):
        return True

    exchange_operator(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if functions.is_solution_feasible(solution,nodes):
        return True
    cross_operator(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if functions.is_solution_feasible(solution,nodes):
        return True

    relocate_operator(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if functions.is_solution_feasible(solution,nodes):
        return True
    # none of the operators could repair the solution,it will be further repaired by a removal procedure
    return False

