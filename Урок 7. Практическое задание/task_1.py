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


# время до оптимизации: 0.990234
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


# время после оптимизации 0.01288699999999987
def bubble_sort_1(lst_obj):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
    return lst_obj


my_list = [random.randint(-100, 100) for _ in range(100)]
copy_my_list = my_list.copy()
print(timeit('bubble_sort(copy_my_list)', setup='from __main__ import bubble_sort, copy_my_list', number=1000))
print(bubble_sort(copy_my_list))
print(timeit('bubble_sort_1(copy_my_list)', setup='from __main__ import bubble_sort_1, copy_my_list', number=1000))
print(copy_my_list)
# замеры показали, что оптимизация имеет смысл
