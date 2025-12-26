"""Day 4, part 1, forklift optimisation."""


import numpy as np


def load_data(file):
    with open(file, "r", encoding="utf-8") as f:
        # return [list(line) for line in f]
        return np.array([list(line.strip()) for line in f])


"""The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions."""


def accessible_rolls(data):
    """Returns the number of accessible rolls of wrapping paper."""
    neighbours = np.zeros((data.shape[0] + 2, data.shape[1] + 2))
    donut = np.ones((3, 3))
    donut[1, 1] -= 1
    for row_index, row in enumerate(input_data):
        for column_index, element in enumerate(row):
            if element == "@":
                neighbours[row_index:row_index + 3,
                           column_index:column_index + 3] += donut

    neighbour_zip = zip(
        neighbours[1:-1, 1:-1].ravel().tolist(), data.ravel().tolist())
    accessible = list(
        filter(lambda x: x[0] < 4 and x[1] == "@", neighbour_zip))

    return len(accessible)
    # return empty_array, np.sum(empty_array[1:-1, 1:-1] < 4)
    # = empty_array[1:-1, 1:-1]
    # for i, element in enumerate():
    # return empty_array[1:-1, 1:-1]
    # return sum[]


input_data = load_data("input.txt")
# input_data = np.array([
#     list("..@@.@@@@."),
#     list("@@@.@.@.@@"),
#     list("@@@@@.@.@@"),
#     list("@.@@@@..@."),
#     list("@@.@@@@.@@"),
#     list(".@@@@@@@.@"),
#     list(".@.@.@.@@@"),
#     list("@.@@@.@@@@"),
#     list(".@@@@@@@@."),
#     list("@.@.@@@.@.")
# ])

roll_sum = accessible_rolls(input_data)
print(roll_sum)
# flattened = ", ".join(input_data[1:-1].tolist())
# print(type(flattened))
# print(flattened)
# print(len(flattened))
# print(list(filter(lambda x: x == "@", flattened)))

# donut = np.ones((3, 3))
# donut[1, 1] -= 1
# arr = np.zeros((4, 4))
# print(arr)
# arr[0:3, 0:3] += donut
# print(arr)
