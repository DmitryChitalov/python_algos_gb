"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

import sys
from functools import reduce
from recordclass import recordclass, make_dataclass
from memory_profiler import profile

# Посмотрим на примере создания словаря оптимальный вариант кода
# для минимизации использования памяти

# 1. Используем встроенный dict
ob_1 = {'x': 1, 'y': 2, 'z': 3}
print(f'Размер следа встроенного словаря на Мб/1000 экз: {sys.getsizeof(ob_1)}')

# 2. Класс с доступом по имени атрибута
class Point_2:
   def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

ob_2 = Point_2(1, 2, 3)
print(f'Размер следа в виде класса на Мб/1000 экз: {sys.getsizeof(ob_2)}')

# 3. Класс с доступом по имени атрибута с использованием __slots__
class Point_3:
    __slots__ = 'a', 'b', 'c'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

ob_3 = Point_3(1, 2, 3)
print(f'Размер следа в виде класса с __slots__ на Мб/1000 экз: {sys.getsizeof(ob_3)}')

# 4. Для уменьшения памяти можно пользоваться кортежем вместо словаря
ob_4 = (1, 2, 3)
print(f'Размер следа встроенного кортежа на Мб/1000 экз: {sys.getsizeof(ob_4)}')

# 5. Создание класса с использованием библиотеки recordclass
Point_5 = recordclass('Point', ('x', 'y', 'z'))
ob_5 = Point_5(1, 2, 3)
print(f'Размер следа кортежа на основе namedtuple на Мб/1000 экз: {sys.getsizeof(ob_5)}')

# 6. Создание класса на основе ф-ции make_dataclass библиотека recordclass
Point_6 = make_dataclass('Point', ('x', 'y', 'z'))
ob_6 = Point_6(1, 2, 3)
print(f'Размер следа класс с make_dataclass на Мб/1000 экз: {sys.getsizeof(ob_6)}')

"""
Результаты измерений следа показывают, что наиболее оптимальные варианты
на основе создания классов, в частности порождение класса при помощи 
функции make_dataclass.

Размер следа встроенного словаря на Мб/1000 экз: 232
Размер следа в виде класса на Мб/1000 экз: 48
Размер следа в виде класса с __slots__ на Мб/1000 экз: 56
Размер следа встроенного кортежа на Мб/1000 экз: 64
Размер следа кортежа на основе namedtuple на Мб/1000 экз: 48
Размер следа класс с make_dataclass на Мб/1000 экз: 40
"""

""" Измерение методом профилировки:"""
@profile
def func_1():
    ob_1 = {'x': 1, 'y': 2, 'z': 3}
    return ob_1

@profile
def func_3():
    ob_3 = Point_3(1, 2, 3)
    return ob_3

@profile
def func_4():
    ob_4 = (1, 2, 3)
    return ob_4

@profile
def func_5():
    Point_5 = recordclass('Point', ('x', 'y', 'z'))
    ob_5 = Point_5(1, 2, 3)
    return ob_5

@profile
def func_6():
    Point_6 = make_dataclass('Point', ('x', 'y', 'z'))
    ob_6 = Point_6(1, 2, 3)
    return ob_6

""" Результаты профилеровки:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    70     17.4 MiB     17.4 MiB           1   @profile
    71                                         def func_1():
    72     17.4 MiB      0.0 MiB           1       ob_1 = {'x': 1, 'y': 2, 'z': 3}
    73     17.4 MiB      0.0 MiB           1       return ob_1


Filename: C:/Users/Белорыбкина/PycharmProjects/algoritms/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    75     17.4 MiB     17.4 MiB           1   @profile
    76                                         def func_3():
    77     17.4 MiB      0.0 MiB           1       ob_3 = Point_3(1, 2, 3)
    78     17.4 MiB      0.0 MiB           1       return ob_3


Filename: C:/Users/Белорыбкина/PycharmProjects/algoritms/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    80     17.4 MiB     17.4 MiB           1   @profile
    81                                         def func_4():
    82     17.4 MiB      0.0 MiB           1       ob_4 = (1, 2, 3)
    83     17.4 MiB      0.0 MiB           1       return ob_4


Filename: C:/Users/Белорыбкина/PycharmProjects/algoritms/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    85     17.4 MiB     17.4 MiB           1   @profile
    86                                         def func_5():
    87     17.4 MiB      0.0 MiB           1       Point_5 = recordclass('Point', ('x', 'y', 'z'))
    88     17.4 MiB      0.0 MiB           1       ob_5 = Point_5(1, 2, 3)
    89     17.4 MiB      0.0 MiB           1       return ob_5


Filename: C:/Users/Белорыбкина/PycharmProjects/algoritms/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    91     17.4 MiB     17.4 MiB           1   @profile
    92                                         def func_6():
    93     17.4 MiB      0.0 MiB           1       Point_6 = make_dataclass('Point', ('x', 'y', 'z'))
    94     17.4 MiB      0.0 MiB           1       ob_6 = Point_6(1, 2, 3)
    95     17.4 MiB      0.0 MiB           1       return ob_6

"""
""" Измерения методом профилировки показали, что несмотря на то, что объекты 
получаются разного объема в байтах, под них выделяется одинаковый объем памяти! 
17.4 MiB
Неожиданный результат, по условию задачи продолжим эксперимент.
В связи с отсутсвием времени замерю пример из примеров ДЗ выполненный разными способами:
"""
"""Функция возвращает сумму квадатов четных чисел от 0 до max_value"""

@profile
def function_3():
    max_value = 9999
    gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    value = reduce(lambda x, y: x + y, gen)
    del gen
    return value

@profile
def function_32():
    max_value = 9999
    gen = []
    for x in range(1, max_value):
        if x % 2 == 0:
            gen = [x ** 2]
    value = reduce(lambda x, y: x + y, gen)
    return value

if __name__ == "__main__":
    func_1()
    func_3()
    func_4()
    func_5()
    func_6()
    function_3()
    function_32()

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   155     17.5 MiB     17.5 MiB           1   @profile
   156                                         def function_3():
   157     17.5 MiB      0.0 MiB           1       max_value = 9999
   158     17.8 MiB      0.2 MiB       10001       gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
   159     17.8 MiB      0.0 MiB        9997       value = reduce(lambda x, y: x + y, gen)
   160     17.8 MiB      0.0 MiB           1       del gen
   161     17.8 MiB      0.0 MiB           1       return value


Filename: C:/Users/Белорыбкина/PycharmProjects/algoritms/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   163     17.8 MiB     17.8 MiB           1   @profile
   164                                         def function_32():
   165     17.8 MiB      0.0 MiB           1       max_value = 9999
   166     17.8 MiB      0.0 MiB           1       gen = []
   167     17.8 MiB      0.0 MiB        9999       for x in range(1, max_value):
   168     17.8 MiB      0.0 MiB        9998           if x % 2 == 0:
   169     17.8 MiB      0.0 MiB        4999               gen = [x ** 2]
   170     17.8 MiB      0.0 MiB           1       value = reduce(lambda x, y: x + y, gen)
   171     17.8 MiB      0.0 MiB           1       return value

Измерения показали, что размер выделяемой памяти все-равно не изменился
"""