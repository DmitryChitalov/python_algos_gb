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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj) - 1:
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


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


inp_lst = [uniform(0, 50) for _ in range(5)]
print(f'{inp_lst}\n')
print(f'{bubble_sort(inp_lst.copy())}\n')
print(f'{merge_sort(inp_lst.copy())}\n')

print(timeit('bubble_sort(inp_lst.copy())',
             setup='from __main__ import bubble_sort, inp_lst',
             number=10000))
print(timeit('merge_sort(inp_lst.copy())',
             setup='from __main__ import merge_sort, inp_lst',
             number=10000))
# Вывод: с уыеличением размера списка метод "слияние" показывает себя
# как более быстродейственный отно сительно метода "пузырек".
