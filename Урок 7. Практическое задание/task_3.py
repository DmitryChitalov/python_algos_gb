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
from statistics import median

def gnome(list):
    i, size = 1, len(list)
    while i < size:
        if list[i - 1] <= list[i]:
            i += 1
        else:
            list[i - 1], list[i] = list[i], list[i - 1]
            if i > 1:
                i -= 1
    return list

def func_median(list):
    gnome(list)
    return list[m]

m = int(input('Введите число для построения массива размером 2m+1: '))
num_list = [random.randint(1, 10) for _ in range(2 * m +1)]
print(num_list)
print('Медиана массива: ', func_median(num_list[:]))
print(median(num_list))

