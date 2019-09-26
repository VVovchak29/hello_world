
def calc (a, b):

    if operation == '+':
        return a + b

    elif operation == '-':
        return a - b

    elif operation == '*':
        return a * b

    elif operation == '/':
        return a / b

    else:
        return None

value = float(input('enter first number'))
operation = input('enter operation (+,-,*,/)')
result = value

while True:
    value1 = float(input('enter number'))
    result = calc (a = result, b = value1)
    print(result)
    operation = input('enter operation (+,-,*,/) or result')
    if operation == 'result':
        print(result)
        break