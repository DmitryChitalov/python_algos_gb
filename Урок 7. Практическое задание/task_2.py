"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import numpy

import timeit
import random


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
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
        return lst_obj

orig_list = 50*numpy.random.rand(10)
print(orig_list)
# замеры 10
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1))
print(orig_list)
print(merge_sort(orig_list))

orig_list = 50*numpy.random.rand(100)

# замеры 100
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1))
print(orig_list)
print(merge_sort(orig_list))


orig_list = 50*numpy.random.rand(1000)


# замеры 1000
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1))
print(orig_list)
print(merge_sort(orig_list))

