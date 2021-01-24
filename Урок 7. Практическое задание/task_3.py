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

m = int(input("Введите натуральное число: "))
a = [randint(1, 10) for _ in range(2 * m + 1)]

print(f"Исходный список: {a}")
print(f"Медиана списка через функцию median: {median(a)}")


def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

    return seq


def median2(list_obj):
    sorted_list = shell(list_obj[:])

    # return sorted_list[m] # 2-й вариант
    return sorted_list[len(sorted_list) // 2]


print(f"Медиана списка через сортировку Шелла: {median2(a)}")
