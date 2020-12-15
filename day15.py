def play(starting_nums: list[int], stop_at: int) -> int:
    mem = {}
    for ix, num in enumerate(starting_nums):
        mem[num] = (-1, ix+1)  # (previous, latest)

    ix = len(starting_nums)
    latest = starting_nums[-1]
    while ix < stop_at:
        ix += 1
        if (latest not in mem) or (mem[latest][0] == -1):
            latest = 0
            mem[latest] = (mem[latest][1], ix)
        else:
            latest = mem[latest][1] - mem[latest][0]
            if latest not in mem:
                mem[latest] = (-1, ix)
            else:
                mem[latest] = (mem[latest][1], ix)

    return latest


def part1(data):
    return play(data, 2020)


def part2(data):
    return play(data, 30000000)


with open('day15-data.txt') as f:
    inputs = [
        int(i)
        for i in f.read().split(',')
    ]

    print(part1(inputs))
    print(part2(inputs))
