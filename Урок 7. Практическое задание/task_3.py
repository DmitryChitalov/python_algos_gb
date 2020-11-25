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

"""
import random
import statistics
import numpy as np

a = random.randint(5, 20)
size = 2 * a + 1
ar = [random.randint(0, 100) for i in range(size)]
print(ar)
#1
print(statistics.median(ar))
#2
a = np.array(ar)
median_value = np.percentile(a, 50)
print(median_value)
#3
b = sum(ar) / len(ar)
print(b)
left = []
right = []
for i in range(len(ar)):
    if ar[i] > b:
        right.append(ar[i])
    else:
        left.append(ar[i])
c = (max(left))

d = (min(right))

print(max(left))
print(min(right))
print(1 - c / b)
print(d % b)
if (1 - c / b) > d % b or d / b == 1:
    print(d)
else:
    print(c)

''' Третий способ с математической точки зрения более точный, чем метод statistics.median, при этом совершенно
странно, что их результаты переодически не совпадают'''
