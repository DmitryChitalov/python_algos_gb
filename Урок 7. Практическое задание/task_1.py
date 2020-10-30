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
    for n in range(0, len(lst_obj) - 1):
        flag = True
        for i in range(len(lst_obj) - 1, n, -1):
            if lst_obj[i] < lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
                flag = flag and False
        if flag:
            del n, flag
            return lst_obj
    del n, flag
    return lst_obj



orig_list = [random.randint(-100, 100) for _ in range(1000)]


# замеры 1000
print('Замеры времени неоптимизированной функции')
print(timeit.timeit("bubble_sort_1(orig_list[:])", setup="from __main__ import bubble_sort_1, orig_list", number=1))



# замеры 1000
print('------------------------------------------')
print('Замеры времени оптимизированной функции')
print(timeit.timeit("bubble_sort_2(orig_list[:])", setup="from __main__ import bubble_sort_2, orig_list", number=1))


'''получилось лишь слегка улучшить результаты
Замеры времени неоптимизированной функции
0.09513420000000002
------------------------------------------
Замеры времени оптимизированной функции
0.09364789999999998
'''