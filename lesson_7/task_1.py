"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

"""Сортировка пузырьком"""

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_reverse(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_reverse_adv(lst_obj):
    n = 1
    if_sorted = True
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                if_sorted = False
        if if_sorted:
            return lst_obj
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

print('orig_list')
print(orig_list)
print('bubble_sort')
print(bubble_sort(orig_list[:]))
print('bubble_sort_reverse')
print(bubble_sort_reverse(orig_list[:]))
print('bubble_sort_reverse_adv')
print(bubble_sort_reverse_adv(orig_list[:]))

# замеры 10
print('замеры 10')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse_adv(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 100

orig_list = [random.randint(-100, 100) for _ in range(100)]

print('замеры 100')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse_adv(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 500

orig_list = [random.randint(-100, 100) for _ in range(500)]

print('замеры 500')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse_adv(orig_list[:])",
        globals=globals(),
        number=1000))

# замеры 500 для заранее отсортированного массива
orig_list = [random.randint(-100, 100) for _ in range(500)]
orig_list.sort()
orig_list.reverse()

print('замеры 500 для заранее отсортированного массива')
print(
    timeit.timeit(
        "bubble_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse(orig_list[:])",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "bubble_sort_reverse_adv(orig_list[:])",
        globals=globals(),
        number=1000))

"""
orig_list
[-36, 65, -52, -18, -77, -32, -83, 1, 38, 45]
bubble_sort
[-83, -77, -52, -36, -32, -18, 1, 38, 45, 65]
bubble_sort_reverse
[65, 45, 38, 1, -18, -32, -36, -52, -77, -83]
bubble_sort_reverse_adv
[65, 45, 38, 1, -18, -32, -36, -52, -77, -83]
замеры 10
0.008076300000000008
0.008012900000000003
0.012299100000000007
замеры 100
0.8102618
0.6642061
0.7531227
замеры 500
19.0830831
19.8505121
19.891533000000003
замеры 500 для заранее отсортированного массива
26.945552499999998
10.857758500000003
0.04267539999999315         вариант обратной сортировки с оптимизацией дает выигрыш по времени только в одном случае, 
                            когда на входе список уже отсортирован в обратном порядке 



"""
