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
from random import randint, choice


# Решение на основе рекурсивного алгоритма quickselect,
# который позволяет находить любой заданный элемент по индексу (не только медиану) без сортировки
def quick_select(array, k):
    if len(array) == 1:
        return array[0]
    base_el = choice(array)
    less = [el for el in array if el < base_el]
    more = [el for el in array if el > base_el]
    bases = [el for el in array if el == base_el]
    if k < len(less):
        return quick_select(less, k)
    elif k < len(less) + len(bases):
        return bases[0]
    else:
        return quick_select(more, k - len(less) - len(bases))


while True:
    try:
        m = int(input('Введите натуральное число m: '))
        if m < 1:
            raise ValueError
    except ValueError:
        print('Ошибка ввода!')
    else:
        arr = [randint(1, 100) for _ in range(2 * m + 1)]
        print(f'Исходный массив:\n{arr}')
        print(f'Медиана statistics: {median(arr)}')
        print(f'Медиана quick_select: {quick_select(arr, m)}')
        break
