def get_first_invalid_num(nums, preamble_len):
    for index, num in enumerate(nums):
        if index >= preamble_len:
            check = False
            previous_nums = nums[index - preamble_len: index]

            for ix, i in enumerate(previous_nums):
                for jx, j in enumerate(previous_nums):
                    if ix > jx:
                        if i + j == num:
                            check = True
            if not check:
                return num
    return -1


def get_continuous_set_that_sum_to_target(nums, target):
    sum_of_set = 0
    left_ix = 0
    right_ix = 0

    # sliding window solution
    while (left_ix <= right_ix) and (right_ix < len(nums)):
        next_num = nums[right_ix]
        if sum_of_set + next_num < target:
            sum_of_set += next_num
            right_ix += 1
        elif sum_of_set + next_num == target:
            return nums[left_ix: right_ix + 1]
        else:
            while (sum_of_set + next_num > target) and (left_ix < right_ix):
                sum_of_set -= nums[left_ix]
                left_ix += 1


def part1(nums):
    return get_first_invalid_num(nums, 25)


def part2(nums):
    first_invalid_num = get_first_invalid_num(nums, 25)
    continuous_set = get_continuous_set_that_sum_to_target(nums, first_invalid_num)
    return min(continuous_set) + max(continuous_set)


with open('day9-data.txt') as f:
    inputs = [
        int(line)
        for line in f.read().splitlines()
    ]

    print(part1(inputs))
    print(part2(inputs))
