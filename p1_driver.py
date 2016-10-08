
import copy
import random
import problem
import search_agent
import search_algorithms


# ----------------- define goal, state transitions and heuristic --------------


goal_state = [1, 2, 3,
              8, 'B', 4,
              7, 6, 5]


def goal_test(node):
    return node.state == goal_state


def up(state):
    idx = state.index('B')
    new_state = []
    if idx > 2:
        new_state = copy.deepcopy(state)
        new_state[idx - 3], new_state[idx] = \
            new_state[idx], new_state[idx - 3]
    return new_state


def down(state):
    idx = state.index('B')
    new_state = []
    if idx < 6:
        new_state = copy.deepcopy(state)
        new_state[idx + 3], new_state[idx] = new_state[idx], new_state[idx + 3]
    return new_state


def left(state):
    idx = state.index('B')
    new_state = []
    if (idx % 3) != 0:
        new_state = copy.deepcopy(state)
        new_state[idx - 1], new_state[idx] = new_state[idx], new_state[idx - 1]
    return new_state


def right(state):
    idx = state.index('B')
    new_state = []
    if (idx % 3) != 2:
        new_state = copy.deepcopy(state)
        new_state[idx + 1], new_state[idx] = new_state[idx], new_state[idx + 1]
    return new_state


state_transitions = [up, right, left, down]


def h_out_of_place(state):
    h_s = 0
    for idx in range(len(state)):
        h_s += (1 if (state[idx] != goal_state[idx])
                and (state[idx] != 'B')  # we don't count the blank
                else 0)
    return h_s


def manhattan(state):
    h_s = 0
    for idx in range(len(state)):
        if (state[idx] != goal_state[idx]) \
          and (state[idx] != 'B'):  # we don't count the blank
            goal_idx = goal_state.index(state[idx])
            x = abs(idx % 3 - goal_idx % 3)
            y = abs(idx // 3 - goal_idx // 3)
            h_s += x + y
    return h_s


# possibly define more heuristics, but choose one in the end


# h = h_out_of_place
h = manhattan


def print_8puzzle_state(state):
    print('\n- - - - - - - - - -\n')
    for row in [state[0:3], state[3:6], state[6:9]]:
        print('{:>4} {:>4} {:>4}'.format(*row))

# ---------------- end definitions for the problem ----------------------------

the_problem = problem.Problem(goal_test, state_transitions, h)

start_state = copy.deepcopy(goal_state)
for i in range(1, 100):
    t_idx = random.randint(0, 3)
    new_state = state_transitions[t_idx](start_state)
    start_state = new_state if new_state else start_state

start = problem.Node(the_problem, start_state)

# print('\n', 'starting DFS')
# dfs_path = search_agent.find_goal(start, search_algorithms.dfs)
# while dfs_path:
#     n = dfs_path.pop(0)
#     print('This node\'s state is: ', n.state, ' and the parent\'s state is: ',
#           n.parent.state if n.parent else ' no parent...')

# print('\n', 'starting BFS')
# bfs_path = search_agent.find_goal(start, search_algorithms.bfs)
# while bfs_path:
#     n = bfs_path.pop(0)
#     print_8puzzle_state(n.state)

print('\n', 'starting Best First')
best_first_path = search_agent.find_goal(start, search_algorithms.best_first)
while best_first_path:
    n = best_first_path.pop(0)
    print_8puzzle_state(n.state)
    print('h = ', n.h)

print('\n', 'starting A*')
a_star_path = search_agent.find_goal(start, search_algorithms.a_star)
while a_star_path:
    n = a_star_path.pop(0)
    print_8puzzle_state(n.state)
    print('f(n) = ', n.h + n.cost,
          ', where h = ', n.h, ', and cost = ', n.cost)

