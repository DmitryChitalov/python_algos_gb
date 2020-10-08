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
########################################################################################################################

from random import randint
from statistics import median

med = 2 * int(input('Введите натуральное число: ')) + 1
some_list = []
while len(some_list) < med:
    some_list.append(randint(0, 20))


print(some_list)


def gnome(data):
    i, j, size = 1, 2, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i, j = j, j + 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return data


print(gnome(some_list))
print(median(some_list))
