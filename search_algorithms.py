# Comp 6721 AI, Project 1, fall 2016
# Federico O'Reilly Regueiro 40012304

# Suppose that a state generator (generate_children) function exists
# generating function needs to set the parent


def dfs(curr_node, open_list, closed_list):
    # no children, generate 'em
    if not curr_node.children:
        curr_node.expand()

    # avoid including listed children redundantly in the open list (no infinite loops here)
    for child in reversed(curr_node.children):
        if not (open_list.__contains__(child) or closed_list.__contains__(child)):
            open_list.insert(0, child)
            child.parent = curr_node


def bfs(curr_node, open_list, closed_list):
    # no children, generate 'em
    if not curr_node.children:
        curr_node.expand()

    # avoid including listed children redundantly in the open list (no infinite loops here)
    for child in curr_node.children:
        if not (open_list.__contains__(child) or closed_list.__contains__(child)):
            open_list.append(child)
            child.parent = curr_node


    


