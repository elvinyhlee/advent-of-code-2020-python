def part1(nums):
    last_jolt = 0
    diff_1, diff_2, diff_3 = 0, 0, 0

    jolts = sorted(nums)
    jolts.append(jolts[-1] + 3)

    for jolt in jolts:
        if jolt - last_jolt == 1:
            diff_1 += 1
        elif jolt - last_jolt == 2:
            diff_2 += 1
        elif jolt - last_jolt == 3:
            diff_3 += 1

        last_jolt = jolt

    return diff_1 * diff_3


def part2(nums):
    jolts = sorted(nums)
    jolts.append(jolts[-1] + 3)

    dp = {0: 1}

    for jolt in jolts:
        dp[jolt] = 0
        if jolt - 1 in dp:
            dp[jolt] += dp[jolt - 1]
        if jolt - 2 in dp:
            dp[jolt] += dp[jolt - 2]
        if jolt - 3 in dp:
            dp[jolt] += dp[jolt - 3]

    return dp[jolts[-1]]


with open('day10-data.txt') as f:
    inputs = [
        int(line)
        for line in f.read().splitlines()
    ]

    print(part1(inputs))
    print(part2(inputs))
