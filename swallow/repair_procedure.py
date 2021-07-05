from swallow.different_local_search.different_local_search import different_local_search

def repair_procedure(solution,route,nodes):
    # local search is applied with a different acceptance condition
    different_local_search(solution,route,nodes)
