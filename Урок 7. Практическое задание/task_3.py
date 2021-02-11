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

m = randint(50, 100)

array = [randint(-1000, 1000) for _ in range(2 * m + 1)]

print(array)
print(median(array))  # 1 способ

for i in range(m):  # 2 способ
    array.pop(array.index(min(array)))
    # print(array)

print(min(array))

"""
Вы изменили список, но забыли поменять m, который отвечает за её длину, способ верен)
Если взять array = [3, 4, 5, 3, 3]
m = 2
и приписать в цикле print(array), то вывод будет таким:\

[3, 4, 5, 3, 3]
3
[4, 5, 3, 3]
[4, 5, 3]
3
"""
