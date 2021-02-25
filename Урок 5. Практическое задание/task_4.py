"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import random
from collections import OrderedDict
from timeit import timeit

def create_d(n = 100000):
    """
    Создание обычного словая на 1000000 записей случайными числами
    """
    keys = list(range(n))
    vals = [random.randint(10,99) for i in range(n)]
    d = dict(zip(keys,vals))
    
    return d

def create_od(n = 100000):
    """
    Создание упорядоченного словая на 1000000 записей случайными числами
    """
    keys = list(range(n))
    vals = [random.randint(10,99) for i in range(n)]
    od = OrderedDict(zip(keys,vals))
    
    return od

d = create_d()
od = create_od()


def pop_item_d(dct, n =500):
    """ Извлекаем 500 значений из словаря"""
    for _ in range(n):
        dct.popitem()
    return


def mult_elem_d(dct, n=10):
    """
    Умножаем элементы словаря на n

    """
    for key in dct.keys():
        dct[key] = dct[key]*2
       
    return dct

print('1. Создание обычного словаря ',
      timeit('create_d()', 'from __main__ import create_d', number= 100)
)
print('2. Создание упорядоченного словаря ',
      timeit('create_od()', 'from __main__ import create_od', number= 100)
)


print('3. Извлечение значений из словаря ',
      timeit('pop_item_d(d)', 'from __main__ import pop_item_d, create_d, d', number= 100)
)
print('4. Извлечение значений из  упорядоченного словаря ',
      timeit('pop_item_d(od)', 'from __main__ import pop_item_d, create_od, od', number= 100)
)


print('5. Перебор элементов словаря ',
      timeit('mult_elem_d(d)', 'from __main__ import mult_elem_d, d', number= 100)
)
print('6. Перебор элементов упорядоченного словаря ',
      timeit('mult_elem_d(od)', 'from __main__ import mult_elem_d, od', number= 100)
)
"""
Python 3.8.7 (default, Dec 21 2020, 20:10:35) 
[GCC 7.5.0] on linux
python3 'Урок 5. Практическое задание/task_4.py'
1. Создание обычного словаря  41.09404565600562
2. Создание упорядоченного словаря  43.806727294002485
3. Извлечение значений из словаря  0.007582436999655329
4. Извлечение значений из  упорядоченного словаря  0.012271175997739192
5. Перебор элементов словаря  2.08520607000537
6. Перебор элементов упорядоченного словаря  2.7016330219994416

На современных версиях python значительной разницы между обычным словарем и упорядоченным словарем не наблюдается. Однако во всех испытаниях OrderedDict работает чуть медленнеe.
"""