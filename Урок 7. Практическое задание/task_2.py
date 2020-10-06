"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from timeit import timeit
import random

n = int(input('Введите количество элементов: '))
my_list = [random.random() * 50 for _ in range(n)]
print(f'Исходный массив: {my_list}')


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


my_list_sort = merge_sort(my_list)
print(f'Отсортированный массив: {my_list_sort}')
print(timeit('merge_sort(my_list)', setup='from __main__ import merge_sort, my_list', number=1))
# замер времени 3.2099999999868345e-05
print(timeit('merge_sort(my_list.copy())', setup='from __main__ import merge_sort, my_list', number=100))
# замер времени 0.0012554000000002397
print(timeit('merge_sort(my_list.copy())', setup='from __main__ import merge_sort, my_list', number=1000))
# замер времени 0.014161400000000324
print(timeit('merge_sort(my_list.copy())', setup='from __main__ import merge_sort, my_list', number=10000))
# замер времени 0.06151060000000008
