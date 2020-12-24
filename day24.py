EAST = 'e'
WEST = 'w'
SOUTHEAST = 'se'
SOUTHWEST = 'sw'
NORTHWEST = 'nw'
NORTHEAST = 'ne'


direction = {
    EAST: (+2, 0),
    WEST: (-2, 0),
    SOUTHEAST: (+1, -1),
    SOUTHWEST: (-1, -1),
    NORTHEAST: (+1, +1),
    NORTHWEST: (-1, +1),
}


def part1(tiles):
    black_coord = set()

    for tile in tiles:
        coord = (0, 0)
        for i in tile:
            coord = (coord[0] + direction[i][0], coord[1] + direction[i][1])

        if coord in black_coord:
            black_coord.remove(coord)
        else:
            black_coord.add(coord)

    return len(black_coord)


def count_adjacent_black_tiles(coord: tuple, black_coord: set[tuple]) -> int:
    return sum(
        1 if (coord[0] + d[0], coord[1] + d[1]) in black_coord else 0
        for d in direction.values()
    )


def part2(tiles):
    # Copied from part 1
    black_coord = set()

    for tile in tiles:
        coord = (0, 0)
        for i in tile:
            coord = (coord[0] + direction[i][0], coord[1] + direction[i][1])

        if coord in black_coord:
            black_coord.remove(coord)
        else:
            black_coord.add(coord)

    # Core logic for part 2
    for i in range(100):
        new_black_coord = set()

        min_x, max_x = float('inf'), float('-inf')
        min_y, max_y = float('inf'), float('-inf')
        for coord in black_coord:
            min_x, max_x = min(min_x, coord[0]), max(max_x, coord[0])
            min_y, max_y = min(min_y, coord[1]), max(max_y, coord[1])

        for j in range(min_x - 2, max_x + 2 + 1):
            for k in range(min_y - 1, max_y + 1 + 1):
                coord = (j, k)
                count = count_adjacent_black_tiles(coord, black_coord)

                if coord in black_coord:
                    if 0 < count <= 2:
                        new_black_coord.add(coord)
                elif count == 2:
                    new_black_coord.add(coord)

        black_coord = new_black_coord

    return len(black_coord)


def extract_data(lines):
    tiles = []
    for line in lines:
        tile = []
        ix = 0
        while ix < len(line):
            if line.startswith((EAST, WEST), ix):
                tile.append(line[ix])
                ix += 1
            else:
                tile.append(line[ix:ix+2])
                ix += 2
        tiles.append(tile)

    return tiles


with open('day24-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(extract_data(inputs)))
    print(part2(extract_data(inputs)))
