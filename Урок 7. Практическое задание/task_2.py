"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

"""Сортировка слиянием"""

import random
import copy
import timeit

orig_list = [random.uniform(0, 50) for _ in range(int(input('Введите число элементов: ')))]
copy_orig_list = copy.copy(orig_list)


#учебный метод
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

print(f'Исходный - {orig_list}')
print(f'Отсортированный - {merge_sort(orig_list)}')
print('Время 1 метода:')
print(timeit.timeit("merge_sort(orig_list)", setup = "from __main__ import merge_sort, orig_list", number = 100))

#мой метод
def my_merge_sort(lst_obj):
    n = len(lst_obj)
    if n < 2:
        return lst_obj

    left = my_merge_sort(lst_obj[:n//2])
    right = my_merge_sort(lst_obj[n//2:n])

    i = j = 0
    res = []
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res

print(f'Исходный - {copy_orig_list}')
print(f'Отсортированный - {my_merge_sort(copy_orig_list)}')
print('Время 2 метода:')
print(timeit.timeit("my_merge_sort(copy_orig_list)", setup = "from __main__ import my_merge_sort,copy_orig_list", number = 100))

"""
Результаты:
Введите число элементов: 4
Исходный - [12.81815498944815, 45.490905996141315, 40.64568709530248, 31.8979216700943]
Отсортированный - [12.81815498944815, 31.8979216700943, 40.64568709530248, 45.490905996141315]
Время 1 метода:
0.0009538140002405271
Исходный - [12.81815498944815, 45.490905996141315, 40.64568709530248, 31.8979216700943]
Отсортированный - [12.81815498944815, 31.8979216700943, 40.64568709530248, 45.490905996141315]
Время 2 метода:
0.0010103960012202151

Время получилось примерно одинаковым.
"""