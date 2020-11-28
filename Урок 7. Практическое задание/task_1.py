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
    change_counter = False
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                change_counter = True
        if change_counter is False:
            break
        n += 1
    return lst_obj

def standart_bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


m = int(input("Введите количество символов массива: "))
my_list = [random.randrange(-100, 100) for i in range(m)]
print(bubble_sort(my_list))
print(standart_bubble_sort(my_list))

print(timeit.timeit("standart_bubble_sort(my_list[:])", setup="from __main__ import standart_bubble_sort, my_list", number=100))
print(timeit.timeit("bubble_sort(my_list[:])", setup="from __main__ import bubble_sort, my_list", number=100))

"""
Результаты: сортировка с досрочным завершением оказалась гораздо быстрее:
0.0006181000000000658 против 0.00021780000000015676.
"""