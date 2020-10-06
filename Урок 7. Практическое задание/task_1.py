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
from timeit import repeat
import random


# Реализовал сначала пузырек с последнего элемента. На всякий случай удалять не стал
# def bubble_sort(lst_obj):
#     n = 0
#     while n < len(lst_obj) - 1:
#         for i in reversed(range(n, len(lst_obj))):
#             if lst_obj[i] < lst_obj[i-1]:
#                 lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
#         n += 1
#     return lst_obj
def bubble_sort(lst_obj_origin):
    lst_obj = lst_obj_origin.copy()
    n = 1
    while n < len(lst_obj) - 1:
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_update(lst_obj_origin):
    lst_obj = lst_obj_origin.copy()
    n = 1
    go = 1
    while go != 0:
        go = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                go += 1
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

bs = repeat('bubble_sort(orig_list)',
            'from __main__ import bubble_sort, orig_list', repeat=10, number=10000)
bsu = repeat('bubble_sort_update(orig_list)',
             'from __main__ import bubble_sort_update, orig_list', repeat=10, number=10000)

print(f'Обычный алгоритм: {sum(bs) / len(bs)}')
print(f'Умный алгоритм: {sum(bsu) / len(bsu)}')

"""
По моим замерам получилось, что умный алгоритм работает примерно так же, что и обычный. В некоторых
случаях чуть-чуть быстрее, а в некоторых, чуть-чуть медленнее. Предполагаю, что это связано с тем, что
умный алгоритм, каждый раз должен обнулять переменную "go"(присваивать ей 0) и увеличивать ее на 1,
а это тоже требует затрат времени.
"""
