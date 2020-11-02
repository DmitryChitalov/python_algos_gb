"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import cProfile
import collections

simple_dict = {}
order_dict = collections.OrderedDict()


def dict_update():
    for i in range(10000000):
        simple_dict.setdefault(i)


def dict_get():
    for i in range(10000000):
        simple_dict.get(i)


def order_dict_update():
    for i in range(10000000):
        order_dict.setdefault(i)


def order_dict_get():
    for i in range(10000000):
        order_dict.get(i)


print(f"Добавление в стандартный словарь")
cProfile.run('my_dict_update()')

print(f"Извлечение из стандартного словаря")
cProfile.run('my_dict_get()')

print(f"Добавление в OrderedDict")
cProfile.run('my_order_dict_update()')

print(f"Извлечение из OrderedDict")
cProfile.run('my_order_dict_get()')

'''
Добавление в стандартный словарь
         10000004 function calls in 3.744 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.744    3.744 <string>:1(<module>)
        1    2.168    2.168    3.744    3.744 task_4.py:15(my_dict_update)
        1    0.000    0.000    3.744    3.744 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 10000000    1.576    0.000    1.576    0.000 {method 'setdefault' of 'dict' objects}


Извлечение из стандартного словаря
         10000004 function calls in 3.722 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.722    3.722 <string>:1(<module>)
        1    2.280    2.280    3.722    3.722 task_4.py:20(my_dict_get)
        1    0.000    0.000    3.722    3.722 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 10000000    1.441    0.000    1.441    0.000 {method 'get' of 'dict' objects}


Добавление в OrderedDict
         10000004 function calls in 4.504 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    4.503    4.503 <string>:1(<module>)
        1    2.202    2.202    4.503    4.503 task_4.py:25(my_order_dict_update)
        1    0.000    0.000    4.504    4.504 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 10000000    2.302    0.000    2.302    0.000 {method 'setdefault' of 'collections.OrderedDict' objects}


Извлечение из OrderedDict
         10000004 function calls in 3.768 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.768    3.768 <string>:1(<module>)
        1    2.324    2.324    3.768    3.768 task_4.py:30(my_order_dict_get)
        1    0.000    0.000    3.768    3.768 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
 10000000    1.444    0.000    1.444    0.000 {method 'get' of 'dict' objects}


Стандартный славарь работает быстрее чем orderDict.
'''
