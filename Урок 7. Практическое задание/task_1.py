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

"""
Чтобы работать с одинаковыми масивами и цифрами решил вариант обычный оставить по возрастанию, 
а второй вариант согласно ДЗ по убыванию

Обычное решение замеры 10: 8.659999999999918e-05
Обычное решение замеры 100 : 0.0009213999999999993
Обычное решение замеры 1000: 0.0106365
Усовершенствованное решение замеры 100 : 2.8500000000000747e-05
Усовершенствованное 100 : 0.00023919999999999497
Усовершенствованное 100 : 0.0016115000000000018
"""
import timeit
import random


def bubble_sort1(lst_obj):  # обычное решение
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort(lst):
    n = 1
    while n < len(lst):
        count = 0
        for i in range(len(lst) - 1 - (n - 1)):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1
        if count == 0:
            break

        n += 1


array = [random.randint(-100, 100) for _ in range(10)]

print('Массив:', array, sep='\n')
bubble_sort1(array)
print('После сортировки обычным способом:', array, sep='\n')

print('Массив:', array, sep='\n')
bubble_sort(array)
print('После сортировки усовершенствованным способом:', array, sep='\n')

# замеры 10
print(
    f' Обычное решение замеры 10: {timeit.timeit("bubble_sort1(array[:])", setup="from __main__ import bubble_sort1, array", number=10)}')

# замеры 100
print(
    f' Обычное решение замеры 100 : {timeit.timeit("bubble_sort1(array[:])", setup="from __main__ import bubble_sort1, array", number=100)}')

# замеры 1000
print(
    f' Обычное решение замеры 1000: {timeit.timeit("bubble_sort1(array[:])", setup="from __main__ import bubble_sort1, array", number=1000)}')

# замеры 10
print(
    f' Усовершенствованное решение замеры 100 : {timeit.timeit("bubble_sort(array[:])", setup="from __main__ import bubble_sort, array", number=10)}')

# замеры 100
print(
    f' Усовершенствованное 100 : {timeit.timeit("bubble_sort(array[:])", setup="from __main__ import bubble_sort, array", number=100)}')

# замеры 1000
print(
    f' Усовершенствованное 100 : {timeit.timeit("bubble_sort(array[:])", setup="from __main__ import bubble_sort, array", number=1000)}')
