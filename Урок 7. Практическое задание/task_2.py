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

import random
from timeit import timeit


###################################################################
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


###################################################################

def merge_sort(in_arr):
    if len(in_arr) < 2:
        return in_arr
    left = in_arr[:len(in_arr) // 2]
    right = in_arr[len(in_arr) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


###################################################################
min = 0
max = 50
m = 5000

randnums = [random.uniform(min, max) for _ in range(m)]
print(randnums)


###################################################################
def main():
    num_arr = merge_sort(randnums.copy())
    print(num_arr)
    print(
        timeit(
            "merge_sort(randnums)",
            setup='from __main__ import merge_sort, randnums',
            number=10))


###################################################################
main()
