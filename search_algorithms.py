# Comp 6721 AI, Project 1, fall 2016
# Federico O'Reilly Regueiro 40012304


def expand_if(curr_node):
    # no children, generate 'em
    if not curr_node.children:
        curr_node.expand()


def dfs(curr_node, open_list, closed_list):
    expand_if(curr_node)

    # avoid including listed children redundantly in the open list (no infinite loops here)
    for child in reversed(curr_node.children):
        if not (any(node.state == child.state for node in open_list) or
                any(node.state == child.state for node in closed_list)):
            open_list.insert(0, child)
            child.parent = curr_node


def bfs(curr_node, open_list, closed_list):
    expand_if(curr_node)

    # avoid including listed children redundantly in the open list (no infinite loops here)
    for child in curr_node.children:
        if not (any(node.state == child.state for node in open_list) or
                any(node.state == child.state for node in closed_list)):
            open_list.append(child)
            child.parent = curr_node


def best_first(curr_node, open_list, closed_list):
    expand_if(curr_node)

# avoid including listed children redundantly in the open list (no infinite loops here)
    for child in sorted(curr_node.children, key=lambda node: node.h, reverse=True):
        if(not (any(node.state == child.state for node in open_list) or
                any(node.state == child.state for node in closed_list))):
            open_list.insert(0, child)
            child.parent = curr_node

# For A*, we could use this snippet but figure out backtracking
# not any((node.h + node.cost) <= (child.h + child.cost) for node in open_list):


def a_star(curr_node, open_list, closed_list):
    expand_if(curr_node)

# avoid including listed children redundantly in the open list (no infinite loops here)
    for child in curr_node.children:
        if (not (any(node.state == child.state for node in open_list) or
                     any(node.state == child.state for node in closed_list))):
            open_list.insert(0, child)
            child.parent = curr_node
    open_list.sort(key=lambda node: node.h + node.cost, reverse=True)





