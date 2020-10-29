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
from timeit import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_optimized(lst_obj):
    go_flag = True
    while go_flag:
        go_flag = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                go_flag = True
    return lst_obj


inp_lst = [random.randint(-100, 100) for _ in range(100)]
print(f'{inp_lst}\n')
print(f'{bubble_sort(inp_lst.copy())}\n')
print(f'{bubble_sort_optimized(inp_lst.copy())}\n')
print(timeit('bubble_sort(inp_lst.copy())',
             setup='from __main__ import bubble_sort, inp_lst',
             number=1000))
print(timeit('bubble_sort_optimized(inp_lst.copy())',
             setup='from __main__ import bubble_sort_optimized, inp_lst',
             number=1000))
# Вывод: "Оптимизированная" функция менее быстродейственна
