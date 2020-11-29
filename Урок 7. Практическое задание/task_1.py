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

# 1. Program "bubble sort" (Original version)

import random
import timeit

def bubble_sort_original(test_lst):
    el = 1
    while el < len(test_lst):
        for i in range(len(test_lst) - el):
            if test_lst[i] < test_lst[i + 1]:
                test_lst[i], test_lst[i + 1] = test_lst[i + 1], test_lst[i]
        el += 1
    return test_lst

# 2. Program "bubble sort" (Modified version)
def bubble_sort_modified(test_lst):
    el = 1
    pass_loop = 0
    while el < len(test_lst):
        for i in range(len(test_lst) - el):
            if test_lst[i] < test_lst[i + 1]:
                test_lst[i], test_lst[i + 1] = test_lst[i + 1], test_lst[i]
                pass_loop = 1
        if pass_loop == 0:
            break
        el += 1
    return test_lst

def print_lst(random_lst):
    '''
    Вывод списка по 10 элементов в ряд
    :param random_lst: 
    :return: None
    '''
    i = 0
    for el in range(len(random_lst)):
        if i == 10:
            print('\n')
            i = 0
        print(f'\t\t{random_lst[el]}', end='')
        i += 1


test_lst = [random.randint(-100, 100) for i in range(50)]
print(f'Program "Bubble sort"')
print('\n------------------------------------Test list--------------------------------------------------------------\n')
print_lst(test_lst)
print('\n------------------------------------Bubble sort original---------------------------------------------------\n')
bubble_sort_original(test_lst)
print_lst(test_lst)
print('\n------------------------------------Bubble sort update-----------------------------------------------------\n')
bubble_sort_modified(test_lst)
print_lst(test_lst)
print('\n--------------------------------------Замеры времени-------------------------------------------------------\n')
print('Work time "Bubble sort (original version)": ', end='')
print(timeit.timeit("bubble_sort_original(test_lst[:])",
                    setup='from __main__ import bubble_sort_original, test_lst', number = 100))
print('Work time "Bubble sort (modified version)": ', end='')
print(timeit.timeit("bubble_sort_modified(test_lst[:])",
                    setup='from __main__ import bubble_sort_modified, test_lst', number = 100))
'''
Результат работы
--------------------------------------Замеры времени-------------------------------------------------------
Work time "Bubble sort (original version)": 0.020194199999999995
Work time "Bubble sort (modified version)": 0.0007116999999999957

Вывод: 
Модифицированная версия выполняет сортировку быстрее.
'''


