def get_target_from_binary_instructions(
    leftmost: int,
    rightmost: int,
    left_instruction: str,
    right_instruction: str,
    instructions: str,
) -> int:
    l_ix, r_ix = leftmost, rightmost
    for instruction in instructions:
        if instruction == left_instruction:
            r_ix = (r_ix - l_ix + 1) // 2 + l_ix - 1
        elif instruction == right_instruction:
            l_ix = (r_ix - l_ix + 1) // 2 + l_ix

    # Note: l_ix and r_ix should be the same
    return l_ix


def get_seat_id(instructions: str) -> int:
    row_instructions = instructions[:7]
    column_instructions = instructions[7:]
    row = get_target_from_binary_instructions(0, 127, 'F', 'B', row_instructions)
    column = get_target_from_binary_instructions(0, 7, 'L', 'R', column_instructions)

    return row * 8 + column


def nth_partial_sum(n: int) -> int:
    return n * (n + 1) // 2


def part1(lines):
    highest_seat_id = 0
    for line in lines:
        seat_id = get_seat_id(line)
        highest_seat_id = max(highest_seat_id, seat_id)

    return highest_seat_id


def part2(lines):
    sum_of_seat_id = 0
    highest_seat_id = 0
    lowest_seat_id = float('inf')

    for line in lines:
        seat_id = get_seat_id(line)
        highest_seat_id = max(highest_seat_id, seat_id)
        lowest_seat_id = min(lowest_seat_id, seat_id)
        sum_of_seat_id += seat_id

    return nth_partial_sum(highest_seat_id) - nth_partial_sum(lowest_seat_id - 1) - sum_of_seat_id


with open('day5-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    print(part1(inputs))
    print(part2(inputs))
