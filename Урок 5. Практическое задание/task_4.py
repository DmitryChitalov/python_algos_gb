"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit
l_od = OrderedDict()
l_od['3'] = 'a'
l_od['1'] = 'b'
l_od['2'] = 'c'

l_d = dict()
l_d['3'] = 'a'
l_d['2'] = 'b'
l_d['1'] = 'c'

def add_elem_od():
    l_od['4'] = 'c'

def add_elem_d():
    l_d['4'] = 'c'

print(l_od)
print(l_d)
add_elem_d()
add_elem_od()
print('add_elem_d',timeit(f'add_elem_d()',globals=globals()))
print('add_elem_od',timeit(f'add_elem_od()',globals=globals()))

# Вывод: при одинаковой операции (Добавление пары Ключ = значение) идентичным методом, Ordinary Dict по времени равен обычному словарю. 0.11 против 0.11
# Но при этом Ordinary Dict сохранил порядок вставки.
