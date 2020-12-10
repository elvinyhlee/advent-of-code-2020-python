from collections import Counter


def part1(nums):
    jolts = sorted(nums)
    jolts.append(jolts[-1] + 3)

    last_jolt = 0
    diffs = [0, 0, 0]

    for jolt in jolts:
        diffs[jolt - last_jolt - 1] += 1
        last_jolt = jolt

    return diffs[0] * diffs[2]


def part2(nums):
    jolts = sorted(nums)
    jolts.append(jolts[-1] + 3)

    dp = Counter()
    dp[0] = 1

    for jolt in jolts:
        dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]

    return dp[jolts[-1]]


with open('day10-data.txt') as f:
    inputs = [
        int(line)
        for line in f.read().splitlines()
    ]

    print(part1(inputs))
    print(part2(inputs))

