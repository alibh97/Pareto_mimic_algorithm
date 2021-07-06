import local_search.functions as functions
from file_content import no_nodes, no_paths, Tmax, Points, integer_parameter, similarity_ratio


def exchange_operator(solution, index_of_route_Rl, nodes):
    while True:
        # a list of all neighboring solutions
        neighborhood = []
        for path1 in solution:
            route_Rl_travel_time = functions.calculate_total_travel_time(solution[index_of_route_Rl], nodes)

            index_of_path1 = solution.index(path1)
            current_path1 = list(path1)
            for node1 in path1:
                index_node1_in_path1 = path1.index(node1)
                for path2 in solution:

                    index_of_path2 = solution.index(path2)

                    if path2 != path1:
                        current_path2 = list(path2)
                        for node2 in path2:
                            # a neighboring solution is made of a change in solution
                            neighboring_solution = list(solution)

                            index_node2_in_path2 = path2.index(node2)
                            current_path1[index_node1_in_path1] = node2
                            current_path2[index_node2_in_path2] = node1

                            new_travel_time1 = functions.calculate_total_travel_time(current_path1, nodes)
                            new_travel_time2 = functions.calculate_total_travel_time(current_path2, nodes)

                            if index_of_path1 == index_of_route_Rl:
                                # shorten the travel time of route Rl
                                if new_travel_time1 < route_Rl_travel_time:
                                    # keep the feasibility of other routes
                                    if new_travel_time2 <= Tmax:
                                        # a neighboring solution will be made
                                        neighboring_solution[solution.index(path1)] = current_path1
                                        neighboring_solution[solution.index(path2)] = current_path2
                                        neighborhood.append(neighboring_solution)

                            if index_of_path2 == index_of_route_Rl:
                                # shorten the travel time of route Rl
                                if new_travel_time2 < route_Rl_travel_time:
                                    # keep the feasibility of other routes
                                    if new_travel_time1 <= Tmax:
                                        # a neighboring solution will be made
                                        neighboring_solution[solution.index(path1)] = current_path1
                                        neighboring_solution[solution.index(path2)] = current_path2
                                        neighborhood.append(neighboring_solution)

                            current_path1 = list(path1)
                            current_path2 = list(path2)
        # a neighboring solution is accepted if it is the first one that can shorten the travel time of route Rl
        # and keep the feasibility of other routes.
        if len(neighborhood) > 0:

            best_neighboring_solution = neighborhood[0]

            solution[:] = best_neighboring_solution

        else:
            # Otherwise, the operator stops.
            break
