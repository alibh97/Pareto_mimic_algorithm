from numpy.linalg import norm
import numpy as np

from file_content import no_nodes, no_paths, Tmax, Points,integer_parameter,similarity_ratio

# for any node i (1<= i <=n ) ,the nodes except 0, i,and n + 1 ,
# are sorted in descending order according to their static preference values,
# and then the first L nodes are stored into a list of node i,
# where L a sufficient large integer (in our experiment, L is chosen as 50).
def favorite_nodes(nodes):
    result = []  # the result is a list of 'First L Nodes' for each node i ( 1 <= i <= n)

    for i in range(len(nodes) - 1):
        spvs = static_preference_values(nodes, i)  # static preference values of other nodes for node i
        sorted_spvs = sorted(
            spvs.items(), key=lambda x: x[1], reverse=True)  # sort in descending order according to spvs
        L = 50
        first_L_nodes = sorted_spvs[0:L]
        result.append(first_L_nodes)
    return result


# suppose current node is i ,static preference value of node j , is r_j / c_ij ,
# r_j is the reward of node j , and c_ij is the travel time of edge(i,j)
def static_preference_values(nodes, index):
    spvs = {}  # static preference values of nodes based on current node
    for j in range(1, len(nodes) - 1):
        if j != index:
            a = np.array([nodes[index][0], nodes[index][1]])  # coordinate of current node
            b = np.array(
                [nodes[j][0], nodes[j][1]])  # coordinate of point we want calculate it's static preference value
            c_ij = norm(a - b)  # distance between two nodes , as the travel time of the edge

            r_j = nodes[j][2]  # reward of node j

            spv = r_j / c_ij  # static preference value of node j

            spvs[j] = spv
    return spvs


# this function finds number of unvisited feasible nodes out of unvisited nodes so far and return it
def find_no_unvisited_feasible(unvisited_so_far, remaining_time, current_node):
    no_unvisited_feasible_nodes = 0  # this will be returned as result

    for unvisited in unvisited_so_far:
        # calculate cost of going from current node i to next node j (1 <= j <= n)
        cost_i_to_j = norm(
            np.array([current_node[0], current_node[1]]) - np.array([unvisited[0], unvisited[1]]))

        # calculate cost of going from next node j to ending node n+1 (1 <= j <= n)
        cost_j_to_end = norm(
            np.array([unvisited[0], unvisited[1]]) - np.array([Points[no_nodes - 1][0], Points[no_nodes - 1][1]]))

        # if cost of going from current node(i) to next node j (1 <= j <= n) plus
        # cost of going from next node j to ending node n+1, be less than remaining time,
        # then node j is a feasible node
        if (cost_i_to_j + cost_j_to_end) <= remaining_time:
            no_unvisited_feasible_nodes += 1

    return no_unvisited_feasible_nodes


# this func find feasible nodes out of favorite nodes of current node
def find_feasibles(current_node_favorite_nodes, remaining_time, current_node):
    current_node_feasible_favorite_nodes = []
    for favorite_node in current_node_favorite_nodes:
        cost_i_to_j = norm(
            np.array([current_node[0], current_node[1]])
            - np.array([Points[favorite_node[0]][0], Points[favorite_node[0]][1]]))

        cost_j_to_end = norm(
            np.array([Points[favorite_node[0]][0], Points[favorite_node[0]][1]]) - np.array(
                [Points[no_nodes - 1][0], Points[no_nodes - 1][1]]))

        # if condition be TRUE, so this favorite node is feasible
        if (cost_i_to_j + cost_j_to_end) <= remaining_time:
            current_node_feasible_favorite_nodes.append(favorite_node)

    return current_node_feasible_favorite_nodes

# this func deletes the chosen next node from all node's favorite nodes, and update fav_nodes list
def delete_from_favorite(favorite__nodes, next_node):
    for nodes in favorite__nodes:
        for node in nodes:
            if node[0] == next_node[3]:
                nodes.remove(node)

