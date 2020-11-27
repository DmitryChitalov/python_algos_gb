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

my_list = [random.randint(-100, 100) for _ in range(100)]


def bubble(any_list):
    n = 1
    flag = True
    while n < len(any_list):
        for i in range(len(any_list) - n):
            if any_list[i] > any_list[i+1]:
                any_list[i], any_list[i+1] = any_list[i+1], any_list[i]
                flag = False
        if flag is True:
            break
        n += 1
    return any_list


print(my_list)
print(bubble(my_list[:]))
print(my_list)
print(timeit.timeit("bubble(my_list[:])", setup="from __main__ import bubble, my_list", number=100))


def bubble1(any_list):
    n = 1
    while n < len(any_list):
        for i in range(len(any_list) - n):
            if any_list[i] > any_list[i+1]:
                any_list[i], any_list[i+1] = any_list[i+1], any_list[i]
        n += 1
    return any_list

print(timeit.timeit("bubble1(my_list[:])", setup="from __main__ import bubble1, my_list", number=100))


'''Улучшенный вариант сортировки дает несущественное улучшение'''