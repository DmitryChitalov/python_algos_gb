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

setup = '''
import random

list1 = [random.choice(range(-100,100)) for _ in range(101)]


def bubble_sort(list):
    n = 1
    while n < len(list):
        for i in range(len(list) - n):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        n += 1
    return list


def bubble_sort_imp(list):
    n = 1
    check_sort = False
    while n < len(list):
        for i in range(len(list) - n):
            if list[i] < list[i + 1]:
                check_sort = True
                list[i], list[i + 1] = list[i + 1], list[i]
        if not check_sort:
            return list
        n += 1
    return list
'''

start_sort = 'bubble_sort(list1[:])'
start_sort2 = 'bubble_sort_imp(list1[:])'


print(f'Время выполнения bubble_sort - {timeit(start_sort, setup, number=100)}')
print(f'Время выполнения bubble_sort_imp - {timeit(start_sort2, setup, number=100)}')

'''Вывод: замеры времени показывают, что в данном случайном списке оптимизация не работает
 (иногда показывает экономию времени, иногда наоборот). Возможно, эта оптимизация сработает,
 когда в большом списке известны паттерны формирования и можно пропускать большие куски сортировки'''

