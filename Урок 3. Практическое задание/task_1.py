"""
Задание 1.
Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
'''
n = int(input('Размер списка: '))
j = input("Введите элимент списка: ")
i = 0

user_sp = []
for i in range(n):
    user_sp.append(j)

print(user_sp)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

n = int(input('Размер списка: '))
j = input("Введите элимент списка: ")
i = 0

user_sp = []
for i in range(n):
    user_sp.extend(j)

print(user_sp)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
'''

import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(args[0])
        print(time.time() - start_time)
    return wrapper


@time_it
def test_list(n):
    list_obj = []
    for i in range(n):
        list_obj.append(i)
        list_obj.index(i)
    return list_obj


@time_it
def test_dict(n):
    dict_obj = dict()
    for i in range(n):
        dict_obj[i] = i
        dict_obj.get(i)
    return dict_obj


test_list(10000)
test_dict(10000)
