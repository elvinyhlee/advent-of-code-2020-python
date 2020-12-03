import math


def get_tree_count(geology, x_move, y_move):
    count = 0
    y_coord, x_coord = 0, 0
    y_length, x_length = len(geology), len(geology[0])

    while (y_coord + 1) <= y_length:
        if geology[y_coord][x_coord % x_length] == '#':
            count += 1
        x_coord += x_move
        y_coord += y_move

    return count


def part1(geology):
    return get_tree_count(geology, 3, 1)


def part2(geology):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    return math.prod(
        [
            get_tree_count(geology, slope[0], slope[1])
            for slope in slopes
        ]
    )


with open('day3-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    print(part1(inputs))
    print(part2(inputs))
