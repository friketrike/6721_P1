# Comp 6721 AI, Project 1, fall 2016
# Federico O'Reilly Regueiro 40012304


def expand_if(curr_node):
    # no children, generate 'em
    if not curr_node.children:
        curr_node.expand()


def dfs(curr_node, open_list, closed_list):
    expand_if(curr_node)
    dfs.counter += 1

    # avoid including listed children redundantly in the open list (no infinite loops here)
    # print('---', dfs.counter, ' ---\n', curr_node.state[0:3],
    #       '\n', curr_node.state[3:6],
    #       '\n', curr_node.state[6:9])
    for child in reversed(curr_node.children):
        if not (any(node.state == child.state for node in open_list) or
                any(node.state == child.state for node in closed_list)):
            open_list.insert(0, child)
            # print('\t', dfs.counter, child.state)
            child.parent = curr_node

dfs.counter = 0


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


def a_star(curr_node, open_list, closed_list):
    expand_if(curr_node)

    # avoid including listed children redundantly in the open list (no infinite loops here)
    for child in curr_node.children:
        if (not (any(node.state == child.state for node in open_list) or
                 any(node.state == child.state for node in closed_list))):
            open_list.insert(0, child)
            child.parent = curr_node
    open_list.sort(key=lambda node: node.h + node.cost)



