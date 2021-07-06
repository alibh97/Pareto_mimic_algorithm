import mimic.functions as functions
import random
from numpy.linalg import norm
import numpy as np

from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter ,similarity_ratio


def mimic_operator(nodes, solution):
    current_node = nodes[0]     # line 1 , Algorithm 2 , set currentNode := 0
    unvisited_nodes = nodes[1:(no_nodes - 1)]  # all unvisited nodes except 0 and n+1
    paths = []  # it is the new solution that will be made
    for i in range(no_paths): # line 2 , Algorithm 2
        remaining_time = Tmax  # time limit of path
        path = []  # construct the ith path, line 4 , Algorithm 2
        while True:  # line 5 , Algorithm 2
            flag = False  # line 6 , Algorithm 2
            r = random.uniform(0, 1)  # a uniformly distributed random number r ∈ [0, 1], line 7 , Algorithm 2
            if r < similarity_ratio:  # similarity ratio ( α ), line 8 , Algorithm 2
                # set node := the next node of currentNode in xI(xI=solution passed to this function)
                node = functions.find_next(solution, current_node)  # line 9 , Algorithm 2
                if functions.is_feasible(current_node, node, remaining_time, paths, path):  # line 10 , Algorithm 2
                    # calculate the cost ( time ) of going from current node, to next node
                    if path.__len__() == 0:
                        # if the node be the first node of path , the current node is node 0
                        cost_i_to_j = norm(
                            np.array([nodes[0][0], nodes[0][1]]) - np.array([node[0], node[1]]))
                    else:
                        cost_i_to_j = norm(
                            np.array([current_node[0], current_node[1]]) - np.array([node[0], node[1]]))
                    remaining_time -= cost_i_to_j  # update remaining time
                    unvisited_nodes.remove(node)  # update unvisited nodes
                    next_node = node # line 11 , Algorithm 2
                    flag = True
            if not flag:  # line 14 , Algorithm 2
                # number of unvisited feasible nodes (μ)
                if path.__len__() == 0: # line 15 , Algorithm 2
                    # always for finding the number of unvisited feasible nodes, if
                    # the path was empty we assume the current node is 0
                    no_unvisited_feasible_nodes = functions.find_no_unvisited_feasible(unvisited_nodes, remaining_time, nodes[0])
                else:
                    no_unvisited_feasible_nodes = functions.find_no_unvisited_feasible(unvisited_nodes, remaining_time,
                                                                             current_node)
                # minimum(l) is the min of μ and γ (Integer Parameter)
                minimum = min(no_unvisited_feasible_nodes, integer_parameter)  # line 16 , Algorithm 2
                if minimum > 0:  # line 17 , Algorithm 2
                    # find static preferences values of other nodes for current node
                    if len(path)==0:  # line 18 , Algorithm 2
                        spvs = functions.static_preference_values(nodes, nodes[0][3]) # spv is static preference value
                    else:
                        spvs = functions.static_preference_values(nodes, current_node[3])
                    sorted_spvs = sorted(
                        spvs.items(), key=lambda x: x[1], reverse=True)  # sort in descending order according to spvs
                    # find feasible nodes in sorted_spvs
                    if len(path) == 0:
                        current_node_feasible_favorite_nodes=functions.find_feasibles(sorted_spvs, remaining_time, nodes[0],paths,path)
                    else:
                        current_node_feasible_favorite_nodes = functions.find_feasibles(sorted_spvs, remaining_time,current_node,paths,path)
                    # the next node is randomly chosen from the best l nodes in terms of their static preference values
                    best_l_nodes = current_node_feasible_favorite_nodes[0:minimum]
                    # randomly choose from best l (l=minimum of  μ and γ) nodes
                    index = int(random.random() * minimum)
                    node = best_l_nodes[index]
                    next_node = nodes[node[0]]   # line 19 , Algorithm 2
                    flag = True
                    if len(path) == 0:  # calculate the cost ( time ) of going from current node, to next node
                        cost_i_to_j = norm(
                            np.array([nodes[0][0], nodes[0][1]]) - np.array([next_node[0], next_node[1]]))
                    else:
                        cost_i_to_j = norm(
                            np.array([current_node[0], current_node[1]]) - np.array([next_node[0], next_node[1]]))
                    remaining_time -= cost_i_to_j  # update remaining time
                    unvisited_nodes.remove(next_node)  # update unvisited nodes
            if flag: # line 22 , Algorithm 2
                path.append(next_node)  # line 23 , Algorithm 2
                current_node = next_node  # line 24 , Algorithm 2
            else:
                break
        paths.append(path)
    # paths variable is the new solution
    return paths
