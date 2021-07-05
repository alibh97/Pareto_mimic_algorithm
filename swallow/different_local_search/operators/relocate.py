from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio

import local_search.functions as functions


def relocate_operator(solution,index_of_route_Rl,nodes):
    while True:
        # a list of all neighboring solutions
        neighborhood=[]
        for path1 in solution:
            route_Rl_travel_time = functions.calculate_total_travel_time(solution[index_of_route_Rl], nodes)
            index_of_path1 = solution.index(path1)
            for node1 in path1:
                relocate_node=node1
                current_path1 = list(path1)
                current_path1.remove(relocate_node)
                for path2 in solution:
                    index_of_path2 = solution.index(path2)

                    if path1!=path2:
                        for i in range(len(path2)+1):
                            # a neighboring solution is made of a change in solution
                            neighboring_solution=list(solution)

                            current_path2 = list(path2)
                            current_path2.insert(i, relocate_node)

                            travel_time_new_path1 = functions.calculate_total_travel_time(current_path1, nodes)

                            travel_time_new_path2 = functions.calculate_total_travel_time(current_path2, nodes)

                            if index_of_path1 == index_of_route_Rl:
                                # shorten the travel time of route Rl
                                if travel_time_new_path1 < route_Rl_travel_time:
                                    # keep the feasibility of other routes
                                    if travel_time_new_path2 <= Tmax:
                                        # a neighboring solution will be made
                                        neighboring_solution[solution.index(path1)] = current_path1
                                        neighboring_solution[solution.index(path2)] = current_path2
                                        neighborhood.append(neighboring_solution)

                            if index_of_path2 == index_of_route_Rl:
                                # shorten the travel time of route Rl
                                if travel_time_new_path2 < route_Rl_travel_time:
                                    print('yessssssssssss')
                                    # keep the feasibility of other routes
                                    if travel_time_new_path1 <= Tmax:
                                        # a neighboring solution will be made
                                        neighboring_solution[solution.index(path1)] = current_path1
                                        neighboring_solution[solution.index(path2)] = current_path2
                                        neighborhood.append(neighboring_solution)

                            # if paths are feasible , neighboring solution will be made
                            if travel_time_new_path1<=Tmax and travel_time_new_path2<=Tmax:
                                neighboring_solution[solution.index(path1)] = current_path1
                                neighboring_solution[solution.index(path2)] = current_path2


        # todo if len >0

        # a neighboring solution is accepted if it is the first one that can shorten the travel time of route Rl
        # and keep the feasibility of other routes.
        if len(neighborhood) > 0:

            best_neighboring_solution = neighborhood[0]

            solution[:] = best_neighboring_solution


        else:
            # Otherwise, the operator stops.
            break

