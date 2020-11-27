"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
from timeit import timeit


number = int(input('Введите количество элементов: '))
usual_list = [random.random() * 50 for i in range(number)]
usual_copy = usual_list.copy()


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


sorted_list = merge_sort(usual_copy)
print(f'Исходный массив: {usual_list}')
print(f'Отсортированный массив: {sorted_list}')
print(timeit('merge_sort(usual_copy)',
             setup='from __main__ import merge_sort, usual_copy', number=1))


print(timeit('merge_sort(usual_copy)',
             setup='from __main__ import merge_sort, usual_copy', number=100))
# 0.0009753999999997376
print(timeit('merge_sort(usual_copy)',
             setup='from __main__ import merge_sort, usual_copy', number=1000))
# 0.008936999999999973


"""Введите количество элементов: 5
Исходный массив: [44.43552836797787, 35.552446934110975, 31.453734358804596, 10.814480220783928, 9.843503837357066]
Отсортированный массив: [9.843503837357066, 10.814480220783928, 31.453734358804596, 35.552446934110975, 44.43552836797787]
1.540000000055386e-05"""


""" C увеличением количества итераций, увеличивается равномерно и время . Если же в программе вбить значения больше 5
происходит разбиение цифр на 5-рки сортированных значений"""
