from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio
import swallow.functions as functions
from swallow.repair_procedure import repair_procedure


def swallow_operator(solution,nodes):
    # find unvisited nodes
    unvisited_nodes = list(nodes[1:len(nodes) - 1])
    for path in solution:
        unvisited_nodes = [i for i in unvisited_nodes if i not in path]

    while True:
        travel_time_of_solution=functions.solution_travel_time(solution,nodes)
        tmp_solution=[]
        for i in range(len(solution)):
            tmp_solution.append(solution[i][:])

        if len(unvisited_nodes)==0:
            # there is no unvisited nodes to insert
            break

        # the swallow operator tries to insert an unvisited node with the largest dynamic preference value
        # suppose that node i is inserted into route Rl

        route_Rl=functions.insertion(nodes, tmp_solution, unvisited_nodes)

        # route_Rl is index of the route(path) which node i has been inserted in

        # todo repair procedure
        repair_procedure(tmp_solution,route_Rl,nodes)

        # If the final solution is better than the starting solution x,
        # then x is replaced and the swallow operator continues.
        travel_time_of_tmp_solution=functions.solution_travel_time(tmp_solution,nodes)
        if travel_time_of_tmp_solution < travel_time_of_solution:
            solution=list(tmp_solution)
        else:
            # Otherwise,the operator stops.
            break

