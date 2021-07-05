from swallow.different_local_search.different_local_search import different_local_search
from swallow.removal_procedure import removal_procedure
from swallow.functions import calculate_total_travel_time

def repair_procedure(solution,index_of_route_Rl,nodes):
    # local search is applied with a different acceptance condition
    is_solution_repaired=different_local_search(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if is_solution_repaired:
        return

    # Otherwise it will be further repaired by a removal procedure.
    removal_procedure(solution,index_of_route_Rl,nodes)
    print('solution: ',solution[0])
    print('solution: ',solution[1])
    print(calculate_total_travel_time(solution[index_of_route_Rl],nodes))