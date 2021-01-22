"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере, а по убыванию
"""
import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_desc(lst_obj):
    count = 0
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                count = 1
        if count == 0:
            break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(100)]

print(timeit.timeit("bubble_sort(orig_list[:])", setup="from __main__ import bubble_sort, orig_list", number=1000))
print(timeit.timeit("bubble_desc(orig_list[:])", setup="from __main__ import bubble_desc, orig_list", number=1000))
"""
Результат при передачи массива на 100 эл
0.7270860640000001
0.721414241
По времени выполнения они одинаковы. Оптимизация алгоритма не прибавила ему эффективности.
Даже при выполнении на заранее отсортированном массиве оптимизированный алгоритм выполнялся дольше обычного (см ниже)

Результат при передачи уже отсортированного массива на 100 эл
0.439051372
1.0379644099999998
"""