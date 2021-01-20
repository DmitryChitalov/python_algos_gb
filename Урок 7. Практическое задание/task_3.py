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

import random


def median(list1, n):
    if len(list1) == 0:
        return 0
    if len(list1) == 1:
        return list1[0]

    pivot = list1[0]

    less = []
    more = []
    pivots = []
    for item in list1:
        if item < pivot:
            less.append(item)
        elif item > pivot:
            more.append(item)
        else:
            pivots.append(item)

    if len(less) > n:
        return median(less, n)
    elif len(less) + len(pivots) >n:
        return pivots[0]
    else:
        return median(more, n- len(more) - len(pivots))



n = 3
array = [random.randint(-100, 100) for _ in range(2 * n + 1)]
print(f'Исходный массив {array}')
print(f'Медиана {median(array, n)}')
""" решение с гномьей"""
import numpy

import timeit
import random

def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data,data[n]
n=int(input("vvedite n"))
array = [random.randint(-100, 100) for _ in range(2 * n + 1)]
print(gnome(array))