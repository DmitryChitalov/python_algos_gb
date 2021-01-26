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

m = int(input('Массив задается формулой 2m + 1, введите m: '))
my_list = [randint(0, 100) for _ in range(2 * m + 1)]


def find_med(obj_list):
    while True:
        left = []
        right = []
        med = obj_list[0]
        for i in range(1, len(obj_list)):
            if obj_list[i] < med:
                left.append(obj_list[i])
            elif obj_list[i] > med:
                right.append(obj_list[i])
            else:
                if len(left) > len(right):
                    right.append(obj_list[i])
                elif len(left) < len(right):
                    left.append(obj_list[i])
                else:
                    left.append(obj_list[i])
        if len(left) == len(right):
            return med
        else:
            temp = obj_list.pop(0)
            obj_list.append(temp)


print(f'Исходный массив: {my_list}')
print(f'Поиск медианы: {find_med(my_list)}')
print(f'Проверка через встроенную функцию: {median(my_list)}')
