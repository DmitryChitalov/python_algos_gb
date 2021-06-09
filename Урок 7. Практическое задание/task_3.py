"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

from random import choice
from random import randint
from statistics import median


#Поиск медианы алгоритмом быстрого выбора

def quickselect_median(inp_arr, pivot_fn=choice):
    if len(inp_arr) % 2 == 1:
        return quickselect(inp_arr, len(inp_arr) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(inp_arr, len(inp_arr) / 2 - 1, pivot_fn) +
                      quickselect(inp_arr, len(inp_arr) / 2, pivot_fn))


def quickselect(inp_arr, k, pivot_fn):
    if len(inp_arr) == 1:
        assert k == 0
        return inp_arr[0]

    pivot = pivot_fn(inp_arr)

    lows = [el for el in inp_arr if el < pivot]
    highs = [el for el in inp_arr if el > pivot]
    pivots = [el for el in inp_arr if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


m = int(input("Ведите число m: "))

test_array = [randint(0, 100) for i in range(m * 2 + 1)]

print(test_array)
print(f'Результат поиска медианы алгоритмом быстрого выбора: {quickselect_median(test_array[:])}')
print(f'Проверяем результат встроенной функцией: {median(test_array)}')
