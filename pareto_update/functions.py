from file_content import no_nodes, no_paths, Tmax, Points, integer_parameter, similarity_ratio
from scipy.spatial.distance import hamming
import numpy as np


# Fx is objective value of solution x, is the total received reward of these paths of x.
def Fx(solution):
    total_received_reward = 0
    for path in solution:
        for node in path:
            total_received_reward += node[2]
    return total_received_reward


# this function give us the number of visited nodes of solution x
def Nx(solution):
    no_visited_nodes = 0
    for path in solution:
        no_visited_nodes += len(path)
    return no_visited_nodes


# Given two solutions x and y, their distance, denoted by
# d(x, y), is defined as the Hamming distance between their corresponding n-dimensional vectors W and V :
def hamming_distance(s1, s2):
    # For any solution x, it is associated with an n-dimensional vector W, if node
    # # i(1 ≤ i ≤ n) is visited, then Wi = 1, otherwise, Wi = 0
    w = []  # n-dimensional vector associated with solution s1
    v = []  # n-dimensional vector associated with solution s2

    # all nodes except node 0 and node n+1 ( 1 < i < n ), obtained from reading file
    all_nodes = Points[1:len(Points) - 1]

    # filling w and v vectors
    for node in all_nodes:
        is_node_in_solution = 0
        for path in s1:
            if path.__contains__(node):
                is_node_in_solution = 1
        w.append(is_node_in_solution)

        is_node_in_solution = 0
        for path in s2:
            if path.__contains__(node):
                is_node_in_solution = 1
        v.append(is_node_in_solution)

    # Given two solutions x and y, their distance, denoted by
    # d(x, y), is defined as the Hamming distance between their corresponding n-dimensional vectors W and V :
    # d(x, y) = HammingDistance(W, V)

    d_s1_s2 = hamming(w, v) * len(w)
    return d_s1_s2

def calculate_crowding(scores):
    # Crowding is based on a vector for each individual
    # All dimension is normalised between low and high. For any one dimension, all
    # solutions are sorted in order low to high. Crowding for chromsome x
    # for that score is the difference between the next highest and next
    # lowest score. Total crowding value sums all crowding for all scores

    population_size = len(scores[:, 0])
    number_of_scores = len(scores[0, :])

    # create crowding matrix of population (row) and score (column)
    crowding_matrix = np.zeros((population_size, number_of_scores))

    # normalise scores (ptp is max-min)
    normed_scores = scores

    # calculate crowding distance for each score in turn
    for col in range(number_of_scores):
        crowding = np.zeros(population_size)

        # end points have maximum crowding
        crowding[0] = float('inf')
        crowding[population_size - 1] = float('inf')

        # Sort each score (to calculate crowding between adjacent scores)
        sorted_scores = np.sort(normed_scores[:, col])

        sorted_scores_index = np.argsort(
            normed_scores[:, col])

        # Calculate crowding distance for each individual
        crowding[1:population_size - 1] = \
            (sorted_scores[2:population_size] -
             sorted_scores[0:population_size - 2])

        # resort to orginal order (two steps)
        re_sort_order = np.argsort(sorted_scores_index)
        sorted_crowding = crowding[re_sort_order]

        # Record crowding distances
        crowding_matrix[:, col] = sorted_crowding

    # Sum crowding distances of each score
    crowding_distances = np.sum(crowding_matrix, axis=1)

    return crowding_distances

def calculate_crowding_distances(solutions_along_indicator):
    indicators=[]
    for s in solutions_along_indicator:
        indicators.append(s[1])
    tmp_crowding_distances=calculate_crowding(np.array(indicators))
    crowding_distances=[]
    for c in tmp_crowding_distances:
        crowding_distances.append(c/2)
    solution_indicators_distance=[]
    print('crowding distances:',crowding_distances)
    for i in range(len(indicators)):
        solution_indicators_distance.append([solutions_along_indicator[i][0],indicators[i],crowding_distances[i]])

    # sort based on crowding distance in descending order
    solution_indicators_distance.sort(reverse=True,key=lambda s:s[2])

    return solution_indicators_distance
