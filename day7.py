SHINY_GOLD = 'shiny gold'


def extract_number_and_color(data: str) -> [int, str]:
    data = data.split(' ')
    number = int(data[0])
    color = " ".join(data[1:])
    return number, color


def clean_data(data: str) -> str:
    return data.replace('bags', '').replace('bag', '').replace('.', '').strip()


def extract_data(lines: list[str]) -> dict:
    contains = {}  # key contains values
    for line in lines:
        bag, bags_contained = line.split('contain')
        bag = clean_data(bag)

        if 'no other bags' in line:
            bags_contained = []
        else:
            bags_contained = [
                extract_number_and_color(clean_data(bag))
                for bag in bags_contained.split(',')
            ]

        contains.update({bag: bags_contained})

    return contains


def invert_relationship(contains: dict) -> dict:
    contained_by = {}  # key is contained by values
    for key in contains.keys():
        for number, color in contains[key]:
            if color not in contained_by:
                contained_by[color] = []
            contained_by[color].append((number, key))

    return contained_by


def part1(contains):
    contained_by = invert_relationship(contains)
    visited_bags = set(SHINY_GOLD)
    color_queue = [SHINY_GOLD]
    ix = 0
    while ix < len(color_queue):
        if color_queue[ix] in contained_by:
            for _number, color in contained_by[color_queue[ix]]:
                if color not in visited_bags:
                    color_queue.append(color)
                    visited_bags.add(color)
        ix += 1

    return len(color_queue) - 1


def part2(contains):
    count = 0
    color_queue = [SHINY_GOLD]
    multiplier_queue = [1]
    ix = 0
    while ix < len(color_queue):
        if color_queue[ix] in contains:
            for number, color in contains[color_queue[ix]]:
                color_queue.append(color)
                multiplier_queue.append(multiplier_queue[ix] * number)
                count += multiplier_queue[ix] * number
        ix += 1

    return count


with open('day7-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    print(part1(extract_data(inputs)))
    print(part2(extract_data(inputs)))
