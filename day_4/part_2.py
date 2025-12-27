"""Day 4, part 1, forklift optimisation."""


import numpy as np


def load_data(file):
    """Loads the input data as an array."""
    with open(file, "r", encoding="utf-8") as f:
        return np.array([list(line.strip()) for line in f])


def accessible_rolls(data):
    """Returns the number of accessible rolls of wrapping paper."""
    donut = np.ones((3, 3))
    donut[1, 1] = 0

    sum = 0

    reducible = True

    while reducible:
        neighbours = np.zeros((data.shape[0] + 2, data.shape[1] + 2))

        for i, j in zip(*np.where(data == "@")):
            neighbours[i:i+3, j:j+3] += donut

        neighbour_counts = neighbours[1:-1, 1:-1]

        accessible = np.sum((data == "@") & (neighbour_counts < 4))
        sum += accessible

        if not accessible:
            reducible = False

        data[(data == "@") & (neighbour_counts < 4)] = "."

    return sum


input_data = load_data("input.txt")

roll_sum = accessible_rolls(input_data)
print(roll_sum)
