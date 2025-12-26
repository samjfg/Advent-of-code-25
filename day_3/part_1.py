"""Day 2 Part 1 Battery Joltage"""


def load_input(file: str) -> list[list[int]]:
    """Returns file data as a list."""
    with open(file, "r", encoding="utf-8") as f:
        return [list(line.strip()) for line in f]


def sum_max_joltage(data: list[list[int]]) -> int:
    """Returns the sum of the maximum joltage's of each battery bank."""
    joltages = []
    for bank in data:
        digit_one = max(bank[:-1])
        digit_two = max(bank[(bank.index(digit_one) + 1):])
        joltages.append(int(f"{digit_one}{digit_two}"))

    return sum(joltages)


input_data = load_input("input.txt")

max_voltage = sum_max_joltage(input_data)
print(max_voltage)
