def check_sequence(grammar, seq, string):
    if not seq:
        yield string
    else:
        index, *seq = seq
        for string in run(grammar, index, string):
            yield from check_sequence(grammar, seq, string)


def run_expand(grammar, alt, string):
    for seq in alt:
        yield from check_sequence(grammar, seq, string)


def run(grammar, index, string):
    if isinstance(grammar[index], list):
        yield from run_expand(grammar, grammar[index], string)
    else:
        if string and string[0] == grammar[index]:
            yield string[1:]


def match(grammar, string):
    return any(m == '' for m in run(grammar, '0', string))


def part1(data):
    rules, messages = data
    return sum(match(rules, message) for message in messages)


def part2(data):
    rules, messages = data
    rules = {
        **rules,
        '8': [['42'], ['42', '8']],
        '11': [['42', '31'], ['42', '11', '31']]
    }
    return sum(match(rules, message) for message in messages)


def extract_data(lines):
    # e.g. rules
    # {
    #     '0': [['4', '1', '5']],
    #     '1': [['2', '3'], ['3', '2']],
    #     '2': [['4', '4'], ['5', '5']],
    #     '3': [['4', '5'], ['5', '4']],
    #     '4': 'a',
    #     '5': 'b'
    # }
    ix = 0
    rules = {}
    while lines[ix] != '':
        line = lines[ix]
        num, rule = line.split(':')
        if 'a' in rule:
            rules[num] = 'a'
        elif 'b' in rule:
            rules[num] = 'b'
        else:
            rules[num] = []
            for r in rule.split('|'):
                rules[num].append(r.strip().split(' '))
        ix += 1

    # e.g. messages
    # ['ababbb', 'bababa', 'abbbab', 'aaabbb', 'aaaabbb']
    ix += 1
    messages = []
    while ix < len(lines):
        messages.append(lines[ix])
        ix += 1

    return rules, messages


with open('day19-data.txt') as f:
    inputs = [
        line
        for line in f.read().splitlines()
    ]

    print(part1(extract_data(inputs)))
    print(part2(extract_data(inputs)))
