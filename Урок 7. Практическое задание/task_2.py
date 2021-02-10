"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
"""Сортировка слиянием"""

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


orig_list10 = [random.uniform(0, 50) for _ in range(10)]
orig_list100 = [random.uniform(0, 50) for _ in range(100)]
orig_list1000 = [random.uniform(0, 50) for _ in range(1000)]
# замеры 10
print(
    timeit.timeit(
        "merge_sort(orig_list10[:])",
        globals=globals(),
        number=1000))

# замеры 100
print(
    timeit.timeit(
        "merge_sort(orig_list100[:])",
        globals=globals(),
        number=1000))

# замеры 1000
print(
    timeit.timeit(
        "merge_sort(orig_list1000[:])",
        globals=globals(),
        number=1000))

"""
0.008287700000000002
0.1293001
1.7835413
"""
print(orig_list10)
print(merge_sort(orig_list10))
