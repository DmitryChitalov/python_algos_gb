"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""

from random import random
from timeit import timeit


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)
        # перестали делить, выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst_obj[k] = left[i]
                i += 1
            else:
                lst_obj[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst_obj[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst_obj[k] = right[j]
            j += 1
            k += 1
        return lst_obj


def merge(a: list, b: list):
    """ алгоритм слияния списков """
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:  # сортировка называется "устойчивой", если она не меняет порядок равных элементов.
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1
    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


def rec_merge_sort(lst_obj):
    """ рекурсия """
    if len(lst_obj) <= 1:  # первым делом указываем крайний случай
        return
    middle = len(lst_obj) // 2
    left = [lst_obj[i] for i in range(0, middle)]
    right = [lst_obj[i] for i in range(middle, len(lst_obj))]
    rec_merge_sort(left)
    rec_merge_sort(right)
    result = merge(left, right)  # слияние двух массивов в новый
    for i in range(len(lst_obj)):  # lst_obj = result нельзя, т.к. result съест сборщик мусора после выхода из функции
        lst_obj[i] = result[i]


def original(lst_obj):
    return merge_sort(lst_obj)


def recursion(lst_obj):
    return rec_merge_sort(lst_obj)


my_list = [random()*50 for x in range(5)]


print(f'Изначальный массив : {my_list}')
print(f'результат: {merge_sort(my_list[:])} (оригинал): ', end="")
print(timeit("original(my_list[:])", setup="from __main__ import original, my_list", number=100_000))
print(f'результат: {merge_sort(my_list[:])} (рекурсия): ', end="")
print(timeit("recursion(my_list[:])", setup="from __main__ import recursion, my_list", number=100_000))

""" Изначальный массив : [0.45222765620333, 13.309794980208, 5.646025699412, 19.59602360750, 4.560215729882]
    результат: [0.45222765620333, 4.560215729882, 5.646025699412, 13.309794980208, 19.59602360750] (оригинал): 1.190
    результат: [0.45222765620333, 4.560215729882, 5.646025699412, 13.309794980208, 19.59602360750] (рекурсия): 2.613
    
    Вывод: как и в предыдущем задании рекурсия никак не оптимизирует вычисления :)
"""