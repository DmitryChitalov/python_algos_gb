"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

# реализовал по 2 функции заполнения списка и словаря, но почему-то список заполняется быстрее, чем словарь
import time

def fil_list():
    list = []
    list = [x for x in range(100000)]

    return 0

def fil_dict():
    dict = {}
    dict = {x: x for x in range(100000)}
    return 0

time1start = time.time()
fil_list()
time1fin = time.time()
print('Время заполнения списка равно: ', time1fin - time1start)

time2start = time.time()
fil_dict()
time2fin = time.time()
print('Время заполнения словаря равно: ', time2fin - time2start)

def fil_list_2():
    list = []
    for x in range(100000):
        list.append[x]

def fil_dict_2():
    dict = {}
    for x in range(100000):
        dict[x] = x

print()
time3start = time.time()
fil_list()
time3fin = time.time()
print('Время заполнения списка равно: ', time3fin - time3start)

time4start = time.time()
fil_dict()
time4fin = time.time()
print('Время заполнения словаря равно: ', time4fin - time4start)