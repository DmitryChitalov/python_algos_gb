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


def merge_sort(lst_obj):
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
        return lst_obj


n = int(input('Введите число элементов: '))
arr = [uniform(0, 50) for _ in range(n)]
print(f'Исходный - {arr}')
print(f'Отсортированный - {merge_sort(arr[:])}')

print(timeit('merge_sort(arr[:])', setup='from __main__ import merge_sort, arr', number=100))
print(timeit('merge_sort(arr[:])', setup='from __main__ import merge_sort, arr', number=1000))
print(timeit('merge_sort(arr[:])', setup='from __main__ import merge_sort, arr', number=10000))


"""Для n = 5
Исходный - [17.79620562887739, 45.91407949557348, 38.1805806194386, 18.712259171774626, 0.008461957216654437]
Отсортированный - [0.008461957216654437, 17.79620562887739, 18.712259171774626, 38.1805806194386, 45.91407949557348]
0.0010833000000003423
Замеры:
0.0010833000000003423
0.006677300000000219
0.07552000000000003"""

"""Для n = 100 замеры:
0.029064800000000002
0.2552851999999999
2.3859361000000003"""