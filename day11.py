import copy

directions = [(+1, 0), (-1, 0), (0, +1), (0, -1), (-1, -1), (+1, -1), (+1, +1), (-1, +1)]

EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
FLOOR = '.'


def number_of_occupied_seats(layout: list[str]) -> int:
    count = 0
    for row in layout:
        count += row.count(OCCUPIED_SEAT)
    return count


def number_of_occupied_immediately_adjacent_seats(layout: list[str], row_ix: int, col_ix: int) -> int:
    count = 0
    row_len = len(layout)
    col_len = len(layout[row_ix])
    for row_dir, column_dir in directions:
        rix = row_ix + row_dir
        cix = col_ix + column_dir
        if (0 <= rix < row_len) and (0 <= cix < col_len) and (layout[rix][cix] == OCCUPIED_SEAT):
            count += 1
    return count


def number_of_occupied_first_next_seats(layout: list[str], row_ix: int, col_ix: int) -> int:
    count = 0
    row_len = len(layout)
    col_len = len(layout[row_ix])
    for row_dir, column_dir in directions:
        rix = row_ix + row_dir
        cix = col_ix + column_dir
        while (0 <= rix < row_len) and (0 <= cix < col_len):
            if layout[rix][cix] == EMPTY_SEAT:
                break
            if layout[rix][cix] == OCCUPIED_SEAT:
                count += 1
                break
            rix += row_dir
            cix += column_dir
    return count


def run_rules(
    initial_layout: list[str],
    tolerance_lvl: int,
    care_immediately_adjacent_seats: bool,
) -> list[str]:

    prev_layout = []
    layout = copy.deepcopy(initial_layout)

    while layout != prev_layout:
        prev_layout = copy.deepcopy(layout)
        layout = []

        for row_ix, prev_row in enumerate(prev_layout):
            row = ''

            for col_ix, prev_position in enumerate(prev_row):
                if care_immediately_adjacent_seats:
                    num = number_of_occupied_immediately_adjacent_seats(prev_layout, row_ix, col_ix)
                else:
                    num = number_of_occupied_first_next_seats(prev_layout, row_ix, col_ix)

                if num == 0 and prev_position == EMPTY_SEAT:
                    row += OCCUPIED_SEAT
                elif num >= tolerance_lvl and prev_position == OCCUPIED_SEAT:
                    row += EMPTY_SEAT
                else:
                    row += prev_position

            layout.append(row)

    return layout


def part1(lines):
    final_layout = run_rules(lines, 4, True)
    return number_of_occupied_seats(final_layout)


def part2(lines):
    final_layout = run_rules(lines, 5, False)
    return number_of_occupied_seats(final_layout)


with open('day11-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(inputs))
    print(part2(inputs))
