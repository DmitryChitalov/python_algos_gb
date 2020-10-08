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
from memory_profiler import profile

@profile
def bubble_sort(lst_obj):
    n = 1
    print(f'start {len(lst_obj)}:', lst_obj)
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i + 1], lst_obj[i] = lst_obj[i], lst_obj[i + 1]
        n += 1
    print(f'finish {len(lst_obj)}:', lst_obj)
    return lst_obj

@profile
def bubble_sort_opt(our_list):
    has_swapped = True
    num_of_iterations = 0
    print(f'start {len(our_list)}:', our_list)
    while(has_swapped):
        has_swapped = False
        for i in range(len(our_list) - num_of_iterations - 1):
            if our_list[i] > our_list[i+1]:
                our_list[i], our_list[i+1] = our_list[i+1], our_list[i]
                has_swapped = True
        num_of_iterations += 1
    print(f'finish {len(our_list)}:',our_list)
    return our_list

orig_list = [random.randint(-100, 100) for _ in range(10)]
# замеры 10
print('Базовый алгоритм')
print(timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=1))
print('Модифицированный алгоритм')
print(timeit.timeit("bubble_sort_opt(orig_list[:])", setup="from __main__ import bubble_sort_opt, orig_list", number=1))


orig_list = [random.randint(-100, 100) for _ in range(100)]
# замеры 100
print('Базовый алгоритм')
print(timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=1))
print('Модифицированный алгоритм')
print(timeit.timeit("bubble_sort_opt(orig_list[:])", setup="from __main__ import bubble_sort_opt, orig_list", number=1))


orig_list = [random.randint(-100, 100) for _ in range(1000)]
# замеры 1000
print('Базовый алгоритм')
print(timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=1))
print('Модифицированный алгоритм')
print(timeit.timeit("bubble_sort_opt(orig_list[:])", setup="from __main__ import bubble_sort_opt, orig_list", number=1))

"""
Модифицированный алгоритм эффективнее т.к. 
с каждой последовательной итерацией мы можем просматривать на один элемент меньше, чем раньше.
"""