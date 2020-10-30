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
from random import randint, random
from timeit import timeit

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def upd_bubble_sort(lst_obj, exchanges=True):
    n = 1
    while n < len(lst_obj) and exchanges:
        exchanges = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i+1] > lst_obj[i]:
                lst_obj[i+1], lst_obj[i] = lst_obj[i], lst_obj[i+1]
                exchanges = True
        if not exchanges:
            break
        n += 1
    return lst_obj

orig_list = [randint(-100, 100) for _ in range(10)]
orig_list_2 = [96, 95, 94, 91, 80, 34, 33, 21, 11, 8]


print(upd_bubble_sort(orig_list))
print(upd_bubble_sort(orig_list_2))

#print(f'bubble_sort, unsorted list', timeit("bubble_sort(orig_list)", \
 #   setup="from __main__ import bubble_sort, orig_list"))   # 10.9194388 - сортировка пузырьком несортированного листа

#print(f'upd_bubble_sort, unsorted list', timeit("bubble_sort(orig_list)", \
 #   setup="from __main__ import bubble_sort, orig_list"))   # 11.641853 - сортировка улучшенным пузырьком несортированного листа

#print(f'bubble_sort, sorted list', timeit("upd_bubble_sort(orig_list_2)", \
 #   setup="from __main__ import upd_bubble_sort, orig_list_2"))   # 1.9140815 - сортировка пузырьком сортированного списка

print(f'upd_bubble_sort, sorted list', timeit("bubble_sort(orig_list_2)", \
    setup="from __main__ import bubble_sort, orig_list_2"))   # 11.75743 - сортировка улучшенным пузырьком сортированного списка

#Либо