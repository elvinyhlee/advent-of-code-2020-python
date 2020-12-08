import copy

ACC = 'acc'
JMP = 'jmp'
NOP = 'nop'


def run(instructions: list) -> [bool, int]:
    accumulator = 0
    visited = [False for _ in instructions]
    ix = 0
    while (0 <= ix < len(instructions)) and (not visited[ix]):
        visited[ix] = True
        operation, arg = instructions[ix]
        if operation == ACC:
            accumulator += arg
            ix += 1
        elif operation == JMP:
            ix += arg
        elif operation == NOP:
            ix += 1

    is_terminated = ix == len(instructions)
    return is_terminated, accumulator


def part1(instructions):
    _, accumulator = run(instructions)
    return accumulator


def part2(instructions):
    for ix, instruction in enumerate(instructions):
        operation, arg = instruction
        if operation in (NOP, JMP):
            instructions_copy = copy.deepcopy(instructions)
            instructions_copy[ix][0] = JMP if operation == NOP else NOP

            is_terminated, accumulator = run(instructions_copy)
            if is_terminated:
                return accumulator
    return 0


def extract_data(lines: list) -> list:
    instructions = []
    for line in lines:
        operation, arg = line.split(' ')
        instructions.append([operation, int(arg)])

    return instructions


with open('day8-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(extract_data(inputs)))
    print(part2(extract_data(inputs)))
