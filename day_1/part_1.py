"""Day 1, Safe Code, Part 1"""


def read_data(filename: str) -> list[str]:
    """Returns a list with each line of the file as an element."""
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def dial_at_zero_count(file_input: list[str]) -> int:
    """
    Given the list of instruction returns the number 
    of times the dial lands on zero.
    """
    dial_state = 50
    zero_count = 0
    for item in file_input:
        dial_state += (-1) ** (item[0] == "L") * int(item[1:])
        dial_state %= 100
        if not dial_state:
            zero_count += 1
    return zero_count


instructions = read_data("input.txt")

count = dial_at_zero_count(instructions)
print(count)
