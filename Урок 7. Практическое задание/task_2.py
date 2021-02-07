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

def merge_sort(lst_obj):
    if len(lst_obj) < 2:
        return lst_obj[:]
    else:
        middle = int(len(lst_obj) / 2)
        left = merge_sort(lst_obj[:middle])
        right = merge_sort(lst_obj[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


len_lst = int(input('Введите число элементов: '))
orig_lst = [random.uniform(0, 50) for _ in range(len_lst)]

print('Исходный массив: ', orig_lst)
print('Отсортированный массив: ', merge_sort(orig_lst))
print('Замер merge_sort: ',
      timeit.timeit("merge_sort(orig_lst[:])", globals=globals(), number=1000))

"""
Результаты замеров:
Замер merge_sort (10):   0.022898300000000038
Замер merge_sort (100):  0.3540904

"""