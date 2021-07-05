import initialization.functions as functions
import random
from numpy.linalg import norm
import numpy as np

from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter


def initialization(nodes):  # initialization func, construct at most m(no_paths) paths
    # line 1 , Algorithm 2
    # set currentNode := 0
    current_node = nodes[0]

    unvisited_nodes = nodes[1:(no_nodes - 1)]  # all unvisited nodes except 0 and n+1

    paths = []

    # line 2 , Algorithm 2
    for i in range(no_paths):
        remaining_time = Tmax  # time limit of path
        # construct the ith path
        # line 4 , Algorithm 2
        path = []

        # line 5 , Algorithm 2
        while True:
            # line 6 , Algorithm 2
            flag = False

            # line 14 , Algorithm 2
            if not flag:
                # line 15 , Algorithm 2
                # number of unvisited feasible nodes (μ)
                if path.__len__() == 0:
                    # always for finding the number of unvisited feasible nodes, if
                    # the path was empty we assume the current node is 0
                    no_unvisited_feasible_nodes = functions.find_no_unvisited_feasible(unvisited_nodes, remaining_time, nodes[0])
                else:
                    no_unvisited_feasible_nodes = functions.find_no_unvisited_feasible(unvisited_nodes, remaining_time,
                                                                             current_node)

                # line 16 , Algorithm 2
                # minimum(l) is the min of μ and γ (Integer Parameter)
                minimum = min(no_unvisited_feasible_nodes, integer_parameter)
                # line 17 , Algorithm 2
                if minimum > 0:

                    # line 18 , Algorithm 2
                    # get favorite nodes of current node
                    if len(path)==0:
                        spvs = functions.static_preference_values(nodes, nodes[0][3])
                    else:
                        spvs = functions.static_preference_values(nodes, current_node[3])
                    sorted_spvs = sorted(
                        spvs.items(), key=lambda x: x[1], reverse=True)  # sort in descending order according to spvs
                    # find feasible favorite nodes of current node
                    if len(path)==0:
                        current_node_feasible_favorite_nodes=functions.find_feasibles(sorted_spvs, remaining_time, nodes[0],paths,path)
                    else:
                        current_node_feasible_favorite_nodes = functions.find_feasibles(sorted_spvs, remaining_time,
                                                                          current_node,paths,path)
                    # the next node is randomly chosen from the best l nodes in terms of their static preference values
                    best_l_nodes = current_node_feasible_favorite_nodes[0:minimum]
                    # randomly choose from best l (l=minimum of  μ and γ) nodes
                    index = int(random.random() * minimum)
                    node = best_l_nodes[index]

                    # line 19 , Algorithm 2
                    next_node = nodes[int(node[0])]
                    flag = True

                    # calculate the cost ( time ) of going from current node, to next node
                    if len(path)==0:
                        cost_i_to_j = norm(
                            np.array([nodes[0][0], nodes[0][1]]) - np.array([next_node[0], next_node[1]]))
                    else:

                        cost_i_to_j = norm(
                            np.array([current_node[0], current_node[1]]) - np.array([next_node[0], next_node[1]]))

                    remaining_time -= cost_i_to_j  # update remaining time

                    unvisited_nodes.remove(next_node)  # update unvisited nodes

            # line 22 , Algorithm 2
            if flag:
                # line 23 , Algorithm 2
                path.append(next_node)

                # line 24 , Algorithm 2
                current_node = next_node
            else:
                break
        if len(path)>0:
            paths.append(path)
    return paths
