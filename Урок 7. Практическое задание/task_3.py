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


def sort_alg(_list):
    for i in _list:
        _left = [el for el in _list if el < i]
        _right = [el for el in _list if el > i]
        if _list.count(i) > 1:
            if len(_left) < len(_right):
                for el in range(_list.count(i) - 1):
                    _left.append(i)
                if len(_left) == len(_right):
                    return i
            elif len(_left) > len(_right):
                for el in range(_list.count(i) - 1):
                    _right.append(i)
                if len(_left) == len(_right):
                    return i
        if len(_left) == len(_right):
            return i


m = int(input('Введите любое чётное число: '))
orig_list = [randint(0, 100) for el in range(2 * m + 1)]


print(f'Проверка через модуль: {median(orig_list)}')
print(f'Мой результат: {sort_alg(orig_list)}')
