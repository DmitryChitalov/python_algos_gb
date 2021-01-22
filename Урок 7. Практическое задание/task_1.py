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
import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    n = 1
    k = 0
    while n < len(lst_obj):
        for elem in range(len(lst_obj)-n):
            if lst_obj[elem] < lst_obj[elem+1]:
                lst_obj[elem], lst_obj[elem+1] = lst_obj[elem+1], lst_obj[elem]
                k = 1
        if k == 0:
            break
        n += 1
    return lst_obj


lst_obj = [random.randint(-100, 100) for i in range(1000)]

print(lst_obj)
print(bubble_sort(lst_obj))
print(bubble_sort(lst_obj))

print(timeit.timeit("bubble_sort(lst_obj[:])", setup="from __main__ import bubble_sort, lst_obj", number=100))
print(timeit.timeit("bubble_sort_2(lst_obj[:])", setup="from __main__ import bubble_sort_2, lst_obj", number=100))

# Первую задачу взял и урока. Она здесь подходит
"""
7.3628849999999995
7.583501900000001
"""