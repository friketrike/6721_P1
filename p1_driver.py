
import problem
import search_agent
import search_algorithms

the_problem = problem.Problem(lambda node: node.state > 9,
                              [lambda state: state+1, lambda state: state+2],
                              lambda self_state, state: state > self_state)

start = problem.Node(the_problem, 1)

dfs_path = search_agent.find_goal(start, search_algorithms.dfs)

while dfs_path:
    n = dfs_path.pop(0)
    print('value of this node is: ')
    print(n.state)
    print(' and the parent\'s node is: ')
    if n.parent:
        print(n.parent.state)
    else:
        print(' no parent...')

bfs_path = search_agent.find_goal(start, search_algorithms.bfs)

while bfs_path:
    n = bfs_path.pop(0)
    print('value of this node is: ')
    print(n.state)
    print(' and the parent\'s node is: ')
    if n.parent:
        print(n.parent.state)
    else:
        print(' no parent...')
