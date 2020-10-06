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

import timeit
import random


def bubble_sort_v1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_v2(lst_obj):
    n = 1
    while n < len(lst_obj):
        check = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                check = False
        if check:
            break
        n += 1
    return lst_obj


def new_list():
    return [random.randint(-100, 100) for el in range(100)]


#  Замер: 1.0374032
print(timeit.timeit("bubble_sort_v1(new_list())", setup="from __main__ import bubble_sort_v1, new_list", number=1000))

#  Замер: 1.0302824
print(timeit.timeit("bubble_sort_v2(new_list())", setup="from __main__ import bubble_sort_v2, new_list", number=1000))

"""
Вывод: добавление флага проверки отсутствия изменений в массиве помогает, хотя и довольно незначительно. 
"""
