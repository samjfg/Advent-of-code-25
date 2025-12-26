"""Day 2, invalid id's, part 1"""


def read_data(filename: str) -> list[str]:
    """Returns a list with each line of the file as an element."""
    with open(filename, "r") as f:
        return f.read().strip().split(",")


def invalid_inputs_sum(input_data):
    """Returns the sum of all of the invalid inputs."""
    invalid_list = []
    for id in input_data:
        id_range = id.split("-")
        for i in range(int(id_range[0]), int(id_range[1]) + 1):
            x = str(i)
            if x[:(len(x) // 2)] == x[(len(x) // 2):]:
                invalid_list.append(i)

    return sum(invalid_list)


input_data = read_data("input.txt")

invalid_sum = invalid_inputs_sum(input_data)

print(invalid_sum)
