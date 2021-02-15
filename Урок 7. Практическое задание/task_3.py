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


def get_uint(msg='', err=''):
    while True:
        res = input(('Enter Unsigned Int number: ', msg)[bool(msg)])
        if res != '':
            try:
                res = int(res)
            except ValueError:
                pass
            else:
                return res
        print(('This is not UInt, try again, please!', err)[bool(err)])


_ = get_uint(
    msg='Для массива длиной 2m + 1 введите m (целое положительное число): ',
    err='Требуется ввести целое положительное число!')
arr = [randint(0, 1000) for _ in range(2 * _ + 1)]


def get_median(unsorted_arr):
    m = len(unsorted_arr) // 2
    while len(unsorted_arr) > m + 1:
        unsorted_arr.remove(max(unsorted_arr))
    return max(unsorted_arr)


print(f'Исходный массив: {arr}')
print(f'Решение: {get_median(arr[:])}')
print(f'Проверка: {median(arr[:])}')
