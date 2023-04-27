import os
from collections import deque

from core.parser import add_border, load_grid

OFF_GRID = ' '


class GridSearchProblem:

    def __init__(self, **kwargs):
        grid_file = kwargs.get('filename') or os.path.join('data', 'grid.txt')
        self.grid = add_border(load_grid(filename=grid_file))
        if kwargs.get('start'):
            x, y = self._findStart()
            self._changeGridAtCoord(x, y, '*')
            self.start = kwargs['start']
            x, y = self.start
            self._changeGridAtCoord(x, y, 'S')
        else:
            self.start = self._findStart()
        if kwargs.get('goal'):
            x, y = self._findGoal()
            self._changeGridAtCoord(x, y, '*')
            self.goal = kwargs['goal']
            x, y = self.goal
            self._changeGridAtCoord(x, y, 'G')
        else:
            self.goal = self._findGoal()
        start_x, _ = self.start
        goal_x, _ = self.goal
        self.path_char = '<' if goal_x < start_x else '>'

    def _findStart(self):
        return self._findElem('S')

    def _findGoal(self):
        return self._findElem('G')

    def _findElem(self, elem):
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char == elem:
                    return x, y
        return None, None

    def _changeGridAtCoord(self, x, y, elem):
        self.grid[y] = self.grid[y][:x] + elem + self.grid[y][x + 1:]

    def getGridPoints(self):
        pts = []
        for y, line in enumerate(self.grid):
            for x, char in enumerate(line):
                if char != OFF_GRID:
                    pts.append((x, y))
        return pts

    def getStartState(self):
        return self.start

    def isGoal(self, state):
        return state == self.goal

    def getSuccessors(self, state):
        x, y = state
        successors = []
        for location in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            x_dir, y_dir = location
            new_x = x + x_dir
            new_y = y + y_dir
            if self.grid[y][x] != OFF_GRID:
                successors.append((new_x, new_y))
        return successors

    def plotSolution(self, path):
        output = ""
        for x, y in path[:-1]:
            self._changeGridAtCoord(x, y, self.path_char)
        for line in self.grid:
            output += line.rstrip() + "\n"
        return output


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
