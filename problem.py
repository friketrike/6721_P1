
# Comp 6721 AI, Project 1, fall 2016
# Federico O'Reilly Regueiro 40012304

# Problem class


class Problem:
    """Common class for all problems subject to search, construct with ... TODO docs"""
    def __init__(self, node_goal_test, state_transitions, h=lambda state: 1):
        self.node_goal_test = node_goal_test
        self.state_transitions = state_transitions
        self.h = h


class Node:
    """"Problem node for search TODO fill in later"""
    def __init__(self, the_problem, state, cost=0, parent=None, children=[]):
        self.parent = parent
        self.cost = cost
        self.children = children
        self.state = state
        self.problem = the_problem
        self.h = the_problem.h(state)

    def expand(self):
        for t in self.problem.state_transitions:
            self.children.append(Node(self.problem, t(self.state), self.cost+1, parent=self, children=[]))

    def goal_test(self):
        return self.problem.node_goal_test(self)
