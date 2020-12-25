def get_loop_size(pub):
    loop_size = 1
    while True:
        if pow(7, loop_size, 20201227) == pub:
            return loop_size
        loop_size += 1


def get_encryption_key(pub, loop_size):
    return pow(pub, loop_size, 20201227)


def part1(lines):
    door_pub = int(lines[0])
    card_pub = int(lines[1])

    return get_encryption_key(door_pub, get_loop_size(card_pub))


with open('day25-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(inputs))
