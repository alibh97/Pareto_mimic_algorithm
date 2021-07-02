import local_search.functions as functions


# exchange move operator
def exchange_operator(solution, nodes):
    flag2 = False
    while True:
        flag = False
        for path1 in solution:
            if flag:
                break
            smallest_travel_time_path1 = functions.calculate_total_travel_time(path1, nodes)
            current_path1 = list(path1)
            for node1 in path1:
                if flag:
                    break
                index_node_in_path1 = path1.index(node1)
                for path2 in solution:
                    if flag:
                        break
                    if path1 != path2:
                        current_path2 = list(path2)
                        smallest_travel_time_path2 = functions.calculate_total_travel_time(path2, nodes)
                        for node2 in path2:
                            index_node2_in_path2 = path2.index(node2)

                            current_path1[index_node_in_path1] = node2
                            current_path2[index_node2_in_path2] = node1
                            new_travel_time1 = functions.calculate_total_travel_time(current_path1, nodes)
                            new_travel_time2 = functions.calculate_total_travel_time(current_path2, nodes)
                            if new_travel_time1 < smallest_travel_time_path1 and \
                                    new_travel_time2 < smallest_travel_time_path2:
                                solution[solution.index(path1)] = current_path1
                                solution[solution.index(path2)] = current_path2
                                flag = True
                                break
                            else:
                                if path2.index(node2) == (len(path2) - 1) and \
                                        solution.index(path2) == (len(solution) - 2) and \
                                        path1.index(node1) == (len(path1) - 1) and \
                                        solution.index(path1) == (len(solution) - 1):
                                    flag2 = True

                                current_path1 = list(path1)
                                current_path2 = list(path2)
        if flag2:
            break
    return solution

