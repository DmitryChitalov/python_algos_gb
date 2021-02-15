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


def get_uint(msg='', err=''):
    while True:
        res = input(('Enter Unsigned Int number: ', msg)[bool(msg)])
        if res != '':
            try:
                res = int(res)
            except ValueError:
                pass
            else:
                return res
        print(('This is not UInt, try again, please!', err)[bool(err)])


def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_list[k] = left[i]
                i += 1
            else:
                unsorted_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            unsorted_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            unsorted_list[k] = right[j]
            j += 1
            k += 1
        return unsorted_list


origin_list = [random() * 50 for el in range(get_uint())]
print(f'Исходный - {origin_list}')
print(f'Отсортированный - {merge_sort(origin_list)}')
