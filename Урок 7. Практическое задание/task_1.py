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
"""
Как видно из результатов замеров, сортировка 'bubble_sort_opt' работает быстрее за счет уменьшения количества итераций.
"""
import timeit
import random


def bubble_sort(lst_obj):
    print(f'Simple sort:')
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_opt(lst_obj):
    print(f'Smart sort:')
    n = 1
    while n < len(lst_obj):
        val_check = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                val_check = False
        if val_check:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(6)]
print(orig_list)

test_1 = orig_list
print(timeit.timeit("bubble_sort(test_1)", setup="from __main__ import bubble_sort, test_1", number=1))
print(orig_list)


test_2 = orig_list
print(timeit.timeit("bubble_sort_opt(test_2)", setup="from __main__ import bubble_sort_opt, test_2", number=1))
print(orig_list)