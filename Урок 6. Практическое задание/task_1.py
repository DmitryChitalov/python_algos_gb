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

from timeit import default_timer
from random import randint
import memory_profiler as mem_profile


def memorize(func):
    def my_func(*args, **kwargs):
        m1 = mem_profile.memory_usage()
        start = default_timer()
        res = func(*args, **kwargs)
        stop = default_timer()
        m2 = mem_profile.memory_usage()
        mem_res = m2[0] - m1[0]
        time_res = stop - start
        print(f"{func.__name__}: {time_res} s, {mem_res} MB")
        return res

    return my_func


@memorize
def sum_list(l):
    g = 0
    for i in l:
        g += int(i)
    return g


@memorize
def sum_c(l):
    return sum(l)


my_list = [randint(10, 100) for i in range(99999999)]

print(sum_list(my_list))
print(sum_c(my_list))
print("Потребление МЕМ крайне низкое в обоих вариантах, но быстрее 2 вариант, т.к. нет перебора через цикл")


@memorize
def append_in_list():
    my_list = []
    for i in range(99999999):
        my_list.append(i)
    return my_list


@memorize
def append_in_list2():
    return [i for i in range(99999999)]


append_in_list()
append_in_list2()
print(
    "Потребление МЕМ высокое в обоих вариантах из-за перебора огромного количества данных. Время работы быстрее во втором, т.к нет перебора через цикл")
