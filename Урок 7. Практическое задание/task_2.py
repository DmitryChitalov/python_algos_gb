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


def merge_sort_copy(lst):
    lst_copy = lst.copy()
    return merge_sort(lst_copy)


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


if __name__ == '__main__':
    n = int(input('Введите число элементов: '))
    orig_list = [random.random() * 50 for _ in range(n)]
    print(f'Исходный масив:        {orig_list}')
    print(f'Отсортированный масив: {merge_sort_copy(orig_list)}')

    print(f'Время сортировки функции merge_sort_copy:    ', end='')
    print(
        timeit(
            "merge_sort_copy(orig_list[:])",
            setup='from __main__ import merge_sort_copy, orig_list',
            number=100000))

'''
Введите число элементов: 5
Исходный масив:        [18.678654203253124, 47.40156351711796, 21.927122989273716, 11.604503574670389, 6.678750547902573]
Отсортированный масив: [6.678750547902573, 11.604503574670389, 18.678654203253124, 21.927122989273716, 47.40156351711796]
Время сортировки функции merge_sort_copy:    1.1270969000000002


'''