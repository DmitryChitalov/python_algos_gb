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

from statistics import median
from random import randint, choice
from timeit import timeit


# Использован алгоритм quickselect, разработанный Тони Хоаром
def median_search(input_array, m):
    if len(input_array) == 1:
        return input_array[0]

    pivot = choice(input_array)
    lower_values = [x for x in input_array if x < pivot]
    higher_values = [x for x in input_array if x > pivot]
    pivot_values = [x for x in input_array if x == pivot]

    if m < len(lower_values):
        return median_search(lower_values, m)
    elif m < len(lower_values) + len(pivot_values):
        return pivot_values[0]
    else:
        return median_search(higher_values, m - len(lower_values) - len(pivot_values))


m = 1000
arr = list([randint(-100, 100) for _ in range(2 * m + 1)])
print(arr)
print(f"Результат median_search - {median_search(arr, m)}")
print(f"Результат median - {median(arr)}")

print(
    f"Время median_search - {timeit('median_search(arr, m)', 'from __main__ import arr, m, median_search', number=1000)}")
print(f"Время median - {timeit('median(arr)', 'from __main__ import arr, m, median', number=1000)}")

"""
Результат median_search - 4
Результат median - 4
Время median_search - 10.617405501001485
Время median - 0.18911677199866972

Алгоритм работает верно, однако встроеная функция работает на порядок быстрее. Возможно, следует поэкспериментировать
с выбором опорного элемента для улучшения быстродействия
"""
