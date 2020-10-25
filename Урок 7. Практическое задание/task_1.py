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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def flag_bub_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        change = True
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                change = False
        if change:
            break
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list))
print(f"bubble_sort, number=1000000: "
      f"{timeit('bubble_sort(orig_list)', setup='from __main__ import bubble_sort, orig_list', number=100000)}")
print()
orig_list = [randint(-100, 100) for _ in range(10)]
print(orig_list)
print(flag_bub_sort(orig_list))
print(f"flag_bubble_sort, number=1000000: "
      f"{timeit('flag_bub_sort(orig_list)', setup='from __main__ import flag_bub_sort, orig_list', number=100000)}")
"""
[66, 97, 66, -50, -33, -15, 47, 47, 9, 75]
[97, 75, 66, 66, 47, 47, 9, -15, -33, -50]
bubble_sort, number=1000000: 1.3553413

[30, -70, 75, 8, -91, -98, 40, -91, -27, 31]
[75, 40, 31, 30, 8, -27, -70, -91, -91, -98]
flag_bubble_sort, number=1000000: 0.23081459999999998

Оптимизация пузырькового метода дала значительный прирост производительности, 
что очень хорошо видно при замерах с большим количеством вызовов. 
"""