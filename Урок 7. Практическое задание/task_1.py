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
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_optim(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            flag = 0
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = 1
        if flag == 1:
            n += 1
        else:
            return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print(bubble_sort(orig_list[:]))
print(bubble_sort_optim(orig_list[:]))

# замеры
print(timeit.repeat("bubble_sort(orig_list[:])",
                    setup="from __main__ import bubble_sort, orig_list", repeat=5, number=1000))
print(timeit.repeat("bubble_sort_optim(orig_list[:])",
                    setup="from __main__ import bubble_sort_optim, orig_list", repeat=5, number=1000))

"""
Один из результатов замеров:
[0.009837838995736092, 0.014766625012271106, 0.015082622005138546, 0.014815785019891337, 0.013687147991731763]
[0.003437837993260473, 0.0032412879809271544, 0.0033189249807037413, 0.003383176022907719, 0.00317583599826321]
Замеры показывают что скорость сортировки в отдельных случаях увеличилась
в четыре раза. А иногда прирост не наблюдается вовсе. Результат зависит от исходного списка.
"""
