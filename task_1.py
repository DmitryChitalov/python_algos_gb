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

from random import randrange
from timeit import timeit


def bull(lst):
    for i in range(len(lst) - 1):
        check = True
        for j in range(len(lst) - i - 1):
            if lst[j] < lst[j + 1]:
                check = False
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if check: break
    return lst


my_list = [randrange(-100, 100) for _ in range(10)]

print(timeit(stmt='bull(my_list[:])', setup='from __main__ import bull,my_list'))
print(timeit(stmt='bull(my_list)', setup='from __main__ import bull,my_list'))

# это значительно ускоряет время выполнения по уже отсортированным спискам
