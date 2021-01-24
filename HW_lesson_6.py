# ************************************************ Task 1 *************************************************************
"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
# ---------------------------------------------------------------------------------------------------------------------
#
# Для тестов использовались: Python 3.8, Windows 10 x64, AMD FX-8300 Eight-Core Processor 3.30 GHz, RAM 16 Gb
#
# ---------------------------------------------------------------------------------------------------------------------
from memory_profiler import profile
import timeit
import math
import sys
import numpy as np


def timer(function):
    def new_function(*args, **kwargs):
        start_time = timeit.default_timer()
        ret = function(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        print(f'Время выполнения функции: {elapsed:.04f}')
        return ret

    return new_function


#
# ----------------------- 1) Определение количества максимальных элементов списка -------------------------------------
#


@timer
@profile
def f_new():
    lst = list(range(100000))
    max_el = max(lst)
    quantity = lst.count(max_el)
    del lst
    return quantity


f_new()

'''
Для запуска программы было выделено 15.7 MiB. При создании списка "lst" было выделено еще 1.9 MiB.
После выполнения программы удалил список, тем самым освободил память (1.6 MiB).
По времени: удаление списка увеличивает время выполнения пррограммы.

Результат выполнения программы:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     15.7 MiB     15.7 MiB           1   @timer
    43                                         @profile
    44                                         def f_new():
    45     17.6 MiB      1.9 MiB           1       lst = list(range(100000))
    46     17.6 MiB      0.0 MiB           1       max_el = max(lst)
    47     17.6 MiB      0.0 MiB           1       quantity = lst.count(max_el)
    48     16.0 MiB     -1.6 MiB           1       del lst
    49     16.0 MiB      0.0 MiB           1       return quantity

Время выполнения функции: 0.0796
'''

#
# ----------------------------------------- 2) Вычисление факториала --------------------------------------------------
#

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

num = 4000


@timer
@profile
def recursion(n):
    def factorial(x):
        if x == 1:
            return x
        else:
            return x * factorial(x - 1)

    print(f'Факториал числа {num}: {factorial(n)}')


@timer
@profile
def for_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f'Факториал числа {n}: {fact}')


@timer
@profile
def math_factorial(n):
    fact = math.factorial(n)
    print(f'Факториал числа {n}: {fact}')


recursion(num)
for_factorial(num)
math_factorial(num)

"""
Результат выполнения программы:

Функция recursion():
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24     15.7 MiB     15.7 MiB           1   @timer
    25                                         @profile
    26                                         def recursion(n):
    27     19.6 MiB      2.8 MiB        4001       def factorial(x):
    28     19.6 MiB      1.0 MiB        4000           if x == 1:
    29     19.6 MiB      0.0 MiB           1               return x
    30                                                 else:
    31     19.6 MiB  -2112.4 MiB        3999               return x * factorial(x - 1)
    32                                         
    33     18.4 MiB     -1.2 MiB           1       print(f'Факториал числа {num}: {factorial(n)}')

Время выполнения функции: 0.6416


Функция for_factorial():
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    36     18.5 MiB     18.5 MiB           1   @timer
    37                                         @profile
    38                                         def for_factorial(n):
    39     18.5 MiB      0.0 MiB           1       fact = 1
    40     18.5 MiB      0.0 MiB        4000       for i in range(2, n+1):
    41     18.5 MiB      0.0 MiB        3999           fact *= i
    42     18.5 MiB      0.0 MiB           1       print(f'Факториал числа {n}: {fact}')

Время выполнения функции: 0.4014


Функция math_factorial()
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    45     18.5 MiB     18.5 MiB           1   @timer
    46                                         @profile
    47                                         def math_factorial(n):
    48     18.5 MiB      0.0 MiB           1       fact = math.factorial(n)
    49     18.5 MiB      0.0 MiB           1       print(f'Факториал числа {n}: {fact}')

Время выполнения функции: 0.0168


ВЫВОД: 
    Начнем с рекурсии. В Python установлен лимит на вызов рекурсии равный 1000 итераций. Чтобы убрать это ограничение
    приходится подключать модуль sys. Следующая проблема - объем RAM, моего хватило на 4000 вызовов рекурсии, остальные 
    две программы (for_factorial и math_factorial) спокойно перешагивали этот рубеж. Конечно, это еще зависит от 
    запускаемой программы, то т.к. я вычислял факториал, приходилось хранить большие числа.
    В Python крайне опрометчиво что-то вычислять рекурсией: в других ЯП вы бы получили цикл вместо рекурсии (хвостовая 
    оптимизация). В Python ее нет. По историческим причинам и личной неприязни Гвидо к рекурсии.
    Мое предпочтение в данной задаче - это math.factorial(), меньше затрат памяти, меньше кода и быстрее выполнение.
"""


#
# ----------------------------------------- 3) Квадратная матрица -----------------------------------------------------
#


@timer
@profile
def matrix():  # Собственными средствами Python
    n = 1000
    el = 0
    mas = []
    for i in range(n):
        mas.append([])
        for j in range(n):
            mas[i].append(el)
            el += 1
    print(mas)
    del mas


@timer
@profile
def numpy_matrix():  # С подключением библиотеки Numpy
    mas = np.arange(1000000).reshape(1000, 1000)
    print(mas)
    del mas


matrix()
numpy_matrix()

"""
Результат выполнения:

Функция matrix():
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   188     26.8 MiB     26.8 MiB           1   @timer
   189                                         @profile
   190                                         def matrix():
   191     26.8 MiB      0.0 MiB           1       n = 1000
   192     26.8 MiB      0.0 MiB           1       el = 0
   193     26.8 MiB      0.0 MiB           1       mas = []
   194     53.7 MiB     -0.3 MiB        1001       for i in range(n):
   195     53.7 MiB     -0.2 MiB        1000           mas.append([])
   196     53.7 MiB   -235.0 MiB     1001000           for j in range(n):
   197     53.7 MiB   -225.9 MiB     1000000               mas[i].append(el)
   198     53.7 MiB   -239.2 MiB     1000000               el += 1
   199     54.2 MiB      0.5 MiB           1       print(mas)
   200     28.7 MiB    -25.5 MiB           1       del mas

Время выполнения функции: 136.3083

Функция numpy_matrix():
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   203     28.5 MiB     28.5 MiB           1   @timer
   204                                         @profile
   205                                         def numpy_matrix():
   206     32.3 MiB      3.8 MiB           1       mas = np.arange(1000000).reshape(1000, 1000)
   207     32.4 MiB      0.1 MiB           1       print(mas)
   208     28.6 MiB     -3.8 MiB           1       del mas

Время выполнения функции: 0.0076

ВЫВОД:
    При создании квадратной матрицы собственными средствами Python резко возрастает объем памяти, необходимый для 
    вычислений и создания массива с 26.8 MiB до 54.2 MiB, т.е. в 2 раза. Используя библиотеку Numpy мы уходим от 
    этих показателей: с 28.5 MiB до 32.4 MiB. Разница в скорости выполнения: 136.3083 против 0.0076.
    Данные показатели указывают, что если работать с большими данными, то нужно склоняться к выбору Numpy - это
    экономия памяти и лучшая скорость выполнения + читаемый код.
"""


#
# ----------------------------------------- 4) Метод класса __slots__  ------------------------------------------------
#

class DataItem1:
    __slots__ = ['name', 'age', 'address']

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f'{self.name}, {self.age}, {self.address}'


class DataItem2:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f'{self.name}, {self.age}, {self.address}'


@timer
@profile
def f(n):
    data = []
    for p in range(n):
        data.append(DataItem1("Maxim", 42, "middle of nowhere"))
    print('Эта программа отработала с методом __slots__')
    del data


@timer
@profile
def f_2(n):
    data = []
    for p in range(n):
        data.append(DataItem2("Maxim", 42, "middle of nowhere"))
    print('Эта программа отработала без метода __slots__')
    del data


number = 100000
f(number)
f_2(number)

"""
Результат выполнения:

Эта программа отработала с методом __slots__
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     15.7 MiB     15.7 MiB           1   @timer
    43                                         @profile
    44                                         def f(n):
    45     15.7 MiB      0.0 MiB           1       data = []
    46     19.5 MiB   -657.1 MiB      100001       for p in range(n):
    47     19.5 MiB   -653.3 MiB      100000           data.append(DataItem1("Maxim", 42, "middle of nowhere"))
    48     19.5 MiB      0.0 MiB           1       print('Эта программа отработала с методом __slots__')
    49     16.2 MiB     -3.3 MiB           1       del data

Время выполнения функции: 9.8613

Эта программа отработала без метода __slots__
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    52     16.2 MiB     16.2 MiB           1   @timer
    53                                         @profile
    54                                         def f_2(n):
    55     16.2 MiB      0.0 MiB           1       data = []
    56     24.9 MiB      0.0 MiB      100001       for p in range(n):
    57     24.9 MiB      8.7 MiB      100000           data.append(DataItem2("Maxim", 42, "middle of nowhere"))
    58     24.9 MiB      0.0 MiB           1       print('Эта программа отработала без метода __slots__')
    59     16.1 MiB     -8.7 MiB           1       del data

Время выполнения функции: 9.8336

ВЫВОД:
    Если мы работаем с классами и не хотим, чтобы были изменения класса извне, то предпочтительно использовать метод 
    класса __slot__. 
    По результатам видно, что используя __slot__ объем используемой памяти возрастает от 15.7 до 19.5 MiB - 24 %. 
    Без __slot__ объем памяти возрастает от 16.2 до 24.9 MiB - 53 %. 
"""
