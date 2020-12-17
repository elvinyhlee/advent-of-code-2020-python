import itertools
import copy

ACTIVE = '#'
INACTIVE = '.'


def part1(data):
    # Initialize grid
    rows = len(data)
    columns = len(data[0])
    loops = 6
    expanded = loops * 2

    grid = [[['.' for _ in range(columns + expanded)] for _ in range(rows + expanded)] for _ in range(1 + expanded)]
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[loops][ix + loops][jx + loops] = j

    # Run 6 cycles
    si = sj = sk = loops - 1  # s means start from

    for loop in range(loops):
        grid_clone = copy.deepcopy(grid)

        range_expanded = 2 * (loop + 1)
        for i in range(1 + range_expanded):
            for j in range(rows + range_expanded):
                for k in range(columns + range_expanded):
                    count_active = 0
                    for z in itertools.product([0, 1, -1], repeat=3):
                        if not(z == (0, 0, 0))\
                                and (0 <= i + si + z[0] < 1 + expanded) \
                                and (0 <= j + sj + z[1] < rows + expanded) \
                                and (0 <= k + sk + z[2] < columns + expanded) \
                                and (grid[i + si + z[0]][j + sj + z[1]][k + sk + z[2]] == ACTIVE):
                            count_active += 1

                    if (grid[i + si][j + sj][k + sk] == ACTIVE) and (not(2 <= count_active <= 3)):
                        grid_clone[i + si][j + sj][k + sk] = INACTIVE

                    if (grid[i + si][j + sj][k + sk] == INACTIVE) and (count_active == 3):
                        grid_clone[i + si][j + sj][k + sk] = ACTIVE
        grid = grid_clone
        si, sj, sk = si - 1, sj - 1, sk - 1

    # Count active cubes
    active = 0
    for i in range(1 + expanded):
        for j in range(rows + expanded):
            for k in range(columns + expanded):
                if grid[i][j][k] == ACTIVE:
                    active += 1
    return active


def part2(data):
    # Initialize grid
    rows = len(data)
    columns = len(data[0])
    loops = 6
    expanded = loops * 2

    grid = [[[['.' for _ in range(columns + expanded)] for _ in range(rows + expanded)]
             for _ in range(1 + expanded)] for _ in range(1 + expanded)]
    for ix, i in enumerate(data):
        for jx, j in enumerate(i):
            grid[loops][loops][ix + loops][jx + loops] = j

    # Run 6 cycles
    si = sj = sk = sl = loops - 1  # s means start from

    for loop in range(loops):
        grid_clone = copy.deepcopy(grid)

        range_expanded = 2 * (loop + 1)
        for i in range(1 + range_expanded):
            for j in range(1 + range_expanded):
                for k in range(rows + range_expanded):
                    for l in range(columns + range_expanded):
                        count_active = 0
                        for z in itertools.product([0, 1, -1], repeat=4):
                            if not(z == (0, 0, 0, 0))\
                                    and (0 <= i + si + z[0] < 1 + expanded) \
                                    and (0 <= j + sj + z[1] < 1 + expanded) \
                                    and (0 <= k + sk + z[2] < rows + expanded) \
                                    and (0 <= l + sl + z[3] < columns + expanded) \
                                    and (grid[i + si + z[0]][j + sj + z[1]][k + sk + z[2]][l + sl + z[3]] == ACTIVE):
                                count_active += 1

                        if (grid[i + si][j + sj][k + sk][l + sl] == ACTIVE) and (not(2 <= count_active <= 3)):
                            grid_clone[i + si][j + sj][k + sk][l + sl] = INACTIVE

                        if (grid[i + si][j + sj][k + sk][l + sl] == INACTIVE) and (count_active == 3):
                            grid_clone[i + si][j + sj][k + sk][l + sl] = ACTIVE
        grid = grid_clone
        si, sj, sk, sl = si - 1, sj - 1, sk - 1, sl - 1

    # Count active cubes
    active = 0
    for i in range(1 + expanded):
        for j in range(1 + expanded):
            for k in range(rows + expanded):
                for l in range(columns + expanded):
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
