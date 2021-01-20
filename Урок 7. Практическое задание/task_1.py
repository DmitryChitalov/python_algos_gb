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


def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        exchange = True
        for i in range(len(lst_obj) - n):
            if not exchange:
                break
            exchange = False

            for j in range(len(lst_obj) - n):
                if lst_obj[j] < lst_obj[j + 1]:
                    lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[j]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("bubble_sort_1(orig_list)",
                    setup="from __main__ import bubble_sort_1, orig_list", number=1))
# print(orig_list)

orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("bubble_sort_2(orig_list)",
                    setup="from __main__ import bubble_sort_2, orig_list", number=1))
print(orig_list)

#############################################################

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort_1(orig_list)",
                    setup="from __main__ import bubble_sort_1, orig_list", number=1))
# print(orig_list)

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort_2(orig_list)",
                    setup="from __main__ import bubble_sort_2, orig_list", number=1))
print(orig_list)

#############################################################

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort_1(orig_list)",
                    setup="from __main__ import bubble_sort_1, orig_list", number=1))
# print(orig_list)

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort_2(orig_list)",
                    setup="from __main__ import bubble_sort_2, orig_list", number=1))
print(orig_list)

'''
После доработки алгоритма сортировки пузырьком видно, что алгоритм стал более быстродейственным.
# замеры 10
1.9502999748510774e-05
1.7917999684868846e-05
# замеры 100
0.0013273260001369636
0.0009115719994952087
# замеры 1000
0.11702334599976894
0.08842120299959788
'''
