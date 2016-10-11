import copy
import random



# ----------------- define goal, state transitions and heuristics --------------


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


# out-of-place number of tiles heuristic
def out_of_place(state):
    h_s = 0
    for idx in range(len(state)):
        h_s += (1 if (state[idx] != goal_state[idx])
                and (state[idx] != 'B')  # we don't count the blank
                else 0)
    return h_s


# Helper for manhattan distance and push_tiles heuristics, given two indices from
# a 3x3 grid, returns a list with the 2d vector we need to ad to the source to get
# to the destination
def manhattan_helper(idx_src, idx_dest):
    return [((idx_dest % 3) - (idx_src % 3)), ((idx_dest // 3) - (idx_dest // 3))]


# helper for manhattan and push_tiles heuristics, the l1 norm of the vector
def l1_dist(x_y):
    return abs(x_y[0]) + abs(x_y[1])


# cost is how many movements would take place if each out-of-place tile was moved to
# the goal unconstrained (no other tiles blocking it
def manhattan(state):
    h_s = 0
    for idx in range(len(state)):
        if (state[idx] != goal_state[idx]) \
          and (state[idx] != 'B'):  # we don't count the blank
            goal_idx = goal_state.index(state[idx])
            x_y = manhattan_helper(idx, goal_idx)
            h_s += l1_dist(x_y)
    return h_s


def min_manhattan_out_of_place(state):
    return min(manhattan(state), out_of_place(state))


# this admissible heuristic is based on the fact that tiles between an out-of-place
# tile and its goal position will also need to be moved towards the blank. In the end
# only the largest number of movements caused by a single tile going towards its
# goal state is considered and all other out-of-place tiles add 1 to the heuristic,
# as per the out-of place heuristic. This performs systematically better or equal
# to the out-of-place heuristic. It performs sometimes better and sometimes worst
# than the Manhattan distance heuristic
def push_tiles(state):
    blank_idx = goal_state.index('B')
    displacements_list = []
    for idx in range(len(state)):
        if (state[idx] != goal_state[idx]) and (idx != blank_idx):
            dest_idx = goal_state.index(state[idx])
            src_idx = idx
            # number of moves this tile must make on each axis, causing others to move
            x_y = manhattan_helper(src_idx, dest_idx)
            x = x_y[0]
            y = x_y[1]
            # moves caused by this out of place tile for each tile in its way to the goal
            displacements = 0
            signum = lambda n: (1 if x > 0 else -1)
            while x != 0 or y != 0:
                # we need to move along both axis, take the least disruptive path
                if x != 0 and y != 0:
                    row_tile_to_blank = l1_dist(
                        manhattan_helper(src_idx + signum(x), blank_idx))
                    col_tile_to_blank = l1_dist(
                        manhattan_helper(src_idx + 3*signum(y), blank_idx))
                    # easier to move horizontally
                    if row_tile_to_blank < col_tile_to_blank:
                        displacements += row_tile_to_blank
                        src_idx += signum(x)
                        x -= signum(x)
                    else:
                        displacements += col_tile_to_blank
                        src_idx += 3*signum(x)
                        y -= signum(y)
                # we're only moving horizontally here...
                elif x != 0:
                    row_tile_to_blank = l1_dist(manhattan_helper(src_idx + signum(x), blank_idx))
                    displacements += row_tile_to_blank
                    src_idx += signum(x)
                    x -= signum(x)
                # column-wise movement going on here...
                else:
                    col_tile_to_blank = l1_dist(manhattan_helper(idx + 3 * signum(y), blank_idx))
                    displacements += col_tile_to_blank
                    src_idx += 3 * signum(x)
                    y -= signum(y)
                # if all we needed to do was switch places with the adjacent blank, it still counts
            if displacements == 0:
                displacements = 1
            displacements_list.append(displacements)
    if displacements_list:
        h_s = max(displacements_list) + len(displacements_list) - 1
    else:  # need this so the last node won't choke on a non-existent list
        h_s = 0
    return h_s


# this is not an optimistic heuristic and frequently overshoots. During testing, we can frequently
# observe a non-monotonic f(n)
def inadmissible(state):
    h_s = push_tiles(state) + out_of_place(state)
    return h_s


def better_heuristic(state):
    return max((manhattan(state), push_tiles(state)))


h_all = out_of_place, manhattan, min_manhattan_out_of_place, \
        push_tiles, better_heuristic, inadmissible

# pretty-print the states with less fuss
def print_8puzzle_state(state):
    print('\n- - - - - - - - - -\n')
    for row in [state[0:3], state[3:6], state[6:9]]:
        print('{:>4} {:>4} {:>4}'.format(*row))


def rand_perm(start_state, n_movs=100):
    the_state = copy.deepcopy(start_state)
    for i in range(1, n_movs):
        # choose a state_transition at random
        t_idx = random.randint(0, 3)
        # apply
        new_state = state_transitions[t_idx](the_state)
        # don't store invalid (None) transitions
        the_state = new_state if new_state else the_state
        # rinse and repeat...
    return the_state

# ---------------- end definitions for the problem ----------------------------