"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from random import randint, choice
from string import ascii_lowercase


# Deco:

def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Runs for {} sec.'.format(end - start))
    return wrapper


# list

@benchmark
def my_lst():
    lst = [randint(1, 99) for el in range(300)]
    return lst

my_lst()


# dict

@benchmark
def my_dict():
    a_dict = {}
    keys = range(1, 300)
    values = ''.join(choice(ascii_lowercase) for _ in range(300))
    for i in keys:
        a_dict[i] = values[i]
    return a_dict

my_dict()


'''У меня вышло так, что операции со словарем (в range(1, 50/100/150/200/250/300) происходили всегда быстрее, 
    особенно с холодного старта пк. Полагаю, словарь выигрывает главным образом за счет своей особенности 
    'ключ-значение', которое существенно убыстряет процесс поиска и перебора значений. '''



