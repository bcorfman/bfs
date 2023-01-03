MAX_GRID_WIDTH = 80


def load_grid(**kwargs):
    with open(kwargs['filename']) as gf:
        grid = gf.readlines()
    return grid


def add_border(grid):
    new_grid = [MAX_GRID_WIDTH * ' ']
    for line in grid:
        new_grid.append(line.ljust(MAX_GRID_WIDTH-1, ' ').rjust(MAX_GRID_WIDTH, ' '))
    new_grid.append(MAX_GRID_WIDTH * ' ')
    return new_grid
