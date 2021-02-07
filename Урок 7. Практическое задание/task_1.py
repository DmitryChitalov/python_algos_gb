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
from timeit import timeit


def bubble_sort(lst):
    last_el = len(lst) - 1
    for x in range(last_el):
        for idx in range(last_el - x):
            if lst[idx] < lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
    return lst


def bubble_sort_optimized(lst):
    last_el = len(lst) - 1
    for x in range(last_el):
        is_changed = False
        for idx in range(last_el - x):
            if lst[idx] < lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                is_changed = True
        if not is_changed:
            return lst

    return lst


start_list = [randint(-100, 100) for i in range(1000)]
new_list = bubble_sort(start_list[:])
new_list_opt = bubble_sort_optimized(start_list[:])

# print(f'Start list: \n{start_list}')
# print(f'New list: \n{new_list}')
# print(f'New list optimized: \n{new_list_opt}')

print('Time for bubble_sort: ', timeit('bubble_sort(start_list[:])',
                                       globals=globals(), number=100))

print('Time for bubble_sort_optimized: ',
      timeit('bubble_sort_optimized(start_list[:])',
             globals=globals(), number=100))

"""
Замеры для списка из 1000 элементов на 100 измерений:

Time for bubble_sort:  16.363335199999998
Time for bubble_sort_optimized:  16.982484200000002

Мой вариант оптимизации кода не дает экономии времени. В зависимости от 
самого списка экономия возможна, то есть в некоторых случаях всё-таки 
оптимизированная функция работает быстрее, но в большинстве случаев время 
работы остается таким же или увеличивается.
"""
