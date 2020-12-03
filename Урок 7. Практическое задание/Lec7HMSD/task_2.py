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
import timeit


def func_sort(list_for_sort):
    if len(list_for_sort) > 1:
        center = len(list_for_sort) // 2
        left = list_for_sort[:center]
        right = list_for_sort[center:]

        func_sort(left)
        func_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_for_sort[k] = left[i]
                i += 1
            else:
                list_for_sort[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list_for_sort[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list_for_sort[k] = right[j]
            j += 1
            k += 1
        return list_for_sort


ls = [random.uniform(0, 50) for _ in range(10)]
print("Исходный массив", ls)
print("Отсортированный массив", func_sort(ls))

ls = [random.uniform(0, 50) for _ in range(10)]
print(timeit.timeit("func_sort(ls[:])", \
                    setup="from __main__ import func_sort, ls", number=100))

ls = [random.uniform(0, 50) for _ in range(100)]
print(timeit.timeit("func_sort(ls[:])", \
                    setup="from __main__ import func_sort, ls", number=100))

ls = [random.uniform(0, 50) for _ in range(1000)]
print(timeit.timeit("func_sort(ls[:])", \
                    setup="from __main__ import func_sort, ls", number=100))

