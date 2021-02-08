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
from timeit import timeit
import copy

orig_list = [random.randint(-100, 100) for _ in range(1000)]
orig_list_copy = copy.deepcopy(orig_list)


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


print("bubble_sort_original_timing: ",
      timeit("bubble_sort(orig_list[:])",
             setup="from __main__ import bubble_sort, orig_list",
             number=100))


def bubble_sort_optimized(lst_obj_new):
    n = 1
    is_changing = False
    while n < len(lst_obj_new):
        for i in range(len(lst_obj_new) - n):
            if lst_obj_new[i] < lst_obj_new[i + 1]:
                lst_obj_new[i], lst_obj_new[i + 1] = lst_obj_new[i + 1], lst_obj_new[i]
                is_changing = True
        if is_changing == False:
            break
        n += 1
    return lst_obj_new


print("bubble_sort_optimized_timing: ",
      timeit("bubble_sort_optimized(orig_list_copy[:])",
             setup="from __main__ import bubble_sort_optimized, orig_list_copy",
             number=100))


"""
    1. Изменить направление сортировки - изи - достаточно изменить знак > на < в операторе if.
    2. Попытка оптимизировать функцию заключалась в проверке условия - когда заданное условие
       lst_obj[i] < lst_obj[i + 1] при очередной проверке не отрабатывает, т.е. нет перестановки
       значений, а соответственно, нет необходимости в дальнейшем выполнении цикла while,
       переменная is_changing завершает цикл.
    3. Результаты замера времени выполнения функций:
       bubble_sort_original_timing:  7.0689003
       bubble_sort_optimized_timing: 7.0689003
       Оптимизация не оказала значительного влияния на время выполнения функции.
"""
