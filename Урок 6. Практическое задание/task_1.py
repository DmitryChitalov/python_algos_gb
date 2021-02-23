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
from memory_profiler import memory_usage


def mem_time_count(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        start = default_timer()
        res = func(*args, **kwargs)
        stop = default_timer()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        time_diff = stop - start
        print(f"{func.__name__}: {time_diff} секунд, {mem_diff} MiB")
        return res

    return wrapper


# суммирование элементов списка
@mem_time_count
def summ_for_list(l):
    g = 0
    for i in l:
        g += int(i)
    return g


@mem_time_count
def sum_counter(l):
    return sum(l)


user_list = [randint(10, 500) for x in range(10000000)]

print(summ_for_list(user_list))
print(sum_counter(user_list))

"""
OS - Windows 10x64
python 3.9

Потребление памяти минимально в обоих случаях.
Но вот время работы лучше во втором т.к. используем встроенные функции без перебора каждого элемента через цикл

summ_for_list: 1.0553133999999993 секунд, 0.00390625 MiB
2549688664
sum_counter: 0.1081821000000005 секунд, 0.00390625 MiB
2549688664
"""


# Добавление данных в список
@mem_time_count
def append_in_list():
    user_list = []
    for i in range(1000000):
        user_list.append(i)
    return user_list


@mem_time_count
def append_in_list2():
    return [x for x in range(1000000)]


append_in_list()
append_in_list2()

"""
Потребление памяти минимально в обоих случаях.
Но вот время работы лучше во втором
append_in_list: 0.11519889999999933 секунд, 38.34765625 MiB
append_in_list2: 0.08049130000000027 секунд, 38.6484375 MiB
"""
