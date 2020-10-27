"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import random
from timeit import timeit


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


n = int(input('Введите число элементов массива: '))
lst = [random() * 50 for i in range(n)]
print('Исходный список:    ', lst)
print('Сортировка слиянием:', merge_sort(lst[:]))
print('Время выполнения:   ', timeit('merge_sort(lst[:])', 'from __main__ import merge_sort, lst', number=10000))
print('Встроенный алгоритм:', sorted(lst[:]))
print('Время выполнения:   ', timeit('sorted(lst[:])', 'from __main__ import lst', number=10000))

"""
Алгоритм сортировки слиянием честно утащен из методички.
Против встроенного алгоритма ловить нечего - разница в 2 порядка.
"""
