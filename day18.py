def perform_operation(stack: list, num: int) -> list[str]:
    while stack:
        if stack[-1] == '(':
            break
        operator, left_operand = stack[-1], stack[-2]
        stack = stack[:-2]
        if operator == '+':
            num = left_operand + num
        elif operator == '*':
            num = left_operand * num

    stack.append(num)

    return stack


def perform_advance_operation(stack: list, num: int, close_bracket: bool) -> list[str]:
    # Perform "*" operations
    if close_bracket:
        ix = -1
        # Find the last position of open bracket - "("
        for sx, s in enumerate(stack):
            if s == '(':
                ix = sx

        if ix != -1:
            target_stack = stack[ix+1:]
            stack = stack[:ix]
        else:
            target_stack = stack
            stack = []

        for s in target_stack:
            if s != '*':  # only "*" and digits are in the target stack
                num *= int(s)

    # Perform "+" operations
    while stack:
        if stack[-1] in '(*':
            break
        operator, left_operand = stack[-1], stack[-2]
        stack = stack[:-2]
        if operator == '+':
            num = left_operand + num

    stack.append(num)

    return stack


def calculate(expression: str, advance: bool) -> int:
    stack = []
    ix = 0
    while ix < len(expression):
        if expression[ix] in '1234567890':
            num = int(expression[ix])
            if advance:
                stack = perform_advance_operation(stack, num, close_bracket=False)
            else:
                stack = perform_operation(stack, num)

        elif expression[ix] in '*+(':
            stack.append(expression[ix])

        elif expression[ix] in ')':
            num = int(stack[-1])
            if advance:
                stack = stack[:-1]
                stack = perform_advance_operation(stack, num, close_bracket=True)
            else:
                stack = stack[:-2]  # stack[-2] must be "("
                stack = perform_operation(stack, num)
        ix += 1

    if advance and (len(stack) > 1):
        stack = perform_advance_operation(stack[:-1], int(stack[-1]), close_bracket=True)

    return int(stack[0])  # should only be 1 value left at the end


def part1(expressions):
    ans = 0
    for expression in expressions:
        ans += calculate(expression, advance=False)
    return ans


def part2(expressions):
    ans = 0
    for expression in expressions:
        ans += calculate(expression, advance=True)
    return ans


with open('day18-data.txt') as f:
    inputs = [
        expression
        for expression in f.read().splitlines()
    ]

    print(part1(inputs))
    print(part2(inputs))
