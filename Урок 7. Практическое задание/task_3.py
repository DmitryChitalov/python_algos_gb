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
m = int(input('Введите натуральное число: '))


def shell_sort(lst_obj):  # сортировка Шелла
    print(f'Исходный список: {lst_obj}')
    last_index = len(lst_obj) - 1
    step = len(lst_obj) // 2
    while step > 0:
        for i in range(step, last_index + 1, 1):
            j = i
            delta = j - step
            while delta >= 0 and lst_obj[delta] > lst_obj[j]:
                lst_obj[delta], lst_obj[j] = lst_obj[j], lst_obj[delta]
                j = delta
                delta = j - step
        step //= 2
    print(f'Отсортированный список: {lst_obj}')
    print(f'Медиана массива = {lst_obj[m]}')
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(2 * m + 1)]

shell_sort(orig_list)
print(f'Проверка: {median(orig_list)}')