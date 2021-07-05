from swallow.different_local_search.operators.two_opt import two_opt_operator
from swallow.different_local_search.operators.exchange import exchange_operator
from swallow.different_local_search.operators.cross import cross_operator
from swallow.different_local_search.operators.relocate import relocate_operator
import swallow.functions as functions

# todo the main local search needs to be changed
def different_local_search(solution,index_of_route_Rl,nodes):
    print('travel0:',functions.calculate_total_travel_time(solution[index_of_route_Rl],nodes))


    two_opt_operator(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if functions.is_solution_feasible(solution,nodes):
        return True
    print('two_opt: ',solution[0])
    print('two_opt: ',solution[1])
    print('travel1:',functions.calculate_total_travel_time(solution[index_of_route_Rl],nodes))


    exchange_operator(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if functions.is_solution_feasible(solution,nodes):
        return True
    print('exchang: ',solution[0])
    print('exchang: ',solution[1])
    print('travel2:',functions.calculate_total_travel_time(solution[index_of_route_Rl],nodes))


    cross_operator(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if functions.is_solution_feasible(solution,nodes):
        return True
    print('cross:  ',solution[0])
    print('cross:  ',solution[1])
    print('travel3:',functions.calculate_total_travel_time(solution[index_of_route_Rl],nodes))


    relocate_operator(solution,index_of_route_Rl,nodes)

    # Once a local search operator repairs the solution (i.e., the solution becomes feasible), the
    # repair procedure is stopped
    if functions.is_solution_feasible(solution,nodes):
        return True
    print('reloc:  ',solution[0])
    print('reloc:  ',solution[1])
    print('travel4:',functions.calculate_total_travel_time(solution[index_of_route_Rl],nodes))

    # none of the operators could repair the solution,it will be further repaired by a removal procedure
    return False

