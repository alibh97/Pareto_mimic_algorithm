from swallow.different_local_search.operators.two_opt import two_opt_operator
from swallow.different_local_search.operators.exchange import exchange_operator
from swallow.different_local_search.operators.cross import cross_operator
import swallow.functions as functions

# todo the main local search needs to be changed
def different_local_search(solution,route,nodes):
    print('travel0:',functions.calculate_total_travel_time(solution[route],nodes))
    two_opt_operator(solution,route,nodes)
    print('two_opt: ',solution[0])
    print('two_opt: ',solution[1])
    print('travel1:',functions.calculate_total_travel_time(solution[route],nodes))

    exchange_operator(solution,route,nodes)
    print('exchang: ',solution[0])
    print('exchang: ',solution[1])
    print('travel2:',functions.calculate_total_travel_time(solution[route],nodes))

    cross_operator(solution,route,nodes)
    print('cross:  ',solution[0])
    print('cross:  ',solution[1])
    print('travel3:',functions.calculate_total_travel_time(solution[route],nodes))


