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
from random import randrange
from statistics import median

m = int(input('chislo'))
massive = [randrange(-100, 100) for i in range(2*m+1)]
print(massive)

print('Решение встроенной функцией', median(massive))

#Решение моей фукнцией

def mediana(array):
    middle = len(array)/2
    while middle > 0.5:
        array.pop(array.index(max(array)))
        middle-=1
    return max(array)
print(mediana(massive))
