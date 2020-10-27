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


def my_decorator(function):
    def wrapper(*args, **kwargs):
        t_1 = time.process_time()
        m_1 = memory_usage()
        function(*args, **kwargs)
        t_2 = time.process_time()
        m_2 = memory_usage()
        process_time = t_2 - t_1
        process_memory = m_2[0] - m_1[0]
        return f'Время выполнения {function.__name__}: {process_time}, память: {process_memory}'

    return wrapper


@my_decorator
def func_1(lst):
    """Находит минимальное значения в списке."""
    min_value = lst[0]
    for el in range(1, len(lst)):
        if lst[el] < min_value:
            min_value = lst[el]
    return min_value


@my_decorator
def func_2(lst):
    """Находит минимальное значения в списке."""
    flag = lst[0]
    for el in range(len(lst) - 1):
        for elem in range(len(lst)):
            if lst[el] < flag:
                flag = lst[el]
    return flag


@my_decorator
def fact_1(n):
    """Находит факториал числа через цикл."""
    factorial = 1
    for el in range(2, n + 1):
        factorial *= el
    return factorial


@my_decorator
def fact_2(n):
    """Находит факториал числа через генератор."""
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial


@my_decorator
def fact_3(n):
    """Находит факториал числа через рекурсию."""
    if n == 0:
        return 1
    return fact_2(n - 1) * n


@my_decorator
def fact_4(n):
    """Находит факториал числа через встроенные функции."""
    math.factorial(n)


@my_decorator
def func_test(lst):
    """Добавляет 1000 к числам в списке."""
    new_list = [lst[el] + 1000 for el in range(len(lst))]
    return new_list


@profile()
def full_program():
    my_list = [random.randint(0, 100) for el in range(0, 100)]
    print(func_1(my_list))
    print(func_2(my_list))
    # func_2 выполняется медленнее func_1 в связи с более высокой сложностью алгоритма.
    print(fact_1(10000))
    print(fact_2(10000))
    print(fact_3(10000))
    print(fact_4(10000))
    # В порядке убывания быстродействия: генератор, рекурсия, встроенные функции, цикл.
    print(func_test(my_list))
    # func_test()


#  из результатов @profile видно, то проблем с памятью нет.


if __name__ == '__main__':
    """Python 3.8, x64"""
    full_program()
