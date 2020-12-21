import copy


def recursion(visited: list, a_i: list) -> list:
    visited_len = len(visited)

    if visited_len == len(a_i):
        return visited

    _, i = a_i[visited_len]
    for ing in i:
        if ing not in visited:
            result = recursion(visited + [ing], a_i)
            if result:
                return result


def solve(food: list[tuple[list, list]], part: int):
    # "a" means allergens, "i" means ingredients
    all_a = set()
    all_i = set()
    for i, a in food:
        all_a = all_a.union(set(a))
        all_i = all_i.union(set(i))

    # Find out all the allergens and the respective possible ingredients
    a_i = []

    for target in all_a:
        possible_i = set()

        for i, a in food:
            if target in a:
                possible_i = possible_i.intersection(i) if possible_i else set(i)

        a_i.append((target, possible_i))

    if part == 1:
        # Get the inert ingredients
        inert = copy.deepcopy(all_i)
        for _, ingredients in a_i:
            inert -= ingredients

        # Count the number of appearance of the inert ingredients
        count = 0
        for i, _ in food:
            count += len(inert.intersection(i))

        return count

    if part == 2:
        result = recursion([], a_i)
        sorted_mapping = sorted(list(zip([a for a, _ in a_i], result)))
        return ','.join([i for _, i in sorted_mapping])


def extract_data(lines):
    food = []
    for line in lines:
        ingredients, allergens = line.split('(contains ')
        ingredients = ingredients[:-1].split(' ')
        allergens = allergens[:-1].replace(',', '').split(' ')
        food.append((ingredients, allergens))

    return food


with open('day21-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(solve(extract_data(inputs), part=1))
    print(solve(extract_data(inputs), part=2))
