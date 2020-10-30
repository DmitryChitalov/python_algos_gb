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

# Дмитрий, хотела сама написать сортировку, но что-то тут не то...
# Посмотрите, пжл, в чем ошибка?
'''
def merge_sort(lst_obj):
    if len(lst_obj) <= 1:
        return lst_obj
    mid = len(lst_obj) // 2
    left_half = lst_obj[:mid]
    right_half = lst_obj[mid:]
    print(left_half, right_half)
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return list(merge(left_half, right_half))


def merge(left_half, right_half):
    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
        if len(left_half) == 0:
            res += right_half
        else:
            res += left_half
    return res
'''

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


orig_list = [50*random() for i in range(5)]
print(orig_list)
print('sorted list', merge_sort(orig_list))

print(timeit('merge_sort(orig_list)', setup='from __main__ import merge_sort, orig_list')) # замер - 8.1427