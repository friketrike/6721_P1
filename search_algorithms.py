# Comp 6721 AI, Project 1, fall 2016
# Federico O'Reilly Regueiro 40012304

# Suppose that a state generator (generate_children) function exists
# generating function needs to set the parent

def dfs(curr_node, open_list, closed_list, generate_children):
    # no children, generate 'em
    if not hasattr(curr_node, 'children'):
        generate_children(curr_node)
        # delete redundant children and put them into lists, keep the deletion
        # of redundancies at the algorithm level since some algorithms will
        # seek to replace parenthood for existing children
        try: # TODO fix this non iterable rubish...
            for child in curr_node.children.reverse():
                if open_list.__contains(child) or closed_list.__contains__(child):
                    curr_node.children.remove(child)
                else:
                    open_list.insert(0, child)
                    child.parent = current_node

            curr_node.children.reverse()
        except AttributeError:
            x = 2 # was the lack of a statement causing the indentation error?

    if open_list:
        return open_list.pop(0)
    else:
        return None

def bfs(curr_node, open_list, closed_list):   
    return new_node
    

    


