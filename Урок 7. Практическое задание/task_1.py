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

orig_list = [random.randint(-100, 100) for _ in range(10)]
orig_list_2 = orig_list[:]


def bubble_sort(lst_obj):
    orig_list_copy = lst_obj[:]
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return f'Исходный массив:        {orig_list_copy}\nOтсортированный массив: {lst_obj}'


print('Время работы функции без доработки 10, 100 и 1000 повторов:\n')
# замеры 10
print(timeit.timeit("bubble_sort(orig_list[:])",
                    setup="from __main__ import bubble_sort, orig_list", number=10))

# замеры 100
print(timeit.timeit("bubble_sort(orig_list[:])",
                    setup="from __main__ import bubble_sort, orig_list", number=100))

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list[:])",
                    setup="from __main__ import bubble_sort, orig_list", number=1000))


def bubble_sort_2(lst_obj):
    orig_list_copy = lst_obj[:]
    n = 1
    while n < len(lst_obj):
        number_of_passes = 0
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                number_of_passes += 1
        if number_of_passes == 0:
            break
        n += 1
    return f'Исходный массив:        {orig_list_copy}\nOтсортированный массив: {lst_obj}'


print('\nВремя работы функции c доработкой 10, 100 и 1000 повторов:\n')
# замеры 10
print(timeit.timeit("bubble_sort_2(orig_list_2[:])",
                    setup="from __main__ import bubble_sort_2, orig_list_2", number=10))

# замеры 100
print(timeit.timeit("bubble_sort_2(orig_list_2[:])",
                    setup="from __main__ import bubble_sort_2, orig_list_2", number=100))

# замеры 1000
print(timeit.timeit("bubble_sort_2(orig_list_2[:])",
                    setup="from __main__ import bubble_sort_2, orig_list_2", number=1000))
print()
if __name__ == "__main__":
    print(bubble_sort(orig_list))
    print(bubble_sort_2(orig_list_2))

"""Сделав оптимизацию алгоритма - break если не сдалана ни одна замена, получил на выходе большее время выполнения
функции. Т.е. идет подсчет замен в массиве в цикле for.
Таким образом оптимизация оказалась не эффективной.
Проводя замеры на различных данных - выяснил, что отсортированный массив обрабатывается на оптимизированной 
функции почти в 2 раза быстрее, но если массив рандомный, то эффект отрицательный.
Связано это, скорей всего, с дополнительной проверкой if, а так же с тем, что к тому моменту, когда срабатывает 
break - непройденными остаются всего несколько единиц n - счетчика, или срабатывает условие while.
Проведя дополнительные замеры - получил смешанные цифры, нет четко прослеживаемого преимущества от доработки."""
