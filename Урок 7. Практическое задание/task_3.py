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

from random import randint
from timeit import timeit

lst_1 = [randint(0, 100) for i in range(7)]


def not_sorted(lst):
    half_lst = len(lst) // 2
    for i in range(half_lst):
        lst.remove(max(lst))
    return max(lst)


def median_with_sort(lst):
    mid_i = len(lst) // 2
    return gnome_sort(lst)[mid_i]


def gnome_sort(lst):
    i = 0
    while i < len(lst):
        if i == 0:
            i = i + 1
        if lst[i] >= lst[i - 1]:
            i = i + 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i = i - 1
    return lst


print(not_sorted(lst_1[:]))
print(median_with_sort(lst_1))


print(timeit("gnome_sort(lst_1[:])", setup="from __main__ import gnome_sort, lst_1", number=1000))
