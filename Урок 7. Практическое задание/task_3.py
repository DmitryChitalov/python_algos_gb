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
from random import randint
from timeit import timeit

random_list = [randint(0, 10) for _ in range(9)]


def find_median(in_list: list):
    # Без сортировки
    while len(in_list) != 1:
        in_list.pop(in_list.index(min(in_list)))
        in_list.pop(in_list.index(max(in_list)))
    return in_list[0]


print(f'Исходный массив: {random_list}')
print(f'Медиана от встроенной функции: {median(random_list)}')
print(f'Медиана от кастомной функции: {find_median(random_list[:])}')
print(f'Отсортированный массив: {sorted(random_list)}')

print(f'Время выполнения встроенной функции: '
      f'{timeit(f"median({random_list})", setup="from statistics import median", number=10000)}')
print(f'Время выполнения кастомной функции: '
      f'{timeit(f"find_median({random_list})", setup="from __main__ import find_median", number=10000)}')

"""
Время выполнения встроенной функции: 0.009680699999999987
Время выполнения кастомной функции: 0.06809379999999998

Вывод: кастомная функция выполняется хоть и без сортировки, но все равно намного медленнее чем встроенная функция
(в ~7 раз)
"""