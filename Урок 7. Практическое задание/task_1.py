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

from random import randint
from timeit import timeit


def bubble_sort_1(value):
    count = 1
    while count < len(value):
        for j in range(len(value) - count):
            if value[j] < value[j + 1]:
                value[j], value[j + 1] = value[j + 1], value[j]
        count += 1
    return value


def bubble_sort_2(value):
    count = 1
    turn = 0
    while count < len(value):
        for i in range(len(value) - count):
            if value[i] < value[i + 1]:
                value[i], value[i + 1] = value[i + 1], value[i]
                turn = 1
        if turn == 0:
            break
        count += 1
    return value


val = [randint(-100, 100) for i in range(1010)]

print(val)

print('bubble_sort_1 = ')
print(bubble_sort_1(val[:]))
print(timeit('bubble_sort_1(val[:])',
             setup='from __main__ import bubble_sort_1, val',
             number=101))

print('*' * 100)

print('bubble_sort_2 = ')
print(bubble_sort_2(val[:]))
print(timeit('bubble_sort_2(val[:])',
             setup='from __main__ import bubble_sort_2, val',
             number=101))

print(val)


'''
Оптимизация эффекта не дала, этовидно по результатам замеров:
bubble_sort_1 = 17.225380111
bubble_sort_2 = 17.525074363
'''
