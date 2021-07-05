import local_search.functions as functions
from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio


# exchange unvisited operator
def exchange_unvisited_operator(solution, nodes):
    # find unvisited nodes
    unvisited_nodes = list(nodes[1:len(nodes) - 1])
    for path in solution:
        unvisited_nodes = [i for i in unvisited_nodes if i not in path]

    find_better_solution = True
    while find_better_solution:
        flag = False

        for path in solution:
            if flag:
                break
            for node in path:
                if flag:
                    break
                tmp_unvisited=[]
                for uu in unvisited_nodes:
                    tmp_unvisited.append(uu)
                for unvisited in tmp_unvisited:
                    tmp_path =[]
                    for pp in path:
                        tmp_path.append(pp)
                    tmp_path[path.index(node)] = unvisited

                    if functions.calculate_total_travel_time(tmp_path, nodes) <= Tmax:  # it is feasible
                        if unvisited[2] > node[2]:  # so it can increase total
                            # received reward
                            solution[solution.index(path)] = tmp_path
                            unvisited_nodes.remove(unvisited)
                            flag = True
                            break
                    else:
                        print('len unvisited: ',len(unvisited_nodes),' index unvisited:',unvisited_nodes.index(unvisited))
                        print('len path: ',len(path),' ,index node: ',path.index(node))
                        print('len solution:',len(solution),' index path: ',solution.index(path))
                        if unvisited_nodes.index(unvisited) == (len(unvisited_nodes) - 1) and \
                                path.index(node) == (len(path) - 1) and solution.index(path) == (len(solution) - 1):
                            find_better_solution = False

    return solution

