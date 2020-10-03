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
from random import randint
from statistics import median


def med(lst_obj):
    left = []
    right = []
    for i in lst_obj:
        left.clear()
        right.clear()
        for j in lst_obj:
            if j < i:
                left.append(i)
            elif j > i:
                right.append(i)
        for x in range(1, lst_obj.count(i)):
            if len(left) > len(right):
                right.append(i)
            else:
                left.append(i)
        if len(left) == len(right):
            return i


m = 6
arr = [randint(0, 10) for i in range(2 * m + 1)]
print(f'Исходный - {arr}')
print(f'Отсортированный - {sorted(arr)}')
print(f'Медиана = {med(arr)}')
print(f'Проверка = {median(arr)}')
