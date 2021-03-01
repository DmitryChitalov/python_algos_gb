"""
3. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import copy
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
    """
    Возвращает медиану массива путем удаления максимальных элементов
    """
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


def gnome_sort(sort_list):
    """
    Сортировка списка методом gnome_sort
    Происходит просмотр массива слева-направо,
    при этом сравниваются (и меняются, если это неотсортированная пара)
    соседние элементы. Если происходит обмен элементов, то проиходит
    возвращение на один шаг назад. Если обменов не происходит, то алгоритм
    продолжает просмотр массива слева-направо в поиске неотсортированных пар.
    """
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


m = int(input('Введите m: '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив:\n{orig_list}\n')


# Нахождение медианы через встроенную функцию
print(f'Медиана - {median(orig_list)}')
# Нахождение медианы без сортировки исходного массива
print(f'Медиана (без сортировки) - {without_sort(orig_list)}')
# Нахождение медианы еще одним вариантом без сортировки исходного массива
print(f'Медиана (без сортировки) - {another_way(orig_list)}')
# Нахождение медианы с сортировкой исходного массива
print(f'Медиана (с сортировкой) - {gnome_sort(orig_list)[m]}')

print(
    timeit.timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=10000))
print(
    timeit.timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=10000))
print(
    timeit.timeit(
        "another_way(orig_list[:])",
        globals=globals(),
        number=10000))
print(
    timeit.timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=10000))

"""
m = 10

0.008883500000000044 - median
0.23688660000000006
0.031861999999999835
0.018787099999999946 - гномья

m = 100
0.017139100000000074 - median
16.540844200000002
1.3362371999999993
0.1674717000000001 - гномья

m = 1000
0.12168910000000022 - median
1593.6272246
104.41096199999993
2.049815299999864 - гномья
"""
