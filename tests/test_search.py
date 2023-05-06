import pytest

from core.search import GridSearchProblem, breadth_first_search


@pytest.mark.unit
def test_bfs_goal_out_of_bounds():
    problem = GridSearchProblem(start=(15, 7), goal=(50, 7))
    path = breadth_first_search(problem)
    assert path is None


@pytest.mark.unit
def test_bfs_start_is_one_row_outside_of_grid():
    problem = GridSearchProblem(start=(26, 6), goal=(44, 7))
    path = breadth_first_search(problem)
    assert path is None


@pytest.mark.unit
def test_bfs_start_and_goal_are_the_same():
    problem = GridSearchProblem(start=(15, 7), goal=(15, 7))
    path = breadth_first_search(problem)
    assert path == []


@pytest.mark.unit
def test_bfs_one_step():
    problem = GridSearchProblem(start=(15, 7), goal=(16, 7))
    path = breadth_first_search(problem)
    assert path == [(16, 7)]


@pytest.mark.unit
def test_bfs_multi_step():
    problem = GridSearchProblem(start=(15, 7), goal=(16, 8))
    path = breadth_first_search(problem)
    assert path == [(15, 8), (16, 8)]


@pytest.mark.unit
def test_bfs_grid_problem():
    problem = GridSearchProblem()
    path = breadth_first_search(problem)
    assert len(path) == 35
