"""
    The world is modeled as a 2-D array of cells, where 0 represents
    uninfected cells, and 1 represents cells contaminated with the
    virus. A wall (and only one wall) can be installed between any
    two 4-directionally adjacent cells, on the shared boundary.
"""
def load_basic_grid(option:int=0) -> list:
    DEFAULT_GRIDS = (
        # Example 1
        [[0, 1, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0]],
        # Example 2
        [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]],
        # Example 3
        [[1, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 1, 1, 1, 1],
         [1, 1, 1, 0, 0, 0, 0, 0, 0]]
    )
    if option > len(DEFAULT_GRIDS):
        print(f'The option {option} is invalid. Please choose a value under{len(DEFAULT_GRIDS)}')
        option = 0
    return DEFAULT_GRIDS[option]