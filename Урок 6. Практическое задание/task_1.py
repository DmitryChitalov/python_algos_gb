"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять задачи с курса Основ
или с текущего курса Алгоритмов
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!

from random import randint
from memory_profiler import profile


@profile
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

@profile
def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'

######################################################################################################
@profile
def reverse_str(num):  # через индексы строки
    num = str(num)
    revers_num = num[::-1]
    return revers_num

@profile
def divide_num(num):  # используем целое и остаток от деления
    m = 0
    while num > 0:
        m = m * 10 + num % 10
        num = num // 10
    return m

@profile
def lambda_reverse(num):  # используем lambda
    return num[::-1]
lambda_reverse = lambda num: num[::-1]

num_1000 = randint(10000000, 100000000)

print("------------- recursive_reverse -------------")
recursive_reverse(num_1000)
print("------------- recursive_reverse_mem -------------")
recursive_reverse_mem(num_1000)
print("------------- reverse_str -------------")
reverse_str(num_1000)
print("------------- divide_num -------------")
divide_num(num_1000)
print("------------- lambda_reverse -------------")
lambda_reverse(str(num_1000))


"""
Взяты примеры скриптов из урока 4, задание 2
по расходу памяти они все одинаковы, отдельный вопрос по рекурсивной функции - 
вероятно она требует памяти на каждый цикл итерации
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     25.5 MiB     25.5 MiB           1   @profile
    35                                         def memoize(f):
    36     25.5 MiB      0.0 MiB           1       cache = {}
    37                                         
    38     25.5 MiB      0.0 MiB           1       def decorate(*args):
    39                                         
    40                                                 if args in cache:
    41                                                     return cache[args]
    42                                                 else:
    43                                                     cache[args] = f(*args)
    44                                                     return cache[args]
    45                                         
    46     25.5 MiB      0.0 MiB           1       return decorate
------------- recursive_reverse ------------
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           1   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           1       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32                                             return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           2   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           2       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32     25.5 MiB      0.0 MiB           1       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           3   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           3       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32     25.5 MiB      0.0 MiB           2       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           4   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           4       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32     25.5 MiB      0.0 MiB           3       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           5   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           5       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32     25.5 MiB      0.0 MiB           4       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           6   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           6       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32     25.5 MiB      0.0 MiB           5       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           7   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           7       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32     25.5 MiB      0.0 MiB           6       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           8   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           8       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32     25.5 MiB      0.0 MiB           7       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     25.5 MiB     25.5 MiB           9   @profile
    29                                         def recursive_reverse(number):
    30     25.5 MiB      0.0 MiB           9       if number == 0:
    31     25.5 MiB      0.0 MiB           1           return str(number % 10)
    32     25.5 MiB      0.0 MiB           8       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
------------- recursive_reverse_mem -------------
------------- reverse_str -------------
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    56     25.5 MiB     25.5 MiB           1   @profile
    57                                         def reverse_str(num):  # через индексы строки
    58     25.5 MiB      0.0 MiB           1       num = str(num)
    59     25.5 MiB      0.0 MiB           1       revers_num = num[::-1]
    60     25.5 MiB      0.0 MiB           1       return revers_num
------------- divide_num -------------
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    62     25.5 MiB     25.5 MiB           1   @profile
    63                                         def divide_num(num):  # используем целое и остаток от деления
    64     25.5 MiB      0.0 MiB           1       m = 0
    65     25.5 MiB      0.0 MiB           9       while num > 0:
    66     25.5 MiB      0.0 MiB           8           m = m * 10 + num % 10
    67     25.5 MiB      0.0 MiB           8           num = num // 10
    68     25.5 MiB      0.0 MiB           1       return m
------------- lambda_reverse -------------
Process finished with exit code 0
"""