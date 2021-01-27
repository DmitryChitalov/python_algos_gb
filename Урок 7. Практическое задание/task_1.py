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


orig_list_1 = [random.randint(-100, 100) for _ in range(10)]
orig_list_2 = orig_list_1.copy()


def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj
# Беру тот же скрипт из примера и меняю знак больше на меньше, получается сортировка по убыванию.


print(orig_list_1)
print(timeit.timeit("bubble_sort_1(orig_list_1)", \
     setup="from __main__ import bubble_sort_1, orig_list_1", number=100))
print(orig_list_1)
print('------------------------------------------')


def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        old_lst_obj = lst_obj.copy()
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if old_lst_obj == lst_obj:
            return lst_obj
        n += 1
    return lst_obj
# Пусть он до прохода по списку запоминает копию списка и после прохода сравнивает с новым.
# если ничего не изменилось, то пора заканчивать. Это убирает очень много проходов по списку, я добавляла print(lst_obj)
# и смотрела наглядно.


print(orig_list_2)
print(timeit.timeit("bubble_sort_2(orig_list_2)", \
     setup="from __main__ import bubble_sort_2, orig_list_2", number=100))
print(orig_list_2)
print('------------------------------------------')

# Видим, что функция работает верно и время выполнения уменьшилось примерно в 5 раз.
# [-31, -40, 18, 60, -1, 64, 95, 59, -34, -50]
# 0.001015099999999998
# [95, 64, 60, 59, 18, -1, -31, -34, -40, -50]
# --------------------------------------------------
# [-31, -40, 18, 60, -1, 64, 95, 59, -34, -50]
# 0.0002134999999999984
# [95, 64, 60, 59, 18, -1, -31, -34, -40, -50]

#
# def bubble_sort_3(lst_obj):
#     for n in range(len(lst_obj)):
#         old_lst_obj = lst_obj.copy()
#         for i in range(len(lst_obj)-n-1):
#             if lst_obj[i] < lst_obj[i+1]:
#                 lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
#         if old_lst_obj == lst_obj:
#             return lst_obj
#     return lst_obj
# # Пусть он до прохода по списку запоминает копию списка и после прохода сравнивает с новым.
# # если ничего не изменилось, то пора заканчивать.
#
#
# print(orig_list_3)
# print(timeit.timeit("bubble_sort_3(orig_list_3)", \
#      setup="from __main__ import bubble_sort_3, orig_list_3", number=100))
# print(orig_list_3)
