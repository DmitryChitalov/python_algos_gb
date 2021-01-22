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

import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_mod(lst_obj):
    n = 1
    x = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                x = 1
        if x == 0:
            break
        n += 1
    return lst_obj


lst_obj = [random.randint(-100, 100) for _ in range(1000)]


print('bubble_sort_time: ', timeit.timeit("bubble_sort(lst_obj[:])", \
                                          setup="from __main__ import bubble_sort, lst_obj", number=1000))

print('bubble_sort_mod_time: ',timeit.timeit("bubble_sort_mod(lst_obj[:])", \
                                              setup="from __main__ import bubble_sort_mod, lst_obj", number=1000))

print(lst_obj)

bubble_sort(lst_obj)
print(lst_obj)

bubble_sort_mod(lst_obj)
print(lst_obj)


'''Как видим, доработка ускорила работу функции. Особенно хорошо заметно на больших аргументах. Неоптимизированная 
функция не останавливала работу цикла и проходила по всему массиву в то время, как модифицированная функция останавли-
вала дальнейшее течение цикла, когда в списке встречались повторяющиеся значения. 

Результаты по времени на range(100):
bubble_sort_time:  1.1237306999999999
bubble_sort_mod_time:  1.0968498999999998

Результаты по времени на range(1000):
bubble_sort_time:  114.7681566
bubble_sort_mod_time:  112.30503319999998
 '''

