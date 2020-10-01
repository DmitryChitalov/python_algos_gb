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

import random as rd
from timeit import timeit
import cProfile

from memory_profiler import profile

"""
Ниже представлены функции, вычисляющие сумму чисел от 1 до MAX_COUNT.
"""

MAX_COUNT = 1000

# @profile
def get_sum_1(count):
    new_list = list(range(count + 1))
    result = sum(new_list)
    return result


# @profile
def get_sum_2(count):
    result = 0
    new_list = (numb for numb in range(count + 1))
    for numb in new_list:
        result += numb
    return result


# @profile
def get_sum_3(count):
    new_list = [1 for y in range(count + 1) for i in range(y)]
    result = len(new_list)
    return result


def main(count):
    get_sum_1(count)
    get_sum_2(count)
    get_sum_3(count)


# cProfile.run('get_sum_1(1000)')
# cProfile.run('get_sum_2(1000)')
# cProfile.run('get_sum_3(1000)')

# result_1 = timeit("get_sum_1(MAX_COUNT)", "from __main__ import get_sum_1, MAX_COUNT", number=100)
# result_2 = timeit("get_sum_2(MAX_COUNT)", "from __main__ import get_sum_2, MAX_COUNT", number=100)
# result_3 = timeit("get_sum_3(MAX_COUNT)", "from __main__ import get_sum_3, MAX_COUNT", number=100)

# print(f'Результат выполнения get_sum_1: {result_1} сек.')
# print(f'Результат выполнения get_sum_2: {result_2} сек.')
# print(f'Результат выполнения get_sum_3: {result_3} сек.')

# main(MAX_COUNT)

# Python 3.8.5 64-bit macOS Catalina 10.15.7

"""
Результаты выполнения программа по времени (в секундах) при 100 запусках.
    Результат выполнения get_sum_1: 0.001937734999999996 -> Занимает меньше всего времени при выполнении,
        т.к. использует встроенные функции.
    Результат выполнения get_sum_2: 0.007393080999999996 -> Позволяет выиграть время по сравнению с формированием
        обычного списка, т.к. используется генератор.
    Результат выполнения get_sum_3: 1.36946993 -> Сильно отличается по времени выполнения в худшую сторону,
        т.к. используется заполнение списка количеством элементов, равным значению ожидаемого результата.
"""

"""
Результаты измерения использования памяти через memory_profiler.

    Функция get_sum_1():
        Line #    Mem usage    Increment   Line Contents
        ================================================
            27     10.8 MiB     10.8 MiB   @profile
            28                             def get_sum_1(count):
            29     10.8 MiB      0.0 MiB       new_list = list(range(count + 1))
            30     10.8 MiB      0.0 MiB       result = sum(new_list)
            31     10.8 MiB      0.0 MiB       return result

    Функция get_sum_2():
        Line #    Mem usage    Increment   Line Contents
        ================================================
            34     10.8 MiB     10.8 MiB   @profile
            35                             def get_sum_2(count):
            36     10.8 MiB      0.0 MiB       result = 0
            37     10.8 MiB      0.0 MiB       new_list = (numb for numb in range(count + 1))
            38     10.8 MiB      0.0 MiB       for numb in new_list:
            39     10.8 MiB      0.0 MiB           result += numb
            40     10.8 MiB      0.0 MiB       return result

    Функция get_sum_3():
        Line #    Mem usage    Increment   Line Contents
        ================================================
            43     10.8 MiB     10.8 MiB   @profile
            44                             def get_sum_3(count):
            45     15.4 MiB      0.7 MiB       new_list = [1 for y in range(count + 1) for i in range(y)]
            46     15.4 MiB      0.0 MiB       result = len(new_list)
            47     15.4 MiB      0.0 MiB       return result

### Вывод: занимаемую память можно заметить только в 3-м примере, т.к. функция формирует достаточно большой список,
        где количество элементов служит результатом выполнения функции.
"""

"""
Результаты измерения через cProfile.
    5 function calls in 0.000 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1.py:29(get_sum_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


            1006 function calls in 0.000 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_1.py:36(get_sum_2)
        1002 0.000    0.000    0.000    0.000 task_1.py:38(<genexpr>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


            6 function calls in 0.014 seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.014    0.014 <string>:1(<module>)
        1    0.000    0.000    0.013    0.013 task_1.py:45(get_sum_3)
        1    0.013    0.013    0.013    0.013 task_1.py:46(<listcomp>)
        1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

### Вывод: в 3-м примере формирование списка занимает значительно больше времени, чем в 1 и 2 функциях.
"""
