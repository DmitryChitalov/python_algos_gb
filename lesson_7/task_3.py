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
import timeit
import random
from statistics import median

orig_list = [random.randint(0, 100) for _ in range(7)]

# поиск медианы через сортировку стандартную сортировку
orig_list_sorted = sorted(orig_list)

# проверка
med = median(orig_list)

print(f'orig_list        : {orig_list}')
print(f'orig_list_sorted : {orig_list_sorted}')
print(f'median           : {med}')


def shell(data):
    inc = len(data) // 2
    while inc:
        for i, el in enumerate(data):
            while i >= inc and data[i - inc] > el:
                data[i] = data[i - inc]
                i -= inc
            data[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return data


# поиск медианы через сортировку Шелла
shell_list_sorted = shell(orig_list[:])
med_calc = shell_list_sorted[len(shell_list_sorted) // 2]

print(f'shell            : {shell_list_sorted}')
print(f'median calc      : {med_calc}')

# поиск медианы через max
max_list = orig_list.copy()
for i in range(len(orig_list) // 2):
    max_list.remove(max(max_list))

print(f'max_list         : {max_list}')

med_calc_max = max(max_list)
print(f'median calc max  : {med_calc_max}')
