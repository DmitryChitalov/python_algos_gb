"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import uniform
from timeit import timeit


lst_1 = [uniform(0, 50) for _ in range(10)]


def lst_maker():
    x = int(input('Введите число элементов: '))
    lst__make = [uniform(0, 50) for _ in range(x)]
    print(lst__make)
    return merge_sort(lst__make)


def merge_sort(lst):
    if len(lst) > 1:
        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        return lst


# Небольшое сравнение с гномьей сортировкой
# -------------------------------------------------------------------------


def gnome_sort(lst):
    n = 0
    while n < len(lst):
        if n == 0:
            n = n + 1
        if lst[n] >= lst[n - 1]:
            n = n + 1
        else:
            lst[n], lst[n - 1] = lst[n - 1], lst[n]
            n = n - 1
    return lst


print(lst_1)
print(timeit("merge_sort(lst_1[:])", setup="from __main__ import merge_sort, lst_1", number=1000),
      merge_sort(lst_1[:]))
print(timeit("gnome_sort(lst_1[:])", setup="from __main__ import gnome_sort, lst_1", number=1000),
      gnome_sort(lst_1[:]))

# ---------------------------------------------------
# Исходный массив
# [41.79860993588793, 15.282433842235637, 31.173780363449893, 30.62561768127006, 40.96372196664239,
# 41.55206474252894, 25.627363006609134, 43.33327053123635, 43.13854113193483, 27.476503979654304]

# 0.02450451399999999
#
# [15.282433842235637, 25.627363006609134, 27.476503979654304, 30.62561768127006,
# 31.173780363449893, 40.96372196664239, 41.55206474252894, 41.79860993588793, 43.13854113193483, 43.33327053123635]

# 0.015410879000000016

# [15.282433842235637, 25.627363006609134, 27.476503979654304, 30.62561768127006,
# 31.173780363449893, 40.96372196664239, 41.55206474252894, 41.79860993588793, 43.13854113193483, 43.33327053123635]

# При нескольких сравнениях гномья сортировка выигрывает во времени
