from folder.big_home_module.module_simple_calc import calc
# from big_home_module.module_pro_calc import calc as pro_cack
from folder.big_home_module.module_functions import addition


# it is simple calc
value1 = float(input('enter first number'))
operation = input('enter operation: (+,-,*,/)')
value2 = float(input('enter second number'))

result = calc (a = value1, b = value2, c = operation)
print(result)


def check(a):
    if type(a) == float:
        return True
    else:
        return False


print(check(result))


### обчислення виразу
s = 2*3+result
print(s)



print(addition())


def check(a):
    if type(a) == float:
        return True
    else:
        return False


print(check(result))