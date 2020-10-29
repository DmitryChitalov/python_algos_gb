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


def search_median(inp_lst):
    while len(inp_lst) != 1:
        inp_lst.pop(inp_lst.index(min(inp_lst)))
        inp_lst.pop(inp_lst.index(max(inp_lst)))
    return inp_lst[0]


inp_lst = [randint(0, 33) for _ in range(33)]
print(f'{inp_lst}')
print(f'{sorted(inp_lst)}')
print(f'{median(inp_lst)}')
print(f'{search_median(inp_lst[:])}')
# Вывод: Задача решена без сортировки двумя способами:
# 1) Встроенная функция библиотеки statistics;
# 2) Функция, в основе которой лежит извлечени min и max
# элементов массива до тех пор пока не останеться 1 элемент
# со средним значением
