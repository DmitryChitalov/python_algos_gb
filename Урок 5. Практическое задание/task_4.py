"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict
from random import randint

my_dict = {a: randint(0, 100) for a in range(1000)}
ord_dict = OrderedDict(my_dict)

print('Возврат пар ключ:значение')
print(timeit('my_dict.items()', 'from __main__ import my_dict', number=100000))
print(timeit('ord_dict.items()', 'from __main__ import ord_dict', number=100000))

print('Изменение элемента по ключу')
print(timeit('my_dict[0]=1', 'from __main__ import my_dict', number=100000))
print(timeit('ord_dict[0]=1', 'from __main__ import ord_dict', number=100000))

print('Получение списка значений')
print(timeit('my_dict.values()', 'from __main__ import my_dict', number=100000))
print(timeit('ord_dict.values()', 'from __main__ import ord_dict', number=100000))


"""
Результаты замеров показали, что разницы во времени при использовании orderdect нет, смысла использовать эту коллекцию 
на Python 3.7 я не вижу
    Возврат пар ключ:значение
    0.006680662000000004
    0.006315386999999999
    Изменение элемента по ключу
    0.0032786959999999976
    0.005226388000000005
    Получение списка значений
    0.006513947999999999
    0.005750210999999998
"""