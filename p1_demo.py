import defs_8puzzle as defs

import problem as p
import search_agent as agent
import search_algorithms as algos

the_problem = p.Problem(defs.goal_test, defs.state_transitions)

def left_uninformed_demo():
    left_branch_start_state = [2, 3, 4,
                               1, 8, 5,
                               7, 6, 'B']
    start_node = p.Node(the_problem, left_branch_start_state, 0, None, [])
    print('Starting BFS:')
    bfs_path = agent.find_goal(start_node, algos.bfs)
    print('BFS results:')
    while bfs_path:
        n = bfs_path.pop(0)
        defs.print_8puzzle_state(n.state)
        print('Path depth:', n.cost)

    start_node = p.Node(the_problem, left_branch_start_state, 0, None, [])
    print('Starting DFS:')
    dfs_path = agent.find_goal(start_node, algos.dfs)
    print('DFS results:')
    while dfs_path:
        n = dfs_path.pop(0)
        defs.print_8puzzle_state(n.state)
        print('Path depth:', n.cost)

def random_uninformed_demo():
    random_start_state = defs.rand_perm(defs.goal_state, 10)
    start_node = p.Node(the_problem, random_start_state, 0, None, [])
    print('Starting BFS:')
    bfs_path = agent.find_goal(start_node, algos.bfs)
    print('DFS results:')
    while bfs_path:
        n = bfs_path.pop(0)
        defs.print_8puzzle_state(n.state)
        print('Path depth:', n.cost)

    start_node = p.Node(the_problem, random_start_state, 0, None, [])
    print('Starting DFS:')
    dfs_path = agent.find_goal(start_node, algos.dfs)
    print('DFS results:')
    while dfs_path:
        n = dfs_path.pop(0)
        defs.print_8puzzle_state(n.state)
        print('Path depth:', n.cost)


def help():
    print('--Call left_uninformed_demo() for a short demo of forcing a state that can be found by going down', \
            'the left sub-tree, good for a quick run of DFS.\n')
    print('--Call random_uninformed_demo() to call uninformed strategies on a random initial state. You might ' ,\
            'want to press Ctrl-c with this one as DFS might take a very long time.\n')
    print('--Call informed_demo(algorithm, h, start_state ) for a demo of informed algorithms. Arguments are ', \
            'as follows:\n\talgorithm can be algos.best_first or algos.a_star. If no argument is given A* ',\
            'is chosen by default.\n')
    print('\th can be any of:\n\t\tdefs.out_of_place, \n\t\tdefs.manhattan, \n\t\tdefs.min_manhattan_out_of_place ',\
            '\n\t\tdefs.push_tiles, \n\t\tdefs.better_heuristic or \n\t\tdefs.indamissible.\n\tIf no argument is '\
            'given better_heuristic will be chosen by default.\n')
    print('\tstart_state should be a valid start state in python list form. Eg. [1,2,3,8,\'B\',4,5,6,7].\n', \
            '\tIf no state is given, a random start_state will be generated.'
            '\n\tNOTE, there is no error checking for the time being and an invalid initial state\n\t',\
            'will cause the program to hang.')

def informed_demo(algorithm, h, start_state):
    if algorithm == None:
        algorithm = algos.a_star
    if h == None:
        h = defs.better_heuristic
    if start_state == None:
        start_state = defs.rand_perm(defs.goal_state, 50)
    start_node = p.Node(the_problem, start_state, 0, None, [])
    print('Starting ', algorithm.__name__, ' with ', h.__name__, ' as a heuristic for:')
    defs.print_8puzzle_state(start_state)
    path = agent.find_goal(start_node, algorithm)
    print('Results:')
    while path:
        n = path.pop(0)
        defs.print_8puzzle_state(n.state)
        print(h.__name__, ' f(n) = ', n.h + n.cost,
              ', where h = ', n.h, ', and cost = ', n.cost)
