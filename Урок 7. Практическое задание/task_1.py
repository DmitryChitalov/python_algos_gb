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
    lst_obj_p = orig_list
    n = 1
    while n < len(lst_obj_p):
        for i in range(len(lst_obj_p)-n):
            if lst_obj_p[i] < lst_obj_p[i+1]:
                lst_obj_p[i], lst_obj_p[i+1] = lst_obj_p[i+1], lst_obj_p[i]
        n += 1
    return lst_obj_p

def bubble_sort_up(lst_obj):
    n = 1
    lst_obj_up = orig_list
    lst_obj_n = [1]
    while n < len(lst_obj):
        if n < len(lst_obj_up) and len(lst_obj_n) != 0:
            lst_obj_n.clear()
            for i in range(len(lst_obj_up) - n):
                if lst_obj_up[i] < lst_obj_up[i + 1]:
                    lst_obj_up[i], lst_obj_up[i + 1] = lst_obj_up[i + 1], lst_obj_up[i]
                    lst_obj_n.append(lst_obj_up[i])
                    lst_obj_n.append(lst_obj_up[i + 1])
        elif n < len(lst_obj_up) and len(lst_obj_n) == 0:
            return lst_obj_up
        n += 1
    return lst_obj_up


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list))
print(timeit.timeit("bubble_sort(orig_list)",
                    setup="from __main__ import bubble_sort, orig_list", number=1))

#print(bubble_sort_up(orig_list))

#print(timeit.timeit("bubble_sort_up(orig_list)",
#                    setup="from __main__ import bubble_sort_up, orig_list", number=1))

''' Доработанная сортировка работает как минимум не мендленее, а чаще всего быстрее. Это обусловленно тем, что мы 
прекращаем вызывать лишние итерации, и сразу выдаем результат. 
[52, -25, 40, 34, 51, 93, 20, -7, 100, -94]
[100, 93, 52, 51, 40, 34, 20, -7, -25, -94]
3.100000000000325e-05
[-29, -67, -41, -51, 100, 47, 7, -24, -82, -96]
[100, 47, 7, -24, -29, -41, -51, -67, -82, -96]
1.6399999999999748e-05

'''