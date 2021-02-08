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
import copy
from timeit import timeit

user_prompt = int(input('Введите число элементов: '))
my_list = [uniform(0, 50) for i in range(user_prompt)]
my_list_copy = copy.deepcopy(my_list)


def merge_sort(list_obj):
    length = len(list_obj)

    if length < 2:
        return list_obj

    left_part = merge_sort(list_obj[:length // 2])
    right_part = merge_sort(list_obj[length // 2:length])

    i, j = 0, 0
    res = []

    while i < len(left_part) or j < len(right_part):
        if not i < len(left_part):
            res.append(right_part[j])
            j += 1
        elif not j < len(right_part):
            res.append(left_part[i])
            i += 1
        elif left_part[i] < right_part[j]:
            res.append(left_part[i])
            i += 1
        else:
            res.append(right_part[j])
            j += 1

    return res


print(f'Original list — {my_list}')
print(f'Sorted list — {merge_sort(my_list_copy)}')
print(timeit('merge_sort(my_list_copy)',
             globals=globals(),
             number=100))

"""
    Замаеры времени выполнения алгоритма:
    10 элеметов     — 0.0018337
    100 элеметов    — 0.0251086
    1000 элеметов   — 0.3465036
    10000 элеметов  — 4.5387098
"""
