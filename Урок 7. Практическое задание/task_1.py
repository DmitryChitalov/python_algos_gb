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


def create_arr(number):
    arr = []
    for _ in range(number):
        arr.append(randint(-100, 100))
    return arr


def bubble():
    arr = create_arr(1000)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


def bubble_plus():
    n = 1
    arr = create_arr(1000)
    while n < len(arr):
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1


def bubble_extra_plus():
    n = 1
    arr = create_arr(1000)
    while n < len(arr):
        f = True
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                f = False
        if f:
            break
        n += 1


print(timeit(
    'bubble()',
    setup='from __main__ import bubble, create_arr', number=10
))  # 1.098884273
print(timeit(
    'bubble_plus()',
    setup='from __main__ import bubble_plus, create_arr', number=10
))  # 1.2367950650000001
print(timeit(
    'bubble_extra_plus()',
    setup='from __main__ import bubble_extra_plus, create_arr', number=10
))  # 1.2961250500000001 толку нет, больше временени тратится на проверку условия
