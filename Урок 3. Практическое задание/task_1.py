"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import random
import time
rand = random.randint(1000000, 5000000)


def auto_lst(int):
    start_time = time.time()
    lst = [i for i in range(int)]
    end_time = time.time()
    return end_time - start_time


def auto_dict(int):
    start_time = time.time()
    dct = {i: i for i in range(int)}
    end_time = time.time()
    return end_time - start_time


print(f'список создается {auto_lst(rand)} секунд')
print(f'словарь создается {auto_dict(rand)} секунд')
print(f'количество элементов {rand}')

"""словарь создается примерно на 50% дольше. Полагаю, что это происходит в том числе за счет
 времени, потраченного на изначальное хеширования ключей"""


def lst_pop(int):
    lst = [i for i in range(int)]
    start_time = time.time()
    lst.pop(10)
#    lst.pop(int - 1)
    end_time = time.time()
    return  end_time - start_time


def dct_pop(int):
    dct = {i: i for i in range(int)}
    start_time = time.time()
    dct.pop(10)
#    dct.pop(int-1)
    end_time = time.time()
    return end_time - start_time


print(f'возвращает элемент из списка {lst_pop(rand)} секунд')
print(f'возвращает элемент из словаря {dct_pop(rand)} секунд')
print(f'количество элементов {rand}')

"""В случае, когда извлекаемый элемент задан числом, словарь выполняет это действие моментально, в то время,
как в списке на это уходит время. По идее, сложность pop в словаре - константа, а в списке O(n), и за счет 
использования хеша нет необходимости делать проход по всему словарю. НО. Когда я задал номер элемента
не числом, а int - 1, то и у списка действие выполнилось моментально. Почему?"""
