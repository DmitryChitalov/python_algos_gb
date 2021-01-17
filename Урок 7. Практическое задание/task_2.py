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
from timeit import timeit

n = int(input("Введите число элементов: "))
arr = [random()*50 for _ in range(n)]

print("Исходный массив: ", arr)

def merge(left: list, right: list):
    i,j = 0 , 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j = j + 1
            if j == len(right):
                result.extend(left[i:])
        else:
            result.append(left[i])
            i = i + 1
            if i == len(left):
                result.extend(right[j:])
    return result


def merge_sort(arr : list):
    if len(arr) == 1:
        return arr
    else:
        middle = len(arr)//2
        left_part = merge_sort(arr[:middle])
        right_part = merge_sort(arr[middle:])
        return merge(left_part,right_part)

print("Отсортированный массив: ", merge_sort(arr))


arr_10 = [random()*50 for _ in range(10)]
arr_100 = [random()*50 for _ in range(100)]
arr_1000 = [random()*50 for _ in range(1000)]
print("10 элементов: ", timeit("merge_sort(arr_10)","from __main__ import arr_10, merge_sort, merge",number=100))
print("100 элементов: ", timeit("merge_sort(arr_100)","from __main__ import arr_100, merge_sort, merge",number=100))
print("1000 элементов: ", timeit("merge_sort(arr_1000)","from __main__ import arr_1000, merge_sort, merge",number=100))

"""Вывод работы программы:
Введите число элементов: 5
Исходный массив:  [19.497989090052037, 43.77655946998179, 21.688223447019343, 7.172632888204622, 10.59084880044846]
Отсортированный массив:  [7.172632888204622, 10.59084880044846, 19.497989090052037, 21.688223447019343, 43.77655946998179]

10 элементов:  0.009429169999999765
100 элементов:  0.06599494999999989
1000 элементов:  0.6784994410000005
Вывод: Очень полезный алгоритм сортировки, т.к работает гораздо быстрее пузырька и шейкерного алгоритма.
"""