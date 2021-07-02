import local_search.functions as functions


# cross move operator
def cross_operator(solution, nodes):
    finding_better_solution = True
    while finding_better_solution:
        flag = False
        for path1 in solution:
            if flag:
                break
            smallest_travel_time_path1 = functions.calculate_total_travel_time(path1, nodes)
            for i in range(len(path1) + 1):
                if flag:
                    break
                path1_slice1 = path1[0:i]
                path1_slice2 = path1[i:]

                for path2 in solution:
                    if flag:
                        break
                    if path1 != path2:
                        smallest_travel_time_path2 = functions.calculate_total_travel_time(path2, nodes)

                        for k in range(len(path2) + 1):
                            path2_slice1 = path2[0:k]
                            path2_slice2 = path2[k:]

                            tmp_path1 = path1_slice1 + path2_slice2
                            tmp_path2 = path2_slice1 + path1_slice2

                            new_travel_time1 = functions.calculate_total_travel_time(tmp_path1, nodes)
                            new_travel_time2 = functions.calculate_total_travel_time(tmp_path2, nodes)
                            if ((new_travel_time1 < smallest_travel_time_path1 and
                                 new_travel_time2 < smallest_travel_time_path2) or
                                    (new_travel_time1 < smallest_travel_time_path2 and
                                     new_travel_time2 < smallest_travel_time_path1)):
                                solution[solution.index(path1)] = tmp_path1
                                solution[solution.index(path2)] = tmp_path2
                                flag = True
                                break
                            else:
                                if k == len(path2) and \
                                        solution.index(path2) == (len(solution) - 2) and \
                                        i == len(path1) and \
                                        solution.index(path1) == (len(solution) - 1):
                                    finding_better_solution = False
    return solution
