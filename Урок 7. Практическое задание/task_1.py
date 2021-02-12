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


def bubble_sort_orig(i_lst):
    i = 0
    while i < (len(i_lst)-1):
        j = 0
        while j < (len(i_lst)-1-i):
            if i_lst[j] < i_lst[j+1]:
                i_lst[j], i_lst[j+1] = i_lst[j+1], i_lst[j]
            j += 1
        i += 1


def bubble_sort_optim(i_lst):
    i = 0
    l_cont = True
    while i < (len(i_lst)-1) and l_cont:
        j = 0
        l_cont = False
        while j < (len(i_lst)-1-i):
            if i_lst[j] < i_lst[j+1]:
                i_lst[j], i_lst[j+1] = i_lst[j+1], i_lst[j]
                l_cont = True
            j += 1
        i += 1


g_lst1 = [randint(-100, 100) for i in range(100)]
'''
print('Original-1:', g_lst1)
bubble_sort_orig(g_lst1)
print('Sorted-1:  ', g_lst1)

g_lst2 = [randint(-100, 100) for i in range(100)]
print('Original-2:', g_lst2)
bubble_sort_optim(g_lst2)
print('Sorted-2:  ', g_lst2)
'''
print(
    timeit(
        "bubble_sort_optim(g_lst1[:])",
        globals=globals(),
        number=10000))
# Для вызова bubble_sort_orig(g_lst1) время заняло 6.4985934.
# Для вызова bubble_sort_optim(g_lst1) время заняло 0.1438.
# Для вызова bubble_sort_orig(g_lst1[:]) время заняло 8.79.
# Для вызова bubble_sort_optim(g_lst1[:]) время заняло 8.08.
#
# Вывод: оптимизация(если за один проход не было перемещений, то выход)
# очень сильно ускорят работу для отсортированных массивов.
# Это значит, что для оптимизированного варианта массив обходится только один раз,
# вместо N**2.
