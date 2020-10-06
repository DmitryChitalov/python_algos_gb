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

# Если заканчивать функцию, в случаи отсутствия сортировки, алгоритм работает быстрее

import random
import timeit


def bubble_sort(list_1):
    n = 1
    while n <= len(list_1):
        for i in range(len(list_1) - 1):
            if list_1[i] < list_1[i + 1]:
                list_1[i], list_1[i + 1] = list_1[+1], list_1[i]
        n += 1
    return list_1


orig_list = [random.randint(-100, 100) for _ in range(10)]

print(orig_list)
print(bubble_sort(orig_list))
# замеры 10
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1000))


def bubble_sort_2(list_1):
    n = 1
    while n <= len(list_1):
        sort = 0
        for i in range(len(list_1) - 1):
            if list_1[i] < list_1[i + 1]:
                list_1[i], list_1[i + 1] = list_1[+1], list_1[i]
                sort += 1
        if sort == 0:
            break

        n += 1
    return list_1


print(bubble_sort_2(orig_list))
# замеры 10
print(timeit.timeit("bubble_sort_2(orig_list)", \
                    setup="from __main__ import bubble_sort_2, orig_list", number=1000))
