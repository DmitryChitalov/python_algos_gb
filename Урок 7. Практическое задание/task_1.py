"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import random
import timeit


def bubble_sort(orig_list):
    """Стандартный подход"""
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        n += 1
    return orig_list


def bubble_sort_upd(orig_list):
    """Доработанный подход. Если за проход по списку
     не совершается ни одной сортировки, то завершение"""
    n = 1
    k = 0
    while n < len(orig_list):
        for i in range(len(orig_list)-n):
            if orig_list[i] < orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
                k = 1
        if k == 0:
            break
        n += 1
    return orig_list


orig_list = [random.randint(-100, 100) for i in range(100)]
"""Дублирую списки, чтобы каждая функция работала с оригинальным списком
Если так н сделать, то второй запуск будет работать на уже отсортированном списке"""

list_4_v1 = orig_list.copy()
list_4_v2 = orig_list.copy()
print('Initial list for sort')
print(list_4_v1)
print(list_4_v2)

print(timeit.timeit("bubble_sort(list_4_v1)",
                    setup="from __main__ import bubble_sort, list_4_v1", number=100))
print('Lists after 1st  sort')
print(list_4_v1)
print(list_4_v2)
print(timeit.timeit("bubble_sort_upd(list_4_v2)",
                    setup="from __main__ import bubble_sort_upd, list_4_v2", number=100))
print('Lists after 2d  sort')
print(list_4_v1)
print(list_4_v2)

"""

На вход функции попадают точно одинаковые списки. Доработка помогла.
0.026368189
0.0009543600000000013
"""
"""
orig_list = [random.randint(-100, 100) for i in range(100)]
print('Initial list for sort')
print(orig_list)

print(timeit.timeit("bubble_sort(orig_list)",
                    setup="from __main__ import bubble_sort, orig_list", number=100))
print('List after 1st  sort')
print(orig_list)

print(timeit.timeit("bubble_sort_upd(orig_list)",
                    setup="from __main__ import bubble_sort_upd, orig_list", number=100))
"""
