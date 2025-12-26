"""Day 2, invalid inputs, part 2"""


def read_data(filename: str) -> list[str]:
    """Returns a list with each line of the file as an element."""
    with open(filename, "r") as f:
        return f.read().strip().split(",")


def invalid_inputs_sum(input_data):
    """Returns the sum of all repeating patterns in the given input list."""
    invalid_list = []
    for id in input_data:
        id_range = id.split("-")

        for i in range(int(id_range[0]), int(id_range[1]) + 1):
            x = str(i)
            x_max = x[:(len(x) // 2)]
            pattern = ""

            for digit in x_max:
                pattern += digit
                x_pattern = pattern * (len(x) // len(pattern))

                if x_pattern == x:
                    invalid_list.append(int(x_pattern))

    return sum(set(invalid_list))


input_data = read_data("input.txt")

invalid_sum = invalid_inputs_sum(input_data)

print(invalid_sum)
