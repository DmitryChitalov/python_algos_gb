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
from copy import copy

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        count = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                count +=1
        if count == 0:
            n = len(lst_obj)
        n += 1
    return lst_obj

orig_list = [random.randint(-100, 100) for _ in range(2000)]
orig_list_2 = copy(orig_list)

print(timeit('bubble_sort(orig_list)', setup='from __main__ import bubble_sort, orig_list', number=1))
print(timeit('bubble_sort_2(orig_list_2)', setup='from __main__ import bubble_sort_2, orig_list_2', number=1))

'''
0.4671839 - без доработки
0.4910934 - с доработкой

После нескольких запусков программы, у меня только пару раз вышло, что доработанный код работает быстрее...
По факту, иногда это может ускорить программу, но как показывает статистика это случается редко

'''

