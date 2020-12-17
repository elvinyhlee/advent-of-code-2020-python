import itertools
import copy

ACTIVE = '#'
INACTIVE = '.'


def part1(data):
    # Initialize grid
    grid = [[['.' for _ in range(24)] for _ in range(24)] for _ in range(24)]
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[12][ix+9][jx+9] = j

    # Run 6 cycles
    for _ in range(6):
        grid_clone = copy.deepcopy(grid)
        for i in range(24):
            for j in range(24):
                for k in range(24):
                    count_active = 0
                    for z in itertools.product([0, 1, -1], repeat=3):
                        if not(z == (0, 0, 0))\
                                and (0 <= i + z[0] <= 23) \
                                and (0 <= j + z[1] <= 23) \
                                and (0 <= k + z[2] <= 23) \
                                and grid[i+z[0]][j+z[1]][k+z[2]] == ACTIVE:
                            count_active += 1

                    if (grid[i][j][k] == ACTIVE) and (not(2 <= count_active <= 3)):
                        grid_clone[i][j][k] = INACTIVE

                    if (grid[i][j][k] == INACTIVE) and (count_active == 3):
                        grid_clone[i][j][k] = ACTIVE
        grid = grid_clone

    # Count active cubes
    active = 0
    for i in range(24):
        for j in range(24):
            for k in range(24):
                if grid[i][j][k] == ACTIVE:
                    active += 1
    return active


def part2(data):
    # Initialize grid
    grid = [[[['.' for _ in range(24)] for _ in range(24)] for _ in range(24)] for _ in range(24)]
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[12][12][ix+9][jx+9] = j

    # Run 6 cycles
    for _ in range(6):
        grid_clone = copy.deepcopy(grid)
        for i in range(24):
            for j in range(24):
                for k in range(24):
                    for l in range(24):
                        count_active = 0
                        for z in itertools.product([0, 1, -1], repeat=4):
                            if not(z == (0, 0, 0, 0))\
                                    and (0 <= i + z[0] <= 23) \
                                    and (0 <= j + z[1] <= 23) \
                                    and (0 <= k + z[2] <= 23) \
                                    and (0 <= l + z[3] <= 23) \
                                    and (grid[i+z[0]][j+z[1]][k+z[2]][l+z[3]] == ACTIVE):
                                count_active += 1

                        if (grid[i][j][k][l] == ACTIVE) and not(2 <= count_active <= 3):
                            grid_clone[i][j][k][l] = INACTIVE

                        if (grid[i][j][k][l] == INACTIVE) and (count_active == 3):
                            grid_clone[i][j][k][l] = ACTIVE
        grid = grid_clone

    # Count active cubes
    active = 0
    for i in range(24):
        for j in range(24):
            for k in range(24):
                for l in range(24):
                    if grid[i][j][k][l] == ACTIVE:
                        active += 1
    return active


with open('day17-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(inputs))
    print(part2(inputs))
