import copy


def calculate_score(p):
    score = 0
    factor = len(p)
    for i in p:
        score += i * factor
        factor -= 1
    return score


def play_game(p1: list[int], p2: list[int], recursive: bool) -> [int, list]:
    p1_records = []
    p2_records = []

    while p1 and p2:
        # Keep records
        if (p1 in p1_records) or (p2 in p2_records):
            return 1, p1
        p1_records.append(p1)
        p2_records.append(p2)

        # Draw cards and battle
        p1_draw = p1[0]
        p2_draw = p2[0]
        p1 = p1[1:]
        p2 = p2[1:]

        if recursive and p1_draw <= len(p1) and p2_draw <= len(p2):
            c_p1 = copy.deepcopy(p1)[:p1_draw]
            c_p2 = copy.deepcopy(p2)[:p2_draw]
            winner, _ = play_game(c_p1, c_p2, recursive)
            if winner == 1:
                p1 += [p1_draw, p2_draw]
            else:
                p2 += [p2_draw, p1_draw]

        elif p1_draw > p2_draw:
            p1 += [p1_draw, p2_draw]
        else:
            p2 += [p2_draw, p1_draw]

    return (1, p1) if p1 else (2, p2)


def part1(data):
    p1, p2 = data
    _, p = play_game(p1, p2, recursive=False)
    return calculate_score(p)


def part2(data):
    p1, p2 = data
    _, p = play_game(p1, p2, recursive=True)
    return calculate_score(p)


def extract_data(lines):
    split_ix = lines.index('')
    p1 = [int(i) for i in lines[1: split_ix]]
    p2 = [int(i) for i in lines[split_ix + 2: len(lines)]]
    return p1, p2


with open('day22-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(extract_data(inputs)))
    print(part2(extract_data(inputs)))
