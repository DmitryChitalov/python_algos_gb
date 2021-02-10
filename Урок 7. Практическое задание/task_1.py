"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

import timeit
import random

"""Сортировка пузырьком по возрастанию"""


def bubble_sort1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


"""
Cортировка пузырьком по убыванию
Просто поменяли знак > на <
"""


def bubble_sort2(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


"""
Cортировка пузырьком по убыванию с оптимизацией

n - это переменная, которая позволяет работать с range и не выходить за диапазон массива.
Т.е мы исключаем ошибку list out of range
Если len = 10, то range должен быть range(9), т.к от 0 до 9 будет 10 цифр.
Поэтому мы пишем range(len(lst_obj) - n)

Мы берем копию списка каждый number в timeit, иначе список первый раз отсортируется и затем тест
будет проходить по уже отсортированному списку. Значения конечно же будут иные и неверные.

Оптимизация:
Базовый алгоритм меняет значения местами, если одно значение больше/меньше другого.
Я добавил swap, который изначально равен 0.
Если значения  меняются местами, то  swap +=1
Когда swap останется равен 0, то алгоритм остановится


"""


def bubble_sort3(lst_obj):
    n = 1
    while n < len(lst_obj):
        swap = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                swap = True

        n += 1
        if not swap:  # если за проход по списку не совершается ни одной сортировки, то завершение.
            break

    return lst_obj


#
# orig_list = [random.randint(-100, 100) for _ in range(7)]
# print('orig list ', orig_list)
# print('отсортированный лист по убыванию c оптимизацией', bubble_sort3(orig_list))


# замеры 10
orig_list10 = [random.randint(-100, 100) for _ in range(10)]
print('Сортировка пузырьком по возрастанию',
    timeit.timeit(
        "bubble_sort1(orig_list10[:])",
        globals=globals(),
        number=1000))

print('Cортировка пузырьком по убыванию',
    timeit.timeit(
        "bubble_sort2(orig_list10[:])",
        globals=globals(),
        number=1000))

print('Cортировка пузырьком по убыванию с оптимизацией',
    timeit.timeit(
        "bubble_sort3(orig_list10[:])",
        globals=globals(),
        number=1000))

# # замеры 100
orig_list100 = [random.randint(-100, 100) for _ in range(100)]
print('Сортировка пузырьком по возрастанию',
    timeit.timeit(
        "bubble_sort1(orig_list100[:])",
        globals=globals(),
        number=1000))

print('Cортировка пузырьком по убыванию',
    timeit.timeit(
        "bubble_sort2(orig_list100[:])",
        globals=globals(),
        number=1000))

print('Cортировка пузырьком по убыванию с оптимизацией',
    timeit.timeit(
        "bubble_sort3(orig_list100[:])",
        globals=globals(),
        number=1000))

# # замеры 1000
orig_list1000 = [random.randint(-100, 100) for _ in range(1000)]
print('Сортировка пузырьком по возрастанию',
    timeit.timeit(
        "bubble_sort1(orig_list1000[:])",
        globals=globals(),
        number=1000))

print('Cортировка пузырьком по убыванию',
    timeit.timeit(
        "bubble_sort2(orig_list1000[:])",
        globals=globals(),
        number=1000))

print('Cортировка пузырьком по убыванию с оптимизацией',
    timeit.timeit(
        "bubble_sort3(orig_list1000[:])",
        globals=globals(),
        number=1000))

"""
---10---
по возрастанию         0.005886100000000002
по убыванию            0.005672199999999999
по убыванию с оптимиз. 0.006210400000000001

---100---
по возрастанию         0.38355819999999996
по убыванию            0.36154060000000005
по убыванию с оптимиз. 0.39677699999999994

---1000---
по возрастанию         46.593054099999996
по убыванию            45.3470438
по убыванию с оптимиз. 49.613648299999994

---3000---
по возрастанию         446.8110442
по убыванию            440.5278936
по убыванию с оптимиз. 473.13869980000004

Вывод: оптимизация не дала результата, только ухудшила.
"""

print('оригинальный массив', orig_list10)
print('сортировка по возрастанию', bubble_sort1(orig_list10))
print('сортировка по убыванию', bubble_sort2(orig_list10))
print('сортировка по убыванию с оптимизацией', bubble_sort3(orig_list10))
