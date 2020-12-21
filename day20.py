class Tile:
    def __init__(self, tile: list[str], tile_id: int = 0):
        self.tile = tile
        self.id = tile_id
        self.edge_len = len(tile)

    def right_edge(self) -> str:
        return ''.join(t[-1] for t in self.tile)

    def left_edge(self) -> str:
        return ''.join(t[0] for t in self.tile)

    def top_edge(self) -> str:
        return self.tile[0]

    def bottom_edge(self) -> str:
        return self.tile[-1]

    def rotate_right(self):
        rotated = []
        for ix in range(self.edge_len):
            rotated.append(''.join([
                self.tile[self.edge_len - jx - 1][ix]
                for jx in range(self.edge_len)
            ]))
        self.tile = rotated

    def flip(self):
        flipped = []
        for t in reversed(self.tile):
            flipped.append(t)
        self.tile = flipped

    def remove_edge(self):
        removed = []
        for ix in range(1, self.edge_len - 1):
            removed.append(''.join([
                self.tile[ix][jx]
                for jx in range(1, self.edge_len - 1)
            ]))
        self.tile = removed


def check(order: list[Tile], tile: Tile, edge_size: int) -> bool:
    if len(order) + 1 - edge_size > 0:
        if tile.top_edge() != order[len(order) - edge_size].bottom_edge():
            return False
    if (len(order) + 1) % edge_size != 1:
        if tile.left_edge() != order[len(order) - 1].right_edge():
            return False
    return True


reassemble = [
    lambda tile: tile,
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.flip(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
    lambda tile: tile.rotate_right(),
]


def recursion(order, visited, tiles, edge_size) -> list[Tile]:
    if len(order) == len(tiles):
        return order

    for tile in tiles:
        if tile not in visited:
            for r in reassemble:
                r(tile)
                if check(order, tile, edge_size):
                    result = recursion(order + [tile], visited.union({tile}), tiles, edge_size)
                    if result:
                        return result


def form_pic(order: list[Tile]) -> Tile:
    tile_edge_len = order[0].edge_len - 2
    num_of_tile_in_each_edge = int(len(order) ** 0.5)

    pic_edge_len = tile_edge_len * num_of_tile_in_each_edge
    pic = ['' for _ in range(pic_edge_len)]

    for ix, tile in enumerate(order):
        tile.remove_edge()
        for jx, t in enumerate(tile.tile):
            pic[(ix // num_of_tile_in_each_edge) * tile_edge_len + jx] += t

    return Tile(pic)


def search(target: list[str], pic: Tile, print_to_terminal: bool) -> int:
    target_row_len = len(target)
    target_column_len = len(target[0])
    pic_row_len = len(pic.tile)
    pic_column_len = len(pic.tile[0])

    # For printing to terminal
    default_color = '\033[94m'
    matched_color = '\033[91m'
    p = []
    for tile in pic.tile:
        p.append([
            default_color + t
            for t in tile
        ])

    # Core logic
    count = 0
    for ix in range(0, pic_row_len - target_row_len + 1):
        for jx in range(0, pic_column_len - target_column_len + 1):
            valid = True
            for kx in range(target_row_len):
                for lx in range(target_column_len):
                    if (target[kx][lx] != ' ') and target[kx][lx] != pic.tile[ix + kx][jx + lx]:
                        valid = False
            if valid:
                count += 1

                # For printing
                for kx in range(target_row_len):
                    for lx in range(target_column_len):
                        if target[kx][lx] != ' ':
                            p[ix + kx][jx + lx] = matched_color + p[ix + kx][jx + lx][-1]

    if print_to_terminal and (count > 0):
        for line in p:
            print(''.join(line))
            print('\033[39m', end='')  # reset to white

    return count


def search_pic(target: list[str], pic: Tile, print_to_terminal: bool) -> int:
    for r in reassemble:
        r(pic)
        count = search(target, pic, print_to_terminal)
        if count:
            return count

    return 0


def part1(tiles: list[Tile]):
    size = len(tiles)
    edge_size = int(size ** 0.5)
    order = recursion([], set(), tiles, edge_size)

    upper_left = 0
    upper_right = edge_size - 1
    bottom_left = size - edge_size
    bottom_right = size - 1

    return order[upper_left].id * order[upper_right].id * order[bottom_left].id * order[bottom_right].id


def part2(tiles: list[Tile]):
    order = recursion([], set(), tiles, int(len(tiles) ** 0.5))
    pic = form_pic(order)
    sea_monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   ',
    ]
    return search_pic(['#'], pic, False) - search_pic(sea_monster, pic, True) * 15


def extract_data(lines) -> list[Tile]:
    tile_id, tile = -1, []
    tiles = []
    for line in lines:
        if 'Tile' in line:
            tile_id = int(line[5:-1])
            tile = []
        elif line:
            tile.append(line)
            is_square = len(tile) == len(tile[0])
            if is_square:
                tiles.append(Tile(tile, tile_id))
    return tiles


with open('day20-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(extract_data(inputs)))
    print(part2(extract_data(inputs)))
