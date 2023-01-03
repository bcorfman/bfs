from core.search import GridSearchProblem, breadth_first_search


def test_bfs_start_and_goal_are_the_same():
    problem = GridSearchProblem(start=(7, 15), goal=(7, 15))
    path = breadth_first_search(problem)
    assert path == []


def test_bfs_one_step():
    problem = GridSearchProblem(start=(7, 15), goal=(7, 16))
    path = breadth_first_search(problem)
    assert path == [(7, 16)]


def test_bfs_multi_step():
    problem = GridSearchProblem(start=(7, 15), goal=(8, 16))
    path = breadth_first_search(problem)
    assert path == [(7, 16), (8, 16)]


def test_bfs_grid_problem():
    problem = GridSearchProblem()
    path = breadth_first_search(problem)
    assert len(path) == 35
