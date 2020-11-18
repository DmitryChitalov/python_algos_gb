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
from random import randint
from statistics import median


def without_sort(lst_obj):
    temp = lst_obj
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


def another_way(lst_obj):
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


def gnome_sort(sort_list):
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


def gnome_median(sort_list):
    return gnome_sort(sort_list)[len(sort_list) // 2]


m = int(input('m = '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'исходный массив:\n{orig_list}\n')

print(median(orig_list))
print(without_sort(orig_list))
print(another_way(orig_list))
print(gnome_sort(orig_list)[m])

print(timeit.timeit('median(orig_list[:])',
                    setup='from __main__ import orig_list, median', number=100))
print(timeit.timeit('without_sort(orig_list[:])',
                    setup='from __main__ import orig_list, without_sort', number=100))
print(timeit.timeit('another_way(orig_list[:])',
                    setup='from __main__ import orig_list, another_way', number=100))
print(timeit.timeit('gnome_sort(orig_list[:])',
                    setup='from __main__ import orig_list, gnome_sort', number=100))
