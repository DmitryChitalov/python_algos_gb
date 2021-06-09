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


def bubble_sort(inp_arr):
    for j in range(len(inp_arr)):
        for i in range(len(inp_arr) - j - 1):
            if inp_arr[i] < inp_arr[i + 1]:
                inp_arr[i], inp_arr[i + 1] = inp_arr[i + 1], inp_arr[i]
    return inp_arr


def bubble_sort_mod(inp_arr):
    for j in range(len(inp_arr)):
        swap = False
        for i in range(len(inp_arr) - j - 1):
            if inp_arr[i] < inp_arr[i + 1]:
                inp_arr[i], inp_arr[i + 1] = inp_arr[i + 1], inp_arr[i]
                swap = True
        if not swap:
            break
    return inp_arr


rand_array = [randint(-100, 100) for i in range(100)]

print(rand_array)
print(bubble_sort(rand_array[:]))
print(rand_array)
print(bubble_sort_mod(rand_array[:]))

print(timeit("bubble_sort(rand_array[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_mod(rand_array[:])", globals=globals(), number=1000))

rand_array = [randint(-100, 100) for i in range(1000)]

print(timeit("bubble_sort(rand_array[:])", globals=globals(), number=1000))
print(timeit("bubble_sort_mod(rand_array[:])", globals=globals(), number=1000))


#Добавлен флаг для проверки, производилась ли перестановка, модификация прироста в скорости не дала
#0.5245647999999999
#0.5074205
#61.157384300000004
#62.9342086
