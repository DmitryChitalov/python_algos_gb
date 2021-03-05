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

import timeit
import random


def merge(left_list, right_list):
    sorted_list = []
    left_index = 0
    right_index = 0

    for _ in range(len(left_list) + len(right_list)):
        if left_index < len(left_list) and right_index < len(right_list):
            # Если первый элемент левого подсписка меньше, добавляем его в отсортированный массив
            if left_list[left_index] <= right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его в отсортированный массив
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1

        # Если достигнут конец левого списка, элементы правого списка добавляем в конец результирующего списка
        elif left_index == len(left_list):
            sorted_list.append(right_list[right_index])
            right_index += 1
        # Если достигнут конец правого списка, элементы левого списка добавляем в отсортированный массив
        elif right_index == len(right_list):
            sorted_list.append(left_list[left_index])
            left_index += 1

    return sorted_list


def merge_sort(lst_obj):
    if len(lst_obj) < 2:
        return lst_obj
    center = len(lst_obj) // 2
    left = merge_sort(lst_obj[:center])
    right = merge_sort(lst_obj[center:])

    return merge(left, right)


orig_list = [round(random.uniform(0, 50), 15) for _ in range(10)]

print('orig_list')
print(orig_list)
print('merge_sort')
print(merge_sort(orig_list[:]))

# замеры 10
print('замеры 10')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 100

orig_list = [round(random.uniform(0, 50), 15) for _ in range(100)]

print('замеры 100')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 1000

orig_list = [round(random.uniform(0, 50), 15) for _ in range(1000)]

print('замеры 1000')
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

'''
orig_list
[9.042498858445269, 38.29379605946098, 34.04892118900389, 36.803582986310815, 17.817948443545955, 40.208220476748735, 17.150481365048186, 18.85421218577552, 25.205695230445503, 11.849015682218427]
merge_sort
[9.042498858445269, 11.849015682218427, 17.150481365048186, 17.817948443545955, 18.85421218577552, 25.205695230445503, 34.04892118900389, 36.803582986310815, 38.29379605946098, 40.208220476748735]
замеры 10
0.0148094
замеры 100
0.2324839
замеры 1000
3.6555594

'''
