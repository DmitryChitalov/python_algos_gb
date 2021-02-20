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
"""
Input number of array elements:
10
MergeSort 10 elements
0.0002089999999999037
MergeSort 100 elements
0.0030186000000003155
MergeSort 1000 elements
0.03667569999999998
"""

from timeit import timeit
import random


def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))

    while len(left) > 0:
        res.append(left.pop(0))
    while len(right) > 0:
        res.append(right.pop(0))
    return res


def merge_sort(in_arr):
    if len(in_arr) < 2:
        return in_arr
    left = in_arr[:len(in_arr) // 2]
    right = in_arr[len(in_arr) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# num_arr = [random.uniform(0, 50) for _ in range(10)]
# print(num_arr)
# num_arr = merge_sort( num_arr )

print('Input number of array elements:')
qty = int(input())
num_arr = [random.uniform(0, 50) for _ in range(qty)]
print(f'MergeSort {len(num_arr)} elements')
#print(num_arr)
print(
    timeit(
        "merge_sort(num_arr)",
        setup='from __main__ import merge_sort, num_arr',
        number=10))
num_arr = merge_sort(num_arr)
#print(num_arr)

num_arr2 = [random.uniform(0, 50) for _ in range(qty*10)]
#print(num_arr2)
print(f'MergeSort {len(num_arr2)} elements')
print(
    timeit(
        "merge_sort(num_arr2)",
        setup='from __main__ import merge_sort, num_arr2',
        number=10))
num_arr2 = merge_sort(num_arr2)
#print(num_arr2)

num_arr3 = [random.uniform(0, 50) for _ in range(qty*100)]
#print(num_arr3)
print(f'MergeSort {len(num_arr3)} elements')
print(
    timeit(
        "merge_sort(num_arr3)",
        setup='from __main__ import merge_sort, num_arr3',
        number=10))
num_arr3 = merge_sort(num_arr3)
#print(num_arr3)
