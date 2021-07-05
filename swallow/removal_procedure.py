from swallow.functions import is_solution_feasible
from swallow.functions import calculate_total_travel_time


def removal_procedure(solution,index_of_route_Rl,nodes):
    # The removal procedure
    # removes the node with the largest removal reward step by step until the final solution is feasible.
    while True:
        sorted_removal_reward_of_nodes_of_route_Rl=calculate_removal_reward(solution[index_of_route_Rl],nodes)
        node_with_largest_removal_reward=sorted_removal_reward_of_nodes_of_route_Rl[0][0]
        # remove the node with the largest removal reward
        solution[index_of_route_Rl].remove(node_with_largest_removal_reward)

        if is_solution_feasible(solution,nodes):
            break


def calculate_removal_reward(path, nodes):
    sorted_removal_reward_of_nodes = []

    travel_time_of_path = calculate_total_travel_time(path, nodes)
    for node in path:
        tmp_path = list(path)

        # reward of node i
        r_i = node[2]

        tmp_path.remove(node)
        tmp_path_travel_time = calculate_total_travel_time(tmp_path, nodes)

        # Ti is the decrement of travel time obtained by removing node i.
        T_i = travel_time_of_path - tmp_path_travel_time

        # the removal reward of node i (i belongs to s) is defined as Ti/ri where
        removal_reward = T_i / r_i

        sorted_removal_reward_of_nodes.append([node, removal_reward])

    # sort nodes in descending order based on their removal reward
    sorted_removal_reward_of_nodes.sort(reverse=True, key=lambda n: n[1])
    return sorted_removal_reward_of_nodes