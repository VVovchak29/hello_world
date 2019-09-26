
import datetime

def calc_of_date (a, b):

    if operation == '+':
        return date11 + date22

    elif operation == '-':
        return date11 - date22

    else:
        return None

date1 = input('Перша дата (рррр-мм-дд): ')
print(date1)
date1 = date1.split('-')
print(date1)

operation = input('enter operation: (+,-)')

date2 = input('Друга дата (рррр-мм-дд): ')
print(date2)
date2 = date2.split('-')
print(date2)

date11 = datetime.date(int(date1[0]),int(date1[1]),int(date1[2]))
date22 = datetime.date(int(date2[0]),int(date2[1]),int(date2[2]))


result = calc_of_date(a = date11, b = date22)
print(result)







