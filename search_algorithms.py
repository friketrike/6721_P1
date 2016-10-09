# Comp 6721 AI, Project 1, fall 2016
# Federico O'Reilly Regueiro 40012304


""""Different search algorithms for a given problem, they expand nodes and order
    them appropriately in the open list"""


# helper to avoid repeating code in each algorithm
def expand_if(curr_node):
    # no children, generate 'em
    if not curr_node.children:
        curr_node.expand()


# Depth-first search
def dfs(curr_node, open_list, closed_list):
    expand_if(curr_node)

    # avoid including listed children redundantly in the open list (no infinite loops here)
    for child in reversed(curr_node.children):
        if not (any(node.state == child.state for node in closed_list)):
            # DFS open list is a LIFO / stack
            open_list.insert(0, child)
            child.parent = curr_node


# Breadth-first search
def bfs(curr_node, open_list, closed_list):
    expand_if(curr_node)

    # avoid including listed children redundantly in the open list (no infinite loops here)
    for child in curr_node.children:
        if not (any(node.state == child.state for node in closed_list)):
            # BFS open list is a FIFO / queue
            open_list.append(child)
            child.parent = curr_node


# Good ol' greedy bfs
def best_first(curr_node, open_list, closed_list):
    expand_if(curr_node)

    # avoid including listed children redundantly in the open list (no infinite loops here)
    # prioritize children with lowest value
    for child in sorted(curr_node.children, key=lambda node: node.h, reverse=True):
        if not (any(node.state == child.state for node in closed_list)):
            open_list.insert(0, child)
            child.parent = curr_node


# A* search
def a_star(curr_node, open_list, closed_list):
    expand_if(curr_node)

    # avoid including listed children redundantly in the open list (no infinite loops here)
    for child in curr_node.children:
        if not (any(node.state == child.state for node in closed_list)):
            open_list.insert(0, child)
            child.parent = curr_node
    # priority queue on f(n)
    open_list.sort(key=lambda node: node.h + node.cost)



