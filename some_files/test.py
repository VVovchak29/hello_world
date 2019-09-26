#1 Ну по-перше list є змінювальним типом а tuple не змінювальним, тобто ми можимо в list робити зі елементами все що
#захочемо( добавляти елементи, удаляти елементи,сортіровка), а в tuple  ме не можемо робити цього, але tuple краще використовувати
###коли є великі бази даних і вони вже сформовані, вони є займають менше памяті і швидші за list.

#2 змінювальні типи:list,dictionary,set. незмінювальні типи: int,float,tuple,srting,frosenset.
#
#3 Функція в python - об'єкт, який приймає аргументи і повертає значення.
# Функція визначається за допомогою інструкції def. Return - це коли щось повертає, коли ми визвали функцію і передаєм їй
#конкретне значення, для того щоб використовувати цю функцію в інших функція чи ще.
#Функція може бути будь-якої складності і повертати будь-які об'єкти (списки, кортежі, і навіть функції, ,будеві значення)
#Функція може приймати будь-яку кількість аргументів чи не приймати їх зовсім.
#
#4 1)буде надруковано всі імена


#  2) [1],[2, 3, 1],[1, 1]
#




#5
# a = [1,2,3,4,5,6,7,8,9]
# count=0
# for i in a:
#     if i%2==0 and i%4==0:
#         count+=1
# print(count)
# 6
# b = a[:5]
# print(b)
# c = b.pop()
# print(c)
#7
# def check(a,b):
#     return a==b and a%2==0 and b%2==0
#
#
# print(check(6,6))
#8
# s = '12332'
# if s==s[::-1]:
#     print(True)
# else:
#     print(False)
#9
# dictionary={
#     'name':'pine_yard',
#     'owner':'Ivan_ivanuch',
#     'year_of_opening':'1977',
#     'adress':{'city':'kiev',
#                'street':'lomonosova',
#                'number_of_building':'67'},
# }
# dictionary['name']= 'yard'
# dictionary['schedule']= 'round the clock'
# print(dictionary['name'])
#10
#

# for i in range(100):
#     if i%2==0 :
#         if i == 6 or i == 8 or i == 86:
#             continue
#         if i == 90:
#             break
#         print(i)



##11
# a = 125
# c = list(str(a))
# print(c)
# s=0
# for i in c:
#     d=int(i)
#     s=s+d
# print(s)

##12 Знайти найбільший спільний дільник двох чисел
# def f(x):
#     q=[]
#     for i in range(1,x+1):
#         if x%i==0:
#             q.append(i)
#     return q
# q1=f(12)
# q2=f(8)
# max=-10
# for i in q1:
#     if i in q2:
#         max=i
# print(max)

#13
# a = [1,2,3,4,5,6,7,8,9]
# b = [4,5,7]
# c = [0,1,2,3,4,5]
# d = [8,9]# 0 тому що 0 ділеться на 5
# count=0
# for i in a:
#     for j in b:
#         for k in c:
#             for u in d:
#                 print(i,j,k,u)
#                 count += 1
# print(count)
#14 	Є файл з даними учнів у форматі Прізвище;ім’я;зріст
#Написати функцію що зчитує дані з файлу, функцію що добавляє учня до списку,
# функцію що перевіряє чи є валідним  формат даних що вводить користувач,
# три функції що обчислюють максимальний, мінімальний і середній зріст.
def read_file(x):

    with open(x,'r') as f:
      return f.read()

y = read_file('list_of_pupils')

def plus_to_list(m):

    result=[]

    b = m.split('\n')

    b.pop()

    for i in b:
        c=i.split(';')

        d={'surname': c[0], 'name': c[1], 'hight': c[2]}
        result.append(d)
    return result

p=plus_to_list(y)
print(p)

#ВАЛІДНІСТЬ НЕ ЗНАЮ ЯК ЗРОБИТИ і


 