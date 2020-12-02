def part1(lines):
    count = 0
    for line in lines:
        limits, letter, password = line.split(' ')
        min_limit, max_limit = map(int, limits.split('-'))
        letter = letter[0]
        if max_limit >= password.count(letter) >= min_limit:
            count += 1

    return count


def part2(lines):
    count = 0
    for line in lines:
        index, letter, password = line.split(' ')
        index1, index2 = map(int, index.split('-'))
        letter = letter[0]
        if bool(password[index1-1] == letter) != bool(password[index2-1] == letter):
            count += 1

    return count


with open('day2-data.txt') as f:
    inputs = [
        line
        for line in f
    ]
    print(part1(inputs))
    print(part2(inputs))
