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

from memory_profiler import memory_usage, profile
import time
import random
import math

my_list = [random.randint(0, 100) for el in range(0, 10000)]
print(my_list)


def my_decorator(function):
    def wrapper(*args, **kwargs):
        t_1 = time.process_time()
        m_1 = memory_usage()
        function(*args, **kwargs)
        t_2 = time.process_time()
        m_2 = memory_usage()
        process_time = t_2 - t_1
        process_memory = m_2[0] - m_1[0]
        return f'Время выполнения: {process_time}, память: {process_memory}'

    return wrapper


# нахождение минимального значения в списке


@my_decorator
def func_1(lst):
    min_value = lst[0]
    for el in range(1, len(lst)):
        if lst[el] < min_value:
            min_value = lst[el]
    return min_value


@my_decorator
def func_2(lst):
    flag = lst[0]
    for el in range(len(lst) - 1):
        for elem in range(len(lst)):
            if lst[el] < flag:
                flag = lst[el]
    return flag


print(func_1(my_list))
print(func_2(my_list))
# Время выполнения: 0.0, память: 0.0  func_1
# Время выполнения: 5.75, память: 0.0  func_2
# результаты в очередной раз подтверждают, что использоание циклов O(n^2) не самая лучшая идея
######################################################################################################################


@my_decorator
def fact_1(n):
    factorial = 1
    for el in range(2, n + 1):
        factorial *= el
    return factorial


@my_decorator
def fact_2(n):
    factorial = 1
    for el in range(1, n+1):
        factorial *= el
        yield factorial


@my_decorator
def fact_3(n):
    if n == 0:
        return 1
    return fact_2(n-1) * n


@my_decorator
def fact_4(n):
    math.factorial(n)


print(fact_1(10000))   # Время выполнения: 0.046875  память: 0.1171875    через цикл
print(fact_2(10000))   # Время выполнения: 0.0       память: 0.00390625   через генератор
print(fact_3(10000))   # Время выполнения: 0.0       память: 0.01953125   через рекурсию
print(fact_4(10000))   # Время выполнения: 0.03125   память: 0.046875     через встроенную функцию
# из результатов видно, что самое затратное решение и по времени, и по памяти- через цикл. Меняя входящее
# значение функций, я заметил, что в генераторе показатели памяти меняются не значительно. Поэтому, если результаты
# функции дальше нигде не надо использовать, то предпочтение за генератором.


@profile()
def func_test():
    my_list_1 = [random.randrange(0, 100) for _ in range(10000)]
    new_list = [my_list_1[el] for el in range(len(my_list_1)) if my_list_1[el] > my_list_1[el - 1]]
    return new_list


print(func_test())
"""
Line #    Mem usage    Increment   Line Contents
================================================
107     13.5 MiB     13.5 MiB   @profile()
108                             def func_test():
109     13.6 MiB     0.0 MiB       my_list_1 = [random.randrange(0, 100) for _ in range(10000)]
110     13.6 MiB     0.0 MiB       new_list = [my_list_1[el] for el in range(len(my_list_1)) 
                                                if my_list_1[el] > my_list_1[el - 1]]
111     13.6 MiB     0.0 MiB       return new_list
"""
#  из результатов видно, что проблемных мест нет, да и объем задачи не велик, чтобы их найти
