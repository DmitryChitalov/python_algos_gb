"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit
import random


def my_dict_append(n):
    for i in range(n):
        my_dict[random.randint(1, 10000000000)] = i
    return my_dict


def my_ordered_dict_append(n):
    for i in range(n):
        my_ordered_dict[random.randint(1, 10000000000)] = i
    return my_ordered_dict


def my_dict_read():
    for k, v in my_dict.items():
        pass
    return


def my_ordered_dict_read():
    for k, v in my_ordered_dict.items():
        pass
    return


def my_dict_pop(n):
    for i in range(n):
        my_dict.popitem()
    return my_dict


def my_ordered_dict_pop(n):
    for i in range(n):
        my_ordered_dict.popitem()
    return my_ordered_dict


n = 10 ** 3

my_dict = {x: x for x in range(1, n)}
my_ordered_dict = OrderedDict(my_dict)

# print(my_dict)

print('добавление в конец словаря')
print(timeit('my_dict_append(n)', globals=globals(), number=1000))

print('добавление в конец упорядоченного словаря')
print(timeit('my_ordered_dict_append(n)', globals=globals(), number=1000))

print('перебор словаря')
print(timeit('my_dict_read()', globals=globals(), number=100))

print('перебор упорядоченного словаря')
print(timeit('my_ordered_dict_read()', globals=globals(), number=100))

print('удаление из словаря')
print(timeit('my_dict_pop(n)', globals=globals(), number=100))

print('удаление из упорядоченного словаря')
print(timeit('my_ordered_dict_pop(n)', globals=globals(), number=100))

"""
по всем тестам обычный словарь (Python 3.9) работает быстрее упорядочного словаря. 
Причем, для операций перебора элементов, разрыв по скорости составляет в 10 раз 

добавление в конец словаря
1.201698
добавление в конец упорядоченного словаря
1.3755759
перебор словаря
2.8558075
перебор упорядоченного словаря
20.6744221
удаление из словаря
0.023361100000002466
удаление из упорядоченного словаря
0.03864249999999814
"""
