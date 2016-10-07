

import search_agent
import search_algorithms

class Node:
    children = []
    parent = None
    value = None

root = Node()
root.value = 1

def generate_children(node):
    node1 = Node()
    node1.value = node.value+1
    node2 = Node()
    node2.value = node.value+2
    node.children = [node1, node2]

def goal_test(node):
    return node.value > 9

open_list = [root]
closed_list = []

dfs_path = search_agent.find_goal(open_list, closed_list,
                              search_algorithms.dfs,
                              goal_test, generate_children)
while dfs_path:
    n = dfs_path.pop(0)
    print('value of this node is: ')
    print(n.value)
    print(' and the parent\'s node is: ')
    if n.parent:
        print(n.parent.value)
    else:
        print(' no parent...')

open_list = [root]
closed_list = []

bfs_path = search_agent.find_goal(open_list, closed_list,
                              search_algorithms.bfs,
                              goal_test, generate_children)
while bfs_path:
    n = bfs_path.pop(0)
    print('value of this node is: ')
    print(n.value)
    print(' and the parent\'s node is: ')
    if n.parent:
        print(n.parent.value)
    else:
        print(' no parent...')
