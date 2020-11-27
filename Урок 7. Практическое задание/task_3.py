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

list_1 = [randint(1, 50) for i in range((2 * randint(1, 15)) + 1)]


# способ без сортировки:
def func_1(array):
    array_len = len(array)
    if array_len % 2 > 0:
        for i in range(array_len):
            left, right, center = [], [], []  # "Центральный" список служит для отбора элементов равных i,
            for j in range(array_len):        # это особенно помогает, если их больше одного.
                if array[i] > array[j]:
                    left.append(array[j])
                elif array[i] < array[j]:
                    right.append(array[j])
                else:
                    center.append(array[i])

            # равномерное распределение одинаковых исходных элементов по левому и правму спискам:
            while len(center) > 1:
                if len(left) == len(right) and (len(center) - 1) % 2 == 0:
                    break
                elif len(left) > len(right):
                    right.append(center.pop(-1))
                elif len(right) > len(left):
                    left.append(center.pop(-1))

            if len(left) == len(right):
                print(f'Медиана в этом массиве равна {array[i]}.')
                break
            # print(left, right)
    else:
        print('Массив чётной длины!')


# Гномья сортировка и нахождение медианы:
def gnome_way(array):
    i, array_len = 1, len(array)
    if array_len % 2 > 0:
        while i < array_len:
            if array[i - 1] <= array[i]:
                i += 1
            else:
                array[i - 1], array[i] = array[i], array[i - 1]
                if i > 1:
                    i -= 1
        print(f'Медиана в этом массиве равна {array[(array_len - 1) // 2]}.')
    else:
        print('Массив чётной длинны!')


# Сортировка Шелла и нахождение медианы:
def shell_sort(array):
    array_len = len(array)
    gap = array_len // 2
    if array_len % 2 > 0:
        while gap > 0:
            for i in range(gap, array_len):
                temp, j = array[i], i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        print(f'Медиана в этом массиве равна {array[(array_len - 1) // 2]}.')
    else:
        print('Массив чётной длинны!')


print(f'Исходный массив: {list_1}')
func_1(list_1)
# gnome_way(list_1)
# shell_sort(list_1)
print(f'Проверка через функцию median: {median(list_1)}.')
