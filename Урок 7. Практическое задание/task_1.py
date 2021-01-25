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

array = [randint(-100, 100) for _ in range(100)]


def bubble_sort(list_obj):
    n = 1
    while n < len(list_obj):
        for i in range(len(list_obj) - n):
            if list_obj[i] < list_obj[i + 1]:
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
        n += 1
    return list_obj


def bubble_sort_update(list_obj):
    n = 1
    sort_fact = 0
    while n < len(list_obj):
        for i in range(len(list_obj) - n):
            if list_obj[i] < list_obj[i + 1]:
                list_obj[i], list_obj[i + 1] = list_obj[i + 1], list_obj[i]
                sort_fact = 1
        if sort_fact == 0:
            break
        n += 1
    return list_obj


print(f"Оригинальная функция:\
{timeit('bubble_sort(array[:])', setup='from __main__ import bubble_sort, array', number=1000)}")

print(f"Оптимизированная функция:\
{timeit('bubble_sort_update(array[:])', setup='from __main__ import bubble_sort_update, array', number=1000)}")

'''
Оригинальная функция:0.3128142
Оптимизированная функция:0.006264400000000003
Вывод: оптимизация существенно повысила эффективность выполнения программы
'''
