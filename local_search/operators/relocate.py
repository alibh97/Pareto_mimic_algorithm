from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio

import local_search.functions as functions


def relocate_operator(solution,nodes):
    while True:
        current_solution_travel_time = 0
        for p in solution:
            current_solution_travel_time += functions.calculate_total_travel_time(p, nodes)

        # a list of all neighboring solutions
        neighborhood=[]
        for path1 in solution:
            for node1 in path1:
                relocate_node=node1
                current_path1 = list(path1)
                current_path1.remove(relocate_node)
                for path2 in solution:
                    if path1!=path2:
                        for i in range(len(path2)+1):
                            # a neighboring solution is made of a change in solution
                            neighboring_solution=list(solution)

                            current_path2 = list(path2)
                            current_path2.insert(i, relocate_node)

                            travel_time_new_path1 = functions.calculate_total_travel_time(current_path1, nodes)

                            travel_time_new_path2 = functions.calculate_total_travel_time(current_path2, nodes)

                            # if paths are feasible , neighboring solution will be made
                            if travel_time_new_path1<=Tmax and travel_time_new_path2<=Tmax:
                                neighboring_solution[solution.index(path1)] = current_path1
                                neighboring_solution[solution.index(path2)] = current_path2

                                neighboring_solution_travel_time = 0
                                for p in neighboring_solution:
                                    neighboring_solution_travel_time += functions.calculate_total_travel_time(p, nodes)

                                neighborhood.append([neighboring_solution, neighboring_solution_travel_time])

        # todo if len >0
        if len(neighborhood)>0:

            # sort the neighboring solutions in ascending order based on their travel time
            neighborhood.sort(reverse=False, key=lambda n: n[1])

            # If the travel time of the best neighboring solution is smaller than the one of the current solution,
            # then the best neighboring solution will be accepted as the new current solution and the operator repeats.
            best_neighboring_solution_travel_time = neighborhood[0][1]
            if best_neighboring_solution_travel_time < current_solution_travel_time:
                best_neighboring_solution = neighborhood[0][0]

                solution[:] = best_neighboring_solution
            else:
                # Otherwise, the operator stops.
                break
        else:
            break

