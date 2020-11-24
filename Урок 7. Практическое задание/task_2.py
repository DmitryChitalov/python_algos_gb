"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import timeit
import random
from memory_profiler import profile


def merge_sort(lst_obj):
    orig_list_copy = lst_obj[:]
    if len(lst_obj) < 1:
        return 'Количество элементов не может быть меньше 1'
    if len(lst_obj) == 1:
        return f'Исходный массив:        {orig_list_copy}\nOтсортированный массив: {lst_obj}'
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return f'Исходный массив:        {orig_list_copy}\nOтсортированный массив: {lst_obj}'


number = int(input('Введите количество элементов: '))
orig_list = [random.random() * 50 for _ in range(number)]
print(merge_sort(orig_list))

print('\nВремя работы функции 10, 100 и 1000 повторов:\n')
# замеры 10
print(timeit.timeit("merge_sort(orig_list[:])",
                    setup="from __main__ import merge_sort, orig_list", number=10))

# замеры 100
print(timeit.timeit("merge_sort(orig_list[:])",
                    setup="from __main__ import merge_sort, orig_list", number=100))

# замеры 1000
print(timeit.timeit("merge_sort(orig_list[:])",
                    setup="from __main__ import merge_sort, orig_list", number=1000))

"""Добавил в функцию проверку, если введено число 0 или 1
При проведении замеров, передав функции полностью отсортированный массив - получил такое же время работы, как и 
на рандомном списке.
Так же замерил память, добавил описание внизу:

Замерив использование памяти данным алгоритмом - также больших инкрементов не увидел (вводил 5000 и 10000 элементов)
Но при большем количестве - памяти понадобится больше, т.к. функция merge_sort() возвращает новый список, 
а не сортирует существующий. И такая сортировка требует больше памяти для создания нового списка того же размера, 
что и входной список.

Введите количество элементов: 5000


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19     19.6 MiB     19.6 MiB           1   @profile
    20                                         def wrap(n):
    21     20.2 MiB     -2.6 MiB       10000       def merge_sort(lst_obj):
    22     20.2 MiB     -2.5 MiB        9999           orig_list_copy = lst_obj[:]
    23     20.2 MiB     -2.5 MiB        9999           if len(lst_obj) < 1:
    24                                                     return 'Количество элементов не может быть меньше 1'
    25     20.2 MiB     -2.5 MiB        9999           if len(lst_obj) == 1:
    26     20.2 MiB     -1.2 MiB        5000               return f'Исходный массив:{orig_list_copy}\nOтсортированный массив: {lst_obj}'
    27     20.2 MiB     -1.3 MiB        4999           if len(lst_obj) > 1:
    28     20.2 MiB     -1.3 MiB        4999               center = len(lst_obj) // 2
    29     20.2 MiB     -1.3 MiB        4999               left = lst_obj[:center]
    30     20.2 MiB     -1.2 MiB        4999               right = lst_obj[center:]
    31     20.2 MiB   -191.5 MiB        4999               merge_sort(left)
    32     20.2 MiB   -275.4 MiB        4999               merge_sort(right)
    33     20.2 MiB    -95.7 MiB        4999               i, j, k = 0, 0, 0
    34     20.2 MiB  -1154.7 MiB       60269               while i < len(left) and j < len(right):
    35     20.2 MiB  -1059.0 MiB       55270                   if left[i] < right[j]:
    36     20.2 MiB   -516.1 MiB       27065                       lst_obj[k] = left[i]
    37     20.2 MiB   -516.1 MiB       27065                       i += 1
    38                                                         else:
    39     20.2 MiB   -542.9 MiB       28205                       lst_obj[k] = right[j]
    40     20.2 MiB   -542.9 MiB       28205                       j += 1
    41     20.2 MiB  -1059.0 MiB       55270                   k += 1
    42                                         
    43     20.2 MiB    -98.8 MiB        7738               while i < len(left):
    44     20.2 MiB    -53.2 MiB        2739                   lst_obj[k] = left[i]
    45     20.2 MiB     -3.1 MiB        2739                   i += 1
    46     20.2 MiB     -3.1 MiB        2739                   k += 1
    47                                         
    48     20.2 MiB   -164.2 MiB        8798               while j < len(right):
    49     20.2 MiB    -68.5 MiB        3799                   lst_obj[k] = right[j]
    50     20.2 MiB    -68.5 MiB        3799                   j += 1
    51     20.2 MiB    -68.5 MiB        3799                   k += 1
    52     20.9 MiB    -94.0 MiB        4999               return f'Исходный массив:{orig_list_copy}\nOтсортированный массив: {lst_obj}'
    53     20.9 MiB      0.0 MiB           1       return merge_sort(n)"""
