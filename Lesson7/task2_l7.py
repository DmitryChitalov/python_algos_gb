"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

import random
from timeit import timeit


def merge_sort(alist):  #Слияние

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


n = int(input("Введите число элементов: "))
alist = [random.random()*50 for i in range(n)]

print(f"Исходный - {alist}")
merge_sort(alist)
print(f"Отсортированный - {alist}")

#Замеры:
alist1 = [random.random() * 50 for _ in range(10)]
print(timeit("merge_sort(alist1)", setup="from __main__ import merge_sort, alist1", number=100))
alist2 = [random.random() * 50 for _ in range(100)]
print(timeit("merge_sort(alist2)", setup="from __main__ import merge_sort, alist2", number=100))
alist3 = [random.random() * 50 for _ in range(1000)]
print(timeit("merge_sort(alist3)", setup="from __main__ import merge_sort, alist3", number=100))
