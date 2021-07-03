import local_search.functions as functions




def exchange_operator(solution, nodes):
    while True:
        current_solution_travel_time = 0
        for p in solution:
            current_solution_travel_time += functions.calculate_total_travel_time(p, nodes)

        # a list of all neighboring solutions
        neighborhood = []
        for path1 in solution:
            current_path1 = list(path1)
            for node1 in path1:
                index_node1_in_path1 = path1.index(node1)
                for path2 in solution:
                    if path2 != path1:
                        current_path2 = list(path2)
                        for node2 in path2:
                            # a neighboring solution is made of a change in solution
                            neighboring_solution = list(solution)
                            index_node2_in_path2 = path2.index(node2)
                            current_path1[index_node1_in_path1] = node2
                            current_path2[index_node2_in_path2] = node1

                            neighboring_solution[solution.index(path1)] = current_path1
                            neighboring_solution[solution.index(path2)] = current_path2

                            neighboring_solution_travel_time = 0
                            for p in neighboring_solution:
                                neighboring_solution_travel_time += functions.calculate_total_travel_time(p, nodes)

                            neighborhood.append([neighboring_solution, neighboring_solution_travel_time])
                            current_path1 = list(path1)
                            current_path2 = list(path2)
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
