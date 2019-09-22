#
# def calc (a, b):
#
#     if operation == '+':
#         return value1 + value2
#
#     elif operation == '-':
#         return value1 - value2
#
#     elif operation == '*':
#         return value1 * value2
#
#     elif operation == '/':
#         return value1 / value2
#
#     else:
#         return None
#
# value1 = float(input('enter first number'))
# operation = input('enter operation: (+,-,*,/)')
# value2 = float(input('enter second number'))
#
# result = calc (a = value1, b = value2)
# print(result)



# def calc (a, b):
#
#     if operation == '+':
#         return a + b
#
#     elif operation == '-':
#         return a - b
#
#     elif operation == '*':
#         return a * b
#
#     elif operation == '/':
#         return a / b
#
#     else:
#         return None
#
# value = float(input('enter first number'))
# operation = input('enter operation (+,-,*,/)')
# result = value
#
# while True:
#     value1 = float(input('enter number'))
#     result = calc (a = result, b = value1)
#     print(result)
#     operation = input('enter operation (+,-,*,/) or result')
#     if operation == 'result':
#         print(result)
#         break




s='2+2*1.2'


from simpleeval import simple_eval
c=simple_eval((input('write example')))
print(c)
print(type(c))