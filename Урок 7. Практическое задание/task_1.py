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
        for i in range(len(lst_obj) - n):  # Всплывают самые маленькие значения
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj
# Сортируем список по убыванию


def better_bubble_sort(lst_obj):
    n = 1
    flag = False
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        if flag:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for i in range(10)]

print(f'обычная пузырьковая: \
    {timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=1000)} ')
orig_list = [random.randint(-100, 100) for i in range(10)]
print(f'улучшенная пузырьковая: \
{timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=1000)} ')

"""range(10)
обычная пузырьковая:     0.012711199999999999 
улучшенная пузырьковая: 0.012053500000000002  """

""" range(100)
обычная пузырьковая:     0.7771168 
улучшенная пузырьковая: 0.7686462000000001 
"""
""" Улучшенная версия дает незначительный прирост. Однако существенной разницы 
не наблюдалось. Как  говорилось ранее  на уроке, весьма малая  вероятность ,что попадется 
уже отсортированный массив"""
