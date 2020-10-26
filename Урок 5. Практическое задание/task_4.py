"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict, deque
from random import randint
import cProfile


dct = dict()
odct = OrderedDict()


def named(n):
    """Создание порядкового имени для словаря"""
    sn = 'abcdefghijklmnopqrstuvwxyz'
    name = deque()
    while n >= 0:
        name.appendleft(sn[n % len(sn)])
        n = n // len(sn) - 1
    return ''.join(name)


def append(a, el_count=1000):
    """Добавление определенного количества элементов в словарь (или именнованный словарь OrderedDict)

    :param a: Словарь
    :param el_count: Количество элементов
    """
    for i in range(el_count):
        a[named(i)] = randint(0, 100)


def get_items(a, el_count=1000):
    """Запрос случайных элементов словаря

    """
    keys = list(a.keys())
    for _ in range(el_count):
        i = a[keys[randint(0, len(keys) - 1)]]


def del_items(a, el_count=1000):
    """Удаление случайных элементов словаря

    """
    keys = list(a.keys())
    for _ in range(el_count):
        k = randint(0, len(keys) - 1)
        i = a.pop(keys[k])
        keys.pop(k)


def test_dict(a, el_count=100):
    """Тестирование словарей

    """
    # Наполнение списка первыми данными в конец
    append(a, el_count * 2)
    # Запрос данных из словаря
    get_items(a, el_count)
    # Удаление части данных из словаря
    del_items(a, el_count)


def test_odict(a, el_count=100):
    """Тестирование очередей deque

    """
    # Наполнение списка первыми данными в конец
    append(a, el_count * 2)
    # Запрос данных из словаря
    get_items(a, el_count)
    # Удаление части данных из словаря
    del_items(a, el_count)


def repeat_test_dict(a, el_count=100, repeat=3):
    """Тестирование словарей dict несколько раз

    :param a: Словарь Dict
    :param el_count: Количество элементов для добавления/извлечения
    :param repeat: Сколько раз повторить
    """
    for _ in range(repeat):
        test_dict(a, el_count)


def repeat_test_odict(a, el_count=100, repeat=3):
    """Тестирование именованных словарей OrderedDict несколько раз

    :param a: словарь OrderedDict
    :param el_count: Количество элементов для добавления/извлечения
    :param repeat: Сколько раз повторить
    """
    for _ in range(repeat):
        test_odict(a, el_count)


#########################################
# Тестируем dict
cProfile.run('repeat_test_dict(dct, 10000, 5)')
""" >>>
2396404 function calls in 1.624 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.624    1.624 <string>:1(<module>)
   200000    0.237    0.000    0.509    0.000 random.py:200(randrange)
   200000    0.123    0.000    0.633    0.000 random.py:244(randint)
   200000    0.177    0.000    0.272    0.000 random.py:250(_randbelow_with_getrandbits)
   100000    0.312    0.000    0.509    0.000 task_4.py:17(named)
        5    0.117    0.023    0.937    0.187 task_4.py:27(append)
        5    0.056    0.011    0.223    0.045 task_4.py:37(get_items)
        5    0.079    0.016    0.463    0.093 task_4.py:46(del_items)
        5    0.001    0.000    1.624    0.325 task_4.py:57(test_dict)
        1    0.000    0.000    1.624    1.624 task_4.py:81(repeat_test_dict)
        1    0.000    0.000    1.624    1.624 {built-in method builtins.exec}
   709940    0.105    0.000    0.105    0.000 {built-in method builtins.len}
   304970    0.048    0.000    0.048    0.000 {method 'appendleft' of 'collections.deque' objects}
   200000    0.036    0.000    0.036    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   281460    0.058    0.000    0.058    0.000 {method 'getrandbits' of '_random.Random' objects}
   100000    0.062    0.000    0.062    0.000 {method 'join' of 'str' objects}
       10    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
    50000    0.019    0.000    0.019    0.000 {method 'pop' of 'dict' objects}
    50000    0.192    0.000    0.192    0.000 {method 'pop' of 'list' objects}
"""

#########################################
# Тестируем OrderedDict
cProfile.run('repeat_test_odict(odct, 10000, 5)')
""" >>>
2397218 function calls in 1.570 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.570    1.570 <string>:1(<module>)
   200000    0.223    0.000    0.477    0.000 random.py:200(randrange)
   200000    0.116    0.000    0.593    0.000 random.py:244(randint)
   200000    0.166    0.000    0.255    0.000 random.py:250(_randbelow_with_getrandbits)
   100000    0.294    0.000    0.478    0.000 task_4.py:17(named)
        5    0.119    0.024    0.888    0.178 task_4.py:27(append)
        5    0.061    0.012    0.219    0.044 task_4.py:37(get_items)
        5    0.079    0.016    0.461    0.092 task_4.py:46(del_items)
        5    0.001    0.000    1.570    0.314 task_4.py:69(test_odict)
        1    0.000    0.000    1.570    1.570 task_4.py:92(repeat_test_odict)
        1    0.000    0.000    1.570    1.570 {built-in method builtins.exec}
   709940    0.099    0.000    0.099    0.000 {built-in method builtins.len}
   304970    0.044    0.000    0.044    0.000 {method 'appendleft' of 'collections.deque' objects}
   200000    0.034    0.000    0.034    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   282274    0.054    0.000    0.054    0.000 {method 'getrandbits' of '_random.Random' objects}
   100000    0.060    0.000    0.060    0.000 {method 'join' of 'str' objects}
       10    0.000    0.000    0.000    0.000 {method 'keys' of 'collections.OrderedDict' objects}
    50000    0.038    0.000    0.038    0.000 {method 'pop' of 'collections.OrderedDict' objects}
    50000    0.183    0.000    0.183    0.000 {method 'pop' of 'list' objects}
"""


""" Вывод:
OrderedDict при тестировании cProfile показал немного лучшие результаты чем стандартные словари dict:

Наполнение случайными данными (append):
    dict()          -> 0.937
    OrderedDict()   -> 0.888
Запрос случайных данных (get_items):
    dict()          -> 0.223
    OrderedDict()   -> 0.219
Запрос случайных данных (del_items):
    dict()          -> 0.463
    OrderedDict()   -> 0.461

"""
