# Comp 6721 AI, Project 1, fall 2016
# Federico O'Reilly Regueiro 40012304

# TODO problem_node should be a class containing children and a null parent
# upon return, the parents of the chosen goal can be set, allowing for backtracking
# the solution path; alternatively after the solution has been found, we can 
# backtrack and instantiate the forward link from the root node up to the goal. 

# import problem_node.py as pn
# impora serach_algorithms.py as sa

def find_goal(open_list, closed_list, search_algorithm, goal_test, generate_children):
    # TODO check that search_algorithm(), goal_test() and generate_children()
    # exist, otherwise give a usage warning
    path_to_goal = []
    while(open_list):
        curr_node = open_list.pop(0)
        # We found it, return a list with the path
        if goal_test(curr_node):
            while (curr_node.parent):
                path_to_goal.insert(0, curr_node)
                curr_node = curr_node.parent
                # TODO do we really want to delete the upstream reference?
                delete(path_to_goal[0].parent)
            return path_to_goal
        else:
            closed_list.append(curr_node)
            curr_node = search_algorithm(curr_node, open_list, closed_list, generate_children)

    return None

