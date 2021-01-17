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
import random

arr = [3,4,3,3,5,3,3]
arr_2 = [random.randint(0,100) for _ in range(11)]
left = []
right = []
mediana = 0

def search_median(array : list):
    for i in range(len(arr)):
        left_count = 0
        right_count = 0
        left.clear()
        right.clear()
        for j in range(len(array)):
            if j == i:
                continue
            elif array[j] <= array[i]:
                left.append(array[j])
            elif array[j] >= array[i]:
                right.append(array[j])
        left.extend(right)
        for j in range(len(left)//2):
            if left[j] <= array[i]:
                left_count = left_count + 1
        for j in range(len(left) // 2, len(left)):
            if left[j] >= array[i]:
                right_count = right_count + 1
        if left_count == right_count:
            mediana = array[i]
            break
    print("Медиана найдена и равна: ", mediana)

print(arr)
print(median(arr))  #Для проверки
search_median(arr)

print(arr_2)
print(median(arr_2))
search_median(arr_2)
"""Работа выполнена: 
    1-й прогон программы:
[3, 4, 3, 3, 5, 3, 3]
3
Медиана найдена и равна:  3
[19, 55, 78, 7, 16, 9, 35, 46, 48, 96, 2]
35
Медиана найдена и равна:  35

    2-й прогон программы:
[3, 4, 3, 3, 5, 3, 3]
3
Медиана найдена и равна:  3
[5, 100, 28, 33, 15, 16, 78, 15, 72, 74, 39]
33
Медиана найдена и равна:  33   

Вывод: моя реализация сходится со встроенной ф-й median.
"""