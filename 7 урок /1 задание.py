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

def bubble_sort_1(sort_lst):
    print(f'Изначальный список: {sort_lst}')
    n = 1
    while n < len(sort_lst):
        for i in range(len(sort_lst)-n):
            if sort_lst[i] < sort_lst[i+1]:
                sort_lst[i], sort_lst[i+1] = sort_lst[i+1], sort_lst[i]
        n += 1
    print(f'Отсортированный список: {sort_lst}')
    return sort_lst

def bubble_sort_2(sort_lst):
    print(f'Изначальный список: {sort_lst}')
    n = 1
    count = 0
    while n < len(sort_lst):
        for i in range(len(sort_lst)-n):
            if sort_lst[i] < sort_lst[i+1]:
                sort_lst[i], sort_lst[i+1] = sort_lst[i+1], sort_lst[i]
                count += 1
        if count == 0:
            break
        n += 1
    print(f'Отсортированный список: {sort_lst}')
    return sort_lst


lst = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(f'Время затраченое на сортировку списка из 10 эллементов: {timeit.timeit("bubble_sort_1(lst[:])", setup="from __main__ import bubble_sort_1, lst", number=1)}')
print(f'Время затраченое на сортировку списка из 10 эллементов: {timeit.timeit("bubble_sort_2(lst[:])", setup="from __main__ import bubble_sort_2, lst", number=1)}')

lst = [random.randint(-100, 100) for _ in range(100)]

#замеры 100
print(f'Время затраченое на сортировку списка из 100 эллементов: {timeit.timeit("bubble_sort_1(lst[:])", setup="from __main__ import bubble_sort_1, lst", number=1)}')
print(f'Время затраченое на сортировку списка из 100 эллементов: {timeit.timeit("bubble_sort_2(lst[:])", setup="from __main__ import bubble_sort_2, lst", number=1)}')

lst = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(f'Время затраченое на сортировку списка из 1000 эллементов: {timeit.timeit("bubble_sort_1(lst[:])", setup="from __main__ import bubble_sort_1, lst", number=1)}')
print(f'Время затраченое на сортировку списка из 1000 эллементов: {timeit.timeit("bubble_sort_2(lst[:])", setup="from __main__ import bubble_sort_2, lst", number=1)}')


"""
Я дорпботал только возможностью выхода из цикла если за проход по списку не совершается ни одной сортировки
Замеры:
    Время затраченое на сортировку списка из 10 эллементов: 5.62350000000017e-05
    Время затраченое на сортировку списка из 10 эллементов: 3.1310999999999145e-05
    Время затраченое на сортировку списка из 100 эллементов: 0.0016456429999999952
    Время затраченое на сортировку списка из 100 эллементов: 0.0010282850000000038
    Время затраченое на сортировку списка из 1000 эллементов: 0.11798167799999999
    Время затраченое на сортировку списка из 1000 эллементов: 0.09776904800000003
Исходя из данных замеров можно сделать вывод, что добавив возможность выхода из цикла время на ее выполнение немного сократилось
"""
