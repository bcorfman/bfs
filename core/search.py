import os
from collections import deque

from core.parser import add_border, load_grid

OFF_GRID = ' '


class Coord:
    def __init__(self, elem):
        self.row = elem[0]
        self.col = elem[1]


class GridSearchProblem:
    def __init__(self, **kwargs):
        grid_file = kwargs.get('filename') or os.path.join('data', 'grid.txt')
        self.grid = add_border(load_grid(filename=grid_file))
        self.start = kwargs.get('start') or self._findStart()
        self.goal = kwargs.get('goal') or self._findGoal()
        _, start_col = self.start
        _, goal_col = self.goal
        self.path_char = '<' if goal_col < start_col else '>'

    def _findStart(self):
        return self._findElem('S')

    def _findGoal(self):
        return self._findElem('G')

    def _findElem(self, elem):
        for row, line in enumerate(self.grid):
            for col, char in enumerate(line):
                if char == elem:
                    return row, col
        return None, None

    def getStartState(self):
        return self.start

    def isGoal(self, state):
        return state == self.goal

    def getSuccessors(self, state):
        row, col = state
        successors = []
        for location in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            row_dir, col_dir = location
            new_row = row + row_dir
            new_col = col + col_dir
            if self.grid[new_row][new_col] != OFF_GRID:
                successors.append((new_row, new_col))
        return successors

    def plotSolution(self, path):
        for row, col in path[:-1]:
            self.grid[row] = self.grid[row][:col] + self.path_char + self.grid[row][col+1:]
        for line in self.grid:
            print(line.rstrip())


def breadth_first_search(problem):
    path = ()
    frontier = deque([(problem.getStartState(), path)])
    explored = set()
    while frontier:
        node = frontier.popleft()
        state, path = node
        if problem.isGoal(state):
            return list(path)
        for new_state in problem.getSuccessors(state):
            new_path = tuple(list(path) + [new_state])
            new_node = new_state, new_path
            if new_state not in explored:
                explored.add(new_state)
                frontier.append(new_node)
    return None
