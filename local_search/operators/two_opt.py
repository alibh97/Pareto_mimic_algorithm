import local_search.functions as functions

# 2_opt operator in local search
def two_opt_operator(solution, nodes):
    for path in solution:

        smallest_travel_time = functions.calculate_total_travel_time(path, nodes)
        no_nodes_to_swap = len(path)
        current_path = path
        while True:
            flag = False
            c = 0
            for i in range(no_nodes_to_swap - 1):
                if flag:
                    break
                for k in range(i + 1, no_nodes_to_swap):
                    new_path = functions.two_opt_swap(path, i, k)
                    new_travel_time = functions.calculate_total_travel_time(new_path, nodes)
                    if new_travel_time < smallest_travel_time:
                        smallest_travel_time = new_travel_time
                        solution[solution.index(current_path)] = new_path
                        current_path = new_path

                        flag = True
                        break
                c = i
            if c == (no_nodes_to_swap - 2):
                break

    return solution
