"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
from math import factorial


def number_of_paths(grid_size):
    return factorial(2 * grid_size) // factorial(grid_size) ** 2


print(number_of_paths(20))
