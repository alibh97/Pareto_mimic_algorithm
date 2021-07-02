import local_search.functions as functions


# insertion operator
def insertion_operator(solution, nodes):
    # find unvisited nodes
    unvisited_nodes = list(nodes[1:len(nodes) - 1])
    for path in solution:
        unvisited_nodes = [i for i in unvisited_nodes if i not in path]

    while True:
        feasible_nodes = functions.find_feasibles_for_insert(solution, unvisited_nodes, nodes)
        if len(feasible_nodes) == 0:
            # there is no feasible node to be inserted
            break

        sorted_largest_dpv_feasible_nodes = functions.dynamic_preference_values(solution, feasible_nodes, nodes)

        # At each step, the feasible node with the largest dynamic
        # preference value is chosen and inserted into the best position of the incumbent solution
        feasible_node_with_largest_dpv = nodes[sorted_largest_dpv_feasible_nodes[0][0]]

        # index of best position for insert
        path_index = sorted_largest_dpv_feasible_nodes[0][1][0]
        node_index = sorted_largest_dpv_feasible_nodes[0][1][1]

        # inserted into the best position of the incumbent solution

        solution[path_index].insert(node_index, feasible_node_with_largest_dpv)

        # update list of unvisited nodes
        unvisited_nodes.remove(feasible_node_with_largest_dpv)
    return solution
