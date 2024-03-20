def calculate(s):
    stack = []
    num = 0
    operator = '+'
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in '+-*/':
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack[-1] *= num
            elif operator == '/':
                stack[-1] = int(stack[-1] / num)
            num = 0
            operator = char
    if operator == '+':
        stack.append(num)
    elif operator == '-':
        stack.append(-num)
    elif operator == '*':
        stack[-1] *= num
    elif operator == '/':
        stack[-1] = int(stack[-1] / num)
    return sum(stack)
expression = "3 + 2 * 2"
result = calculate(expression)
print(f"The result of evaluating '{expression}' is {result}.")
