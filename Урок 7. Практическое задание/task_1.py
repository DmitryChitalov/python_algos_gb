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
from random import randint
from timeit import timeit


def bubble_sort_mod(array):
    for j in range(len(array)):
        swap = 0
        for i in range(len(array) - j - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = 1
        if swap == 0:
            break
    return array


def bubble_sort(array):
    for j in range(len(array)):
        for i in range(len(array) - j - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


rand_array = [randint(-100, 100) for i in range(100)]
print(rand_array)
print(bubble_sort(rand_array[:]))
print(timeit("bubble_sort(rand_array[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_mod(rand_array[:])", globals=globals(), number=1000))


rand_array = [randint(-100, 100) for i in range(1000)]

print(timeit("bubble_sort(rand_array[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_mod(rand_array[:])", globals=globals(), number=1000))


# Доработал алгоритм, добавил выход если за проход не было перестановок.
# По замерам данная "доработка" преймущества не дает.
# 0.7841395
# 0.6920742000000001
# 78.8818797
# 82.0807847
