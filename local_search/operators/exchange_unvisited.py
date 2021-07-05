import local_search.functions as functions
from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio


# exchange unvisited operator
def exchange_unvisited_operator(solution, nodes):

    # print('unvisited nodes at first:',unvisited_nodes , ' , len:',len(unvisited_nodes))
    find_better_solution = True
    while find_better_solution:
        # find unvisited nodes
        unvisited_nodes = list(nodes[1:len(nodes) - 1])
        for path in solution:
            unvisited_nodes = [i for i in unvisited_nodes if i not in path]

        flag = False

        for path in solution:

            if flag:
                break
            for node in path:
                if flag:
                    break
                for unvisited in unvisited_nodes:
                    tmp_path =[]
                    for pp in path:
                        tmp_path.append(pp)
                    tmp_path[path.index(node)] = unvisited
                    if functions.calculate_total_travel_time(tmp_path, nodes) <= Tmax:  # it is feasible
                        if unvisited[2] > node[2]:  # so it can increase total
                            # received reward
                            solution[solution.index(path)] = tmp_path
                            flag = True
                            break
                        else:
                            if (unvisited_nodes.index(unvisited) == (len(unvisited_nodes) - 1)) and \
                                    (path.index(node) == (len(path) - 1)) and (
                                    solution.index(path) == (len(solution) - 1)):
                                find_better_solution = False
                    else:
                        if (unvisited_nodes.index(unvisited) == (len(unvisited_nodes) - 1)) and \
                                (path.index(node) == (len(path) - 1)) and (solution.index(path) == (len(solution) - 1)):

                            find_better_solution = False

    return solution

