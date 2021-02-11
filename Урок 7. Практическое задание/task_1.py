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

import random
from timeit import timeit


def func_sort(list_num):
    for i in range(len(list_num) - 1, 0, -1):
        for j in range(0, i):
            if list_num[j + 1] > list_num[j]:
                list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
    return list_num


def func_sort_mod(list_num):
    for i in range(len(list_num) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if list_num[j + 1] > list_num[j]:
                list_num[j], list_num[j + 1] = list_num[j + 1], list_num[j]
                no_swap = False
        if no_swap:
            return list_num
    return list_num


nums_10 = [random.randint(-100, 100) for _ in range(10)]
nums_100 = [random.randint(-100, 100) for _ in range(100)]
nums_1000 = [random.randint(-100, 100) for _ in range(1000)]

print(func_sort(nums_10[:]))
print(func_sort_mod(nums_10[:]))
print(nums_10, '\n')

print(func_sort(nums_100[:]))
print(func_sort_mod(nums_100[:]))
print(nums_100, '\n')

print(func_sort(nums_1000[:]))
print(func_sort_mod(nums_1000[:]))
print(nums_1000, '\n')

print('Замеры обычной функции:')
print(timeit("func_sort(nums_10[:])", globals=globals(), number=1000))
print(timeit("func_sort(nums_100[:])", globals=globals(), number=1000))
print(timeit("func_sort(nums_1000[:])", globals=globals(), number=1000))
print('Замеры оптимизированной функции:')
print(timeit("func_sort_mod(nums_10[:])", globals=globals(), number=1000))
print(timeit("func_sort_mod(nums_100[:])", globals=globals(), number=1000))
print(timeit("func_sort_mod(nums_1000[:])", globals=globals(), number=1000))

"""
Замеры обычной функции:
0.013223792000000012
1.223140367
123.43215817
Замеры оптимизированной функции:
0.013375203000009606
1.0983337700000106
124.41100866899998

Оптимизация не показывает свою эффективность 
"""
