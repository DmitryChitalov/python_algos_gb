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
import random

my_list = [random.randint(0, 100) for _ in range(21)]


def gnome(data):
    i, size = 1, len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data


print(gnome(my_list))


def my_median(lst):
    n = len(lst)
    m = n // 2
    return lst[m]


print(f'Проверка: {median(my_list)}')
print(f'Медиана: {my_median(my_list)}')
# использовал сортировку Гномья
# пробовал как Вы говорили на уроке, но не вышло(
