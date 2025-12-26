"""Day 2 Part 1 Battery Joltage"""


def load_input(file: str) -> list[list[int]]:
    """Returns file data as a list."""
    with open(file, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f]


def sum_max_joltage(data: list[list[int]]) -> int:
    """Returns the sum of the maximum joltage's of each battery bank."""
    joltages = []
    for bank in data:
        digits = ""
        last_index = 0
        for i in range(11, -1, -1):
            digits += max(bank[last_index:len(bank)-i])
            last_index = bank[last_index:].index(digits[-1]) + last_index + 1
        joltages.append(int(digits))

    return sum(joltages)


input_data = load_input("input.txt")

max_voltage = sum_max_joltage(input_data)
print(max_voltage)
