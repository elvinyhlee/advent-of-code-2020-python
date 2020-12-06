import string


def part1(answers_by_group: list[list[str]]) -> int:
    ans = 0
    for group_answers in answers_by_group:
        unions = set()
        for answers in group_answers:
            unions = unions.union(set(answers))
        ans += len(unions)

    return ans


def part2(answers_by_group: list[list[str]]) -> int:
    ans = 0
    for group_answers in answers_by_group:
        intersections = set(string.ascii_lowercase)
        for answers in group_answers:
            intersections = intersections.intersection(set(answers))
        ans += len(intersections)

    return ans


def extract_answers_by_group(lines: list[str]) -> list[list[str]]:
    answers_by_group = []
    answers = []
    for line in lines:
        if line == '':
            answers_by_group.append(answers)
            answers = []
        else:
            answers.append(line)
    answers_by_group.append(answers)
    return answers_by_group


with open('day6-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]
    print(part1(extract_answers_by_group(inputs)))
    print(part2(extract_answers_by_group(inputs)))
