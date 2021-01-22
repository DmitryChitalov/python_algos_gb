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

import timeit
from statistics import median
import random


def sort(lst_obj):
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


count = int(input('Введите m: '))
lst_obj = [random.randint(0, 100) for i in range(2 * count + 1)]

print(f'Медиана - {median(lst_obj)}')

print(timeit.timeit("sort(lst_obj[:])", setup="from __main__ import sort, lst_obj", number=10000))
