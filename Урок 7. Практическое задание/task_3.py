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
import random


def count_input():
    try:
        return int(input('Введите число элементов:'))
    except:
        print('Вы ввели не целое число')
        return count_input()


def median_finder(source_array, random_fn=random.choice):

    def __inner_fn(l, k, fn):
        if len(l) == 1:
            assert k == 0
            return l[0]
        pin = fn(l)
        lower = [el for el in l if el < pin]
        higher = [el for el in l if el > pin]
        pins = [el for el in l if el == pin]
        if k < len(lower):
            return __inner_fn(lower, k, fn)
        elif k < len(lower) + len(pins):
            return pins[0]
        else:
            return __inner_fn(higher, k - len(lower) - len(pins), fn)

    if len(source_array) % 2 == 1:
        return __inner_fn(source_array, len(source_array) / 2, random_fn)
    else:
        return 0.5 * (__inner_fn(source_array, len(source_array) / 2 - 1, random_fn) +
                      __inner_fn(source_array, len(source_array) / 2, random_fn))


initial_array = list(random.uniform(0, 100) for _ in range(0, count_input()))
print(initial_array)
print(median_finder(initial_array))
