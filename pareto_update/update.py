import pareto_update.functions as functions
from file_content import N


# Xb is the best so far solution
# from main import Xb


def update(solutions, Xb):
    # PMA assigns two indicators to each solution x: F(x) and N(x) + d(x, xb)
    solution_along_indicators = []
    for solution in solutions:
        # The first indicator(Fx) corresponds to the solution quality.
        first_indicator = functions.Fx(solution)

        # N(x) is the number of visited nodes
        N_x = functions.Nx(solution)

        # the solution x distance away from Xb
        d_x_Xb = functions.hamming_distance(solution, Xb)

        # The second indicator ( N(x) + d(x, xb) )
        # considers the influence of the number of visited nodes and the distance away from xb
        second_indicator = N_x + d_x_Xb

        solution_along_indicators.append([solution, [first_indicator, second_indicator]])

    # The update procedure (Update) chooses the new incumbent solutions from a set of candidate solutions consisting
    # of the old solutions in IS and new generated solutions (Q) as follows:
    # At first, those solutions which visit
    # less than N(xb) − N nodes are removed since their objective values are rather poorer than xb.
    threshold = functions.Nx(Xb) - N  # N is the maximum number of incumbent solutions=10

    tmp_solution_along_indicators = solution_along_indicators[:]
    for solution_along_indicator in tmp_solution_along_indicators:
        if functions.Nx(solution_along_indicator[0]) < threshold:
            solution_along_indicators.remove(solution_along_indicator)

    # Secondly, the nondominated solutions are chosen from the remaining solutions
    nondominated_solutions_along_indicators = []
    # A solution x is said to dominate another solution y,if the following conditions hold:
    # 1) x is not worse than y with respect to the two indicators.
    # 2) x is strictly better than y in terms of at least one indicator.
    # A solution is said to be nondominated if no other solution dominates it
    for solution_along_indicator1 in solution_along_indicators:
        nondominated = True
        for solution_along_indicator2 in solution_along_indicators:
            if solution_along_indicator1 != solution_along_indicator2:
                # condition 1
                if not (solution_along_indicator1[1][0] > solution_along_indicator2[1][0] or \
                        solution_along_indicator1[1][1] > solution_along_indicator2[1][1]):
                    # condition 2
                    if (solution_along_indicator2[1][0] > solution_along_indicator1[1][0] or
                            solution_along_indicator2[1][1] > solution_along_indicator1[1][1]):
                        nondominated = False

        # if no bode could dominate this solution,then this solution is nondominated
        if nondominated:
            nondominated_solutions_along_indicators.append(solution_along_indicator1)

    # If the number of the nondominated solutions
    # is larger than N, then N solutions are chosen according to crowding-distance
    if len(nondominated_solutions_along_indicators) > N:
        # it gives us an array of solutions along with indicators and crowding distances,sorted based on crowding
        # distances in descending order
        sorted_solution_indicator_distance = functions.calculate_crowding_distances(
            nondominated_solutions_along_indicators)
        final_solutions=[]
        for i in range(N):
            final_solutions.append(sorted_solution_indicator_distance[i][0])

        # return N best solutions based on crowding distance
        return final_solutions
    else:
        final_solutions = []
        for i in range(len(nondominated_solutions_along_indicators)):
            final_solutions.append(nondominated_solutions_along_indicators[i][0])
        return final_solutions