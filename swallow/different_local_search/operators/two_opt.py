import local_search.functions as functions
from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio


def two_opt_operator(solution,route_Rl, nodes):
    index_of_route_Rl=solution.index(route_Rl)
    route_Rl_travel_time=functions.calculate_total_travel_time(route_Rl,nodes)
    for path in solution:
        current_path = path

        while True:
            neighborhood = []
            no_nodes_to_swap = len(current_path)

            for i in range(no_nodes_to_swap - 1):

                for k in range(i + 1, no_nodes_to_swap):
                    neighboring_solution = list(solution)
                    new_path = functions.two_opt_swap(current_path, i, k)

                    new_travel_time = functions.calculate_total_travel_time(new_path, nodes)

                    # if current path is route Rl,new path will be accepted if it's travel time is less than route Rl
                    if solution.index(current_path)==index_of_route_Rl:
                        neighboring_solution[solution.index(current_path)] = new_path

                        neighborhood.append(neighboring_solution)

                    # if new path is feasible , neighboring solution will be made , in this way we can keep the
                    # feasibility of other routes than route Rl
                    if new_travel_time <= Tmax:

                        neighboring_solution[solution.index(current_path)] = new_path

                        neighborhood.append(neighboring_solution)
            # a neighboring solution is accepted if it is the first one that can shorten the travel time of route Rl
            # and keep the feasibility of other routes.


                best_neighboring_solution = neighborhood[0][0]

                current_path = [k for k in best_neighboring_solution if k not in solution]
                current_path=current_path[0]
                solution[:] = best_neighboring_solution
            else:
                # Otherwise, the operator stops.
                break




