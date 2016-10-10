# Comp 6721 AI, Project 1, fall 2016
# Federico O'Reilly Regueiro 40012304


""""generic search algorithm taking nodes and an algorithm to traverse the
    problem space. The node itself should contain its own goal_test as per the
    Node class in the problem.m file"""

# Once we've found the goal, reconstruct a path leading to it from the start
def set_path_to_goal(node):
    path_to_goal = []
    while (node.parent):
        path_to_goal.insert(0, node)
        node = node.parent

    # don't forget to include the start state!    
    path_to_goal.insert(0, node)
    return path_to_goal


# generic search code, returns None if nothing was found, a path (linked-list)
# from the start to the goal otherwise
def find_goal(start_node, search_algorithm):

    open_list = [start_node]
    closed_list = []

    while open_list:
        curr_node = open_list.pop(0)
        # We found it, return a list with the path
        if curr_node.goal_test():
            return set_path_to_goal(curr_node)
        else:
            closed_list.append(curr_node)
            search_algorithm(curr_node, open_list, closed_list)

    return None

