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
from timeit import timeit
from random import randint


def bubble_sort1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort2(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = True
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = False
        if flag:
            return lst_obj
        n += 1
    return lst_obj


orig_list = [randint(-100, 100) for _ in range(10)]
print(f'Оригинальный список:  \n{orig_list}')
print(f'Список, отсортированный методом "пузырька" в порядке убывания без доработки: \n{bubble_sort1(orig_list)}')
print(f'Список, отсортированный методом "пузырька" в порядке убывания после доработки: \n{bubble_sort2(orig_list)}')

# замеры 10
print('Замеры функции без доработки:')
print(
    timeit(
        "bubble_sort1(orig_list[:])",
        globals=globals(),
        number=1000))

print('Замеры функции после доработки:')
print(
    timeit(
        "bubble_sort2(orig_list[:])",
        globals=globals(),
        number=1000))

