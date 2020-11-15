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

from memory_profiler import profile
from functools import reduce
from random import randint

@profile
def max_el_in_list1(n):
    my_list = [randint(0, 10000) for _ in range(1, n)]
    max_el = reduce(lambda a, b: a if (a > b) else b, my_list)
    print(f'Максимальный элемент - {max_el}')
    del my_list


max_el_in_list1(100000)

'''
Для выполнения программы выделено 19.1 Мебибайт.
При выполнении генераторного выражения прирост памяти составил - 4.4 Мебибайт
После выполнения функции удаляем сгенерированный список и освобождаем 3.7 Мебибайт
Версия Python - 3.9
ОС - Windows 10, x64

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     19.1 MiB     19.1 MiB           1   @profile
    22                                         def max_el_in_list1(n):
    23     23.5 MiB      4.4 MiB      100002       my_list = [randint(0, 10000) for _ in range(1, n)]
    24     23.5 MiB      0.0 MiB      199997       max_el = reduce(lambda a, b: a if (a > b) else b, my_list)
    25     23.5 MiB      0.0 MiB           1       print(f'Максимальный элемент - {max_el}')
    26     19.6 MiB     -3.9 MiB           1       del my_list
'''

@profile
def max_el_in_list2(n):
    my_list = []
    max_el = 0
    for _ in range(n):
        a = randint(0, 10000)
        my_list.append(a)
        if a > max_el:
            max_el = a
    print(f'Максимальный элемент - {max_el}')
    del my_list


max_el_in_list2(100000)

'''
Результаты получились аналогичными.
В данном случае - основной прирост памяти - это список из случайных значений random.
Если, в целом список, не нужен, то можно обойтись без него. Просто сравнивать каждый раз сгенерированное
число с предыдущим максимальным. Тогда прироста к памяти вообще не будет, но изначально выделенная память
так и останется на уровне 19.0 - 19.6 Мебибайт


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    48     19.5 MiB     19.5 MiB           1   @profile
    49                                         def max_el_in_list2(n):
    50     19.5 MiB      0.0 MiB           1       my_list = []
    51     19.5 MiB      0.0 MiB           1       max_el = 0
    52     23.0 MiB      0.0 MiB      100001       for _ in range(n):
    53     23.0 MiB      0.0 MiB      100000           a = randint(0, 10000)
    54     23.0 MiB      3.5 MiB      100000           my_list.append(a)
    55     23.0 MiB      0.0 MiB      100000           if a > max_el:
    56     20.2 MiB      0.0 MiB           6               max_el = a
    57     23.0 MiB      0.0 MiB           1       print(f'Максимальный элемент - {max_el}')
    58     19.7 MiB     -3.3 MiB           1       del my_list
'''