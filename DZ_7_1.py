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
import timeit


def bubble(rand_list):
    for i in range(len(rand_list) - 1):
        for j in range(len(rand_list) - i - 1):
            if rand_list[j] < rand_list[j + 1]:
                rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]

    return rand_list


def bubble_upgrade(rand_list):
    i = 0
    e = 0
    while i < len(rand_list) - 1:
        for j in range(len(rand_list) - i - 1):
            if rand_list[j] < rand_list[j + 1]:
                rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]
                e = 1
        if e == 0:
            break
        i += 1
    return rand_list


rand_list = [randint(-100, 100) for i in range(1000)]

elapsed_bubble = (timeit.timeit("bubble(rand_list[:])",
                                setup="from __main__ import bubble, rand_list",
                                number=100))
elapsed_bubble_upgrade = (timeit.timeit("bubble_upgrade(rand_list[:])",
                                        setup="from __main__ import bubble_upgrade, rand_list",
                                        number=100))
print(elapsed_bubble)  # 10.3843928
print(elapsed_bubble_upgrade)  # 10.552127400000002

# Очевидно что эта идея по оптимизации "слабовата". У меня больше шансов стать миллионером, чем
# шанс того что рандом выдаст уже отсортированный список.
