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

# Просто поиск медианы
m = int(input('введите длину массива: '))
lst_obj = [random.randint(-100, 100) for i in range(2 * m + 1)]
print(f'исходный массив: {lst_obj}')

while len(lst_obj) != 1:
    lst_obj.remove(max(lst_obj))
    lst_obj.remove(min(lst_obj))

print(f'медиана массива равна: {lst_obj[0]}')

#######################################################

print()
# Поиск медианы с созданием двух списков, с элементами больше и меньше медианы.
lst_obj = [random.randint(-100, 100) for i in range(2 * m + 1)]
print(f'исходный массив: {lst_obj}')

more_median = []
less_median = []
while len(lst_obj) != 1:
    more_median.append(max(lst_obj))
    lst_obj.remove(max(lst_obj))
    less_median.append(min(lst_obj))
    lst_obj.remove(min(lst_obj))

print(f'медиана массива равна: {lst_obj[0]}')
print(f'список элементов больше медианы: {more_median}')
print(f'список элементов меньше медианы: {less_median}')

