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
from random import uniform

source_array = [uniform(0.0, 100.0) for element in range(0, 5)]


def median(array):
    for index in range(0, len(array)):
        left, right = 0, 0
        for count_element in range(0, len(array)):
            if array[index] != array[count_element]:
                if array[index] < array[count_element]:
                    left += 1
                else:
                    right += 1
        if left == right:
            return array[index]


print(f"массив {source_array}\n медиана {median(source_array)}")

