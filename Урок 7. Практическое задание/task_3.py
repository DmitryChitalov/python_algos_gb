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


def median_1(array):
    for i in range(len(array)):
        count = 0
        for el in array:
            if array[i] >= el:
                count += 1

        if count == len(array) // 2 + 1:
            return array[i]

    return array[i]


m = int(input("Ведите число :"))

test_array = [randint(0, 100) for i in range(m * 2 + 1)]

print(test_array)
print(
    f"Используем встроенную функцию для нахождения медианы : {median(test_array)}"
)
print(f"Используем метод подсчета : {median_1(test_array)}")
