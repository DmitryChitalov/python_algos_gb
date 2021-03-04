"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from timeit import timeit
from random import random


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1


    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1


    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


arr = [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]

n = len(arr)

print(arr)
mergeSort(arr, 0, n - 1)
print(arr)

#10
arr = [random()*5 for i in range(10)]

print(
    timeit(
        "mergeSort(arr, 0, n - 1)",
        globals=globals(),
        number=1000))

#100

arr = [random()*5 for i in range(100)]

print(
    timeit(
        "mergeSort(arr, 0, n - 1)",
        globals=globals(),
        number=1000))

#1000

arr = [random()*5 for i in range(1000)]

print(
    timeit(
        "mergeSort(arr, 0, n - 1)",
        globals=globals(),
        number=1000))

"""

0.010724899999999996
0.010048500000000002
0.009631899999999999

Нашел такой вариант реализации сортировки слиянием.
"""