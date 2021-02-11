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


def bubble_sort_optimized(lst_obj):
    list_copy = lst_obj.copy()
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        if list_copy == lst_obj:
            return lst_obj
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for i in range(50)]
print(f'оригинальный список {orig_list}')
print("______оригинальный вариант_________")
print(timeit("bubble_sort(orig_list)", globals=globals(), number=1000))
print(f'отсортированный список {bubble_sort(orig_list)}')
print("___________________________________")
print("______доработанный вариант_________")
print(timeit("bubble_sort_optimized(orig_list)", globals=globals(), number=1000))
print(f'отсортированный список {bubble_sort_optimized(orig_list)}')


"""
Доработка помогла, программа стала работать значительно быстрее за счет невыполнения "пустых" циклов
"""
