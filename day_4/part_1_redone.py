"""Redone Day 4 part 1"""


import numpy as np


def load_data(file):
    """Loads the data grid in as a numpy array."""
    with open(file, "r", encoding="utf-8") as f:
        return np.array([list(line.strip()) for line in f])


def accessible_rolls(data):
    """Returns the number of accessible rolls of wrapping paper."""
    neighbours = np.zeros((data.shape[0] + 2, data.shape[1] + 2))

    donut = np.ones((3, 3))
    donut[1, 1] = 0

    for i, j in zip(*np.where(data == "@")):
        neighbours[i:i+3, j:j+3] += donut

    neighbour_counts = neighbours[1:-1, 1:-1]

    return np.sum((data == "@") & (neighbour_counts < 4))


input_data = load_data("input.txt")

accessible_sum = accessible_rolls(input_data)
print(accessible_sum)
