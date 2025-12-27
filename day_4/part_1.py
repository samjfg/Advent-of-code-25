"""Day 4, part 1, forklift optimisation."""


import numpy as np


def load_data(file):
    """Loads the data grid in as a numpy array."""
    with open(file, "r", encoding="utf-8") as f:
        return np.array([list(line.strip()) for line in f])


def accessible_rolls(data):
    """Returns the number of accessible rolls of wrapping paper."""
    neighbours = np.zeros((data.shape[0] + 2, data.shape[1] + 2))
    donut = np.ones((3, 3))
    donut[1, 1] -= 1
    for row_index, row in enumerate(data):
        for column_index, element in enumerate(row):
            if element == "@":
                neighbours[row_index:row_index + 3,
                           column_index:column_index + 3] += donut

    neighbour_zip = zip(
        neighbours[1:-1, 1:-1].ravel().tolist(), data.ravel().tolist())
    accessible = list(
        filter(lambda x: x[0] < 4 and x[1] == "@", neighbour_zip))

    return len(accessible)


input_data = load_data("input.txt")

roll_sum = accessible_rolls(input_data)
print(roll_sum)
