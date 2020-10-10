"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

from statistics import median
from timeit import timeit


def find_median(value):
    cp_value = value[:]
    for i in range(len(value) // 2):
        cp_value.remove(max(cp_value))
    return max(cp_value)


val = [el for el in range(101)]
print(f'1. find_median = {find_median(val)}')
print(f'2. median = {int(median(val))}')

print(timeit('find_median(val)',
             setup='from __main__ import find_median, val',
             number=10101))

print(timeit('median(val)',
             setup='from __main__ import median, val',
             number=10101))
