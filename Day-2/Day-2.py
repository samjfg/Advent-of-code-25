"""Safe Code Day 2"""


def read_data(filename: str) -> list[str]:
    """Returns a list with each line of the file as an element."""
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def dial_at_zero_count(file_input: list[str]) -> int:
    """
    Given the list of instruction returns the number
    of times the dial passes zero.
    """
    dial_state = 50
    zero_count = 0
    for item in file_input:
        dial_state += (-1) ** (item[0] == "L") * int(item[1:])
        zero_count += (abs((dial_state - (dial_state <= 0)) //
                           100)) - (dial_state == -int(item[1:]) < 0)

        dial_state %= 100
    return zero_count


def dial_at_zero_count_alt(file_input: list[str]) -> int:
    """
    In this function I have split the logic up to make it easier to 
    comprehend, the complexity comes from the fact that calculating
    dial_state // 100, tells use the number of times that the dial has passed
    either from 99 to 0 if moving in the positive direction, or from 0 to 99
    if moving in the negative direction not actually the number of times it
    lands on 0. This is an issue because if we move in the negative direction
    and land exactly on 0 then it will not count this as the dial landing on 0
    if we then proceed to move in the positive direction afterwards it will
    not increase the count. We can counteract this by finding 
    (dial_state - 1) // 100 but only when we are moving in the negative 
    direction so we are checking if it passes from 1 to 0 instead. But then we
    also have the issue of it counting the 0 again if we move in the negative
    direction even though we have actually moved off of it rather than on.
    """
    dial_state = 50
    zero_count = 0
    for item in file_input:
        if item[0] == "L":
            dial_state -= int(item[1:])
            zero_count += -((dial_state - 1) // 100) - \
                (dial_state == -int(item[1:]))

        if item[0] == "R":
            dial_state += int(item[1:])
            zero_count += dial_state // 100

        dial_state %= 100

    return zero_count


input = read_data("input.txt")


count = dial_at_zero_count(input)
print(count)
