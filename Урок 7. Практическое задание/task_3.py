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


def gnome_sort(a):
    i = 0
    j = 1
    while i < len(a):
        if a[i - 1] < a[i]:
            i = j
            j += 1
        else:
            a[i - 1], a[i] = a[i], a[i - 1]
            i -= 1
            if i == 0:
                i = j
                j += 1
    return a


m = int(input('Введите целое число: '))
arr = [randint(0, 1000) for i in range(2 * m + 1)]
print(arr)
print('Эталонное значение медианы:', median(arr))
arr = gnome_sort(arr)
print(arr)
print('Медиана: ', arr[m])

