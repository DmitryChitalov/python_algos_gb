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
import timeit
import random

arrays = [
    [1, 2, 3, 3, 3],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 2],
    [0, 1, 1, 3, 3],
]


def median_1(inp_arr):  # способ без сортировки
    for _ in range(int((len(inp_arr) - 1) / 2)):
        inp_arr.remove(max(inp_arr))
        inp_arr.remove(min(inp_arr))
    return inp_arr[0]


def median_shell_sort(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data[int((len(data) - 1) / 2)]


def median_sorted(data):
    return sorted(data)[int((len(data) - 1) / 2)]


for arr in arrays:
    print(median_1(arr) == median(arr) == median_shell_sort(arr))

random_list = [random.randint(-100, 100) for _ in range(100)]
print(timeit.timeit("median_1(random_list[:])", globals=globals(), number=10000))  # 1.77
print(timeit.timeit("median_shell_sort(random_list[:])", globals=globals(), number=10000))  # 2.02
print(timeit.timeit("median(random_list[:])", globals=globals(), number=10000))  # 0.03806740
print(timeit.timeit("median_sorted(random_list[:])", globals=globals(), number=10000))  # 0.03805369

'''можно предположить, что функция median из модуля statistics использует быструю сортировку
для поиска медианы'''
