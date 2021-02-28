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


def gnome(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


m = int(input("Введите натуральное число: "))

array = [randint(0, 100) for _ in range(2 * m + 1)]

print(f'Массив до гномьей сортировки: {array}')
gnome(array)
print(f'Массив после гномьей сортировки: {array}')

mediana = median(array)
print(f'Медиана массива равна: {mediana}')

