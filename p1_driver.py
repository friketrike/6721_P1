
import problem
import search_agent
import search_algorithms

the_problem = problem.Problem(lambda node: node.state > 53,
                              [lambda state: state*2, lambda state: state*3],
                              lambda state: 2 if state % 2 == 0 else 1)

start = problem.Node(the_problem, 1)

dfs_path = search_agent.find_goal(start, search_algorithms.dfs)

while dfs_path:
    n = dfs_path.pop(0)
    print('This node\'s state is: ', n.state, ' and the parent\'s state is: ',
          n.parent.state if n.parent else ' no parent...')

bfs_path = search_agent.find_goal(start, search_algorithms.bfs)

while bfs_path:
    n = bfs_path.pop(0)
    print('This node\'s state is: ', n.state, ' and the parent\'s state is: ',
          n.parent.state if n.parent else ' no parent...')

best_first_path = search_agent.find_goal(start, search_algorithms.best_first)

while best_first_path:
    n = best_first_path.pop(0)
    print('This node\'s state is: ', n.state, ' and the parent\'s state is: ',
          n.parent.state if n.parent else ' no parent...')
    print('And h is', n.h)

print('starting A*')
a_star_path = search_agent.find_goal(start, search_algorithms.a_star)

while a_star_path:
    n = a_star_path.pop(0)
    print('This node\'s state is: ', n.state, ' and the parent\'s state is: ',
          n.parent.state if n.parent else ' no parent...')
    print('And h is', n.h)

