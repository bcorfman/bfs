import os
from app.parser import load_grid, add_border


def test_load_grid():
    grid_file = os.path.join('data', 'grid.txt')
    grid = load_grid(filename=grid_file)
    assert grid[6][14] == 'S'


def test_add_border():
    grid_file = os.path.join('data', 'grid.txt')
    grid = load_grid(filename=grid_file)
    grid = add_border(grid)
    assert grid[7][15] == 'S'
