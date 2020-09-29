"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit
from random import choice, randint

my_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'i': 8,
    'h': 9,
    'j': 0
}
my_OrderDict = OrderedDict(my_dict)

print(timeit("""
sum = 0 
for key, val in my_dict.items():
    sum += val
""", "from __main__ import my_dict"))

print(timeit("""
sum = 0 
for key, val in my_OrderDict.items():
    sum += val
""", "from __main__ import my_OrderDict"))

print(timeit("""
for i in range(3):
    n_key = choice('klmnopqrstuvwxyz1234567890')
    my_dict[n_key] = randint(0, 100)
""", "from __main__ import my_dict, choice, randint"))

print(timeit("""
for i in range(3):
    n_key = choice('klmnopqrstuvwxyz1234567890')
    my_OrderDict[n_key] = randint(0, 100)
""", "from __main__ import my_OrderDict, choice, randint"))

"""
Вывод:
    Все происходит примерно одинаково.
"""
# print(my_dict)
# print(my_OrderDict)
