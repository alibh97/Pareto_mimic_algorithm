from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio

import local_search.functions as functions


# relocate operator
def relocate_operator(solution, nodes):
    finding_better_solution = True
    while finding_better_solution:
        flag = False
        for path1 in solution:
            if flag:
                break
            travel_time_path1 = functions.calculate_total_travel_time(path1, nodes)
            for node1 in path1:
                if flag:
                    break
                relocate_node = node1
                current_path1 = list(path1)
                current_path1.remove(relocate_node)
                new_travel_time_path1 = functions.calculate_total_travel_time(current_path1, nodes)
                reduction_time_path1 = travel_time_path1 - new_travel_time_path1
                for path2 in solution:
                    if flag:
                        break
                    if path1 != path2:
                        travel_time_path2 = functions.calculate_total_travel_time(path2, nodes)
                        for i in range(len(path2) + 1):
                            current_path2 = list(path2)
                            current_path2.insert(i, relocate_node)
                            new_travel_time_path2 = functions.calculate_total_travel_time(current_path2, nodes)
                            increased_time_path2 = new_travel_time_path2 - travel_time_path2
                            if increased_time_path2 < reduction_time_path1 and \
                                    new_travel_time_path2 <= Tmax and \
                                    new_travel_time_path1 <= Tmax:
                                solution[solution.index(path1)] = current_path1
                                solution[solution.index(path2)] = current_path2
                                flag = True
                                break
                            else:
                                if i == len(path2) and \
                                        solution.index(path2) == (len(solution) - 2) and \
                                        path1.index(node1) == (len(path1) - 1) and \
                                        solution.index(path1) == (len(solution) - 1):
                                    finding_better_solution = False
    return solution
