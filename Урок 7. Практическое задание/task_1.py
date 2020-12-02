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


def standart_metod(unsorted):
    i = 1
    while i < len(unsorted):
        for el in range(len(unsorted) - i):
            if unsorted[el] < unsorted[el + 1]:
                unsorted[el], unsorted[el + 1] = unsorted[el + 1], unsorted[el]
        i += 1
    return unsorted


def update_metod(unsorted):
    i = 1
    while i < len(unsorted):
        change = 0
        for el in range(len(unsorted) - i):
            if unsorted[el] < unsorted[el + 1]:
                unsorted[el], unsorted[el + 1] = unsorted[el + 1], unsorted[el]
                change += 1
        if change == 0:
            break
        i += 1
    return unsorted


start_list = [random.randint(-100, 100) for i in range(1000)]
print(start_list)
print(
    timeit.timeit("standart_metod(start_list[:])", setup="from __main__ import standart_metod, start_list", number=100))
print(timeit.timeit("update_metod(start_list[:])", setup="from __main__ import update_metod, start_list", number=100))

'''
У меня из 10 запусков в 4 с доработкой ушло больше времени, примерно на 2-3 секунды
'''
