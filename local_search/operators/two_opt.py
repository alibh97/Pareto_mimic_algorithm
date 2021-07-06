import local_search.functions as functions
from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio


def two_opt_operator(solution, nodes):
    for path in solution:
        current_path = path

        while True:
            neighborhood = []
            no_nodes_to_swap = len(current_path)

            current_solution_travel_time = 0
            for p in solution:
                current_solution_travel_time += functions.calculate_total_travel_time(p, nodes)

            for i in range(no_nodes_to_swap - 1):

                for k in range(i + 1, no_nodes_to_swap):
                    neighboring_solution = list(solution)
                    new_path = functions.two_opt_swap(current_path, i, k)

                    new_travel_time = functions.calculate_total_travel_time(new_path, nodes)

                    # if new path is feasible , neighboring solution will be made
                    if new_travel_time <= Tmax:

                        neighboring_solution[solution.index(current_path)] = new_path
                        neighboring_solution_travel_time = 0
                        for p in neighboring_solution:
                            neighboring_solution_travel_time += functions.calculate_total_travel_time(p, nodes)
                        neighborhood.append([neighboring_solution, neighboring_solution_travel_time])
            if len(neighborhood)>0:

                # sort the neighboring solutions in ascending order based on their travel time
                neighborhood.sort(reverse=False, key=lambda n: n[1])
                # If the travel time of the best neighboring solution is smaller than the one of the current solution,
                # then the best neighboring solution will be accepted as the new current solution and the operator repeats.

                best_neighboring_solution_travel_time = neighborhood[0][1]
                if best_neighboring_solution_travel_time < current_solution_travel_time:

                    best_neighboring_solution = neighborhood[0][0]

                    current_path = [k for k in best_neighboring_solution if k not in solution]
                    current_path=current_path[0]
                    solution[:] = best_neighboring_solution
                else:
                    # Otherwise, the operator stops.
                    break
            else:
                break

