from swallow.different_local_search.operators.two_opt import two_opt_operator
from swallow.different_local_search.operators.exchange import exchange_operator

# todo the main local search needs to be changed
def different_local_search(solution,route,nodes):
    two_opt_operator(solution,route,nodes)
    print('two_opt: ',solution[0])
    print('two_opt: ',solution[1])
    exchange_operator(solution,route,nodes)
    print('exchang: ',solution[0])
    print('exchang: ',solution[1])

