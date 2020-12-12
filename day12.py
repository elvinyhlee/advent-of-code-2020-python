EAST = 'E'
WEST = 'W'
NORTH = 'N'
SOUTH = 'S'
FORWARD = 'F'
LEFT = 'L'
RIGHT = 'R'

directions = {
    EAST: (+1, 0),
    WEST: (-1, 0),
    NORTH: (0, +1),
    SOUTH: (0, -1),
}


def manhattan_distance(position: (int, int)) -> int:
    return abs(position[0]) + abs(position[1])


def right_rotation(position: (int, int), degree: int) -> (int, int):
    x, y = position
    if degree % 360 == 0:
        return x, y
    elif degree % 360 == 90:
        return y, -x
    elif degree % 360 == 180:
        return -x, -y
    elif degree % 360 == 270:
        return -y, x
    else:
        raise ValueError('Degree not supported')


def left_rotation(position: (int, int), degree: int) -> (int, int):
    return right_rotation(position, 360 - degree)


def part1(instructions):
    dr = directions[EAST]
    coord = (0, 0)

    for action, value in instructions:
        if action == FORWARD:
            coord = (
                coord[0] + dr[0] * value,
                coord[1] + dr[1] * value,
            )
        elif action in directions.keys():
            coord = (
                coord[0] + directions[action][0] * value,
                coord[1] + directions[action][1] * value,
            )
        elif action == LEFT:
            dr = left_rotation(dr, value)
        elif action == RIGHT:
            dr = right_rotation(dr, value)

    return manhattan_distance(coord)


def part2(instructions):
    coord = (0, 0)
    waypoint = (+10, +1)

    for action, value in instructions:
        if action == FORWARD:
            coord = (
                coord[0] + waypoint[0] * value,
                coord[1] + waypoint[1] * value,
            )
        elif action in directions.keys():
            waypoint = (
                waypoint[0] + directions[action][0] * value,
                waypoint[1] + directions[action][1] * value,
            )
        elif action == LEFT:
            waypoint = left_rotation(waypoint, value)
        elif action == RIGHT:
            waypoint = right_rotation(waypoint, value)

    return manhattan_distance(coord)


def extract_data(lines):
    data = []
    for line in lines:
        action = line[:1]
        value = int(line[1:])
        data.append((action, value))
    return data


with open('day12-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(extract_data(inputs)))
    print(part2(extract_data(inputs)))
