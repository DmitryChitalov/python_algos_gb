"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
from timeit import timeit


random_list = [random.randint(-100, 100) for _ in range(10)]


def decr_bubble_sort(input_list):

    n = 1
    while n < len(input_list):
        for i in range(len(input_list) - n):
            if input_list[i] < input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
        n += 1
    return input_list


def decr_bubble_sort_modify(input_list):
    n = 1
    flag = 0
    while n < len(input_list):
        for i in range(len(input_list) - n):
            if input_list[i] < input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                flag += 1
        if flag == 0:
            print('This list is already sorted)')
            break
        n += 1
    return f'{input_list},\nThis list has been sorted for {flag + 1} iterations'


print(timeit("decr_bubble_sort(random_list[:])", globals=globals(), number=1000))
print(timeit("decr_bubble_sort_modify(random_list[:])", globals=globals(), number=1000))
print(random_list)
print(decr_bubble_sort_modify(random_list))
print(decr_bubble_sort_modify([3, 2, 1]))


""""
0.025895600000000005
0.030724600000000005

[92, 71, 70, 69, 60, 30, -31, -35, -35, -58],
This list has been sorted for 25 iterations
This list is already sorted)
[3, 2, 1],
This list has been sorted for 1 iterations
"""

random_list = [random.randint(-100, 100) for _ in range(100)]

# print(timeit("decr_bubble_sort(random_list[:])", globals=globals(), number=1000))
# print(timeit("decr_bubble_sort_modify(random_list[:])", globals=globals(), number=1000))
# print(decr_bubble_sort_modify(random_list))

"""
2.2127535999999997
2.3446428000000004 
[100, 97, 95, 89, 82, 80, 80, 79, 78, 72, 71, 62, 61, 58, 57, 56, 55, 54, 
51, 50, 50, 45, 41, 40, 38, ... , -77, -80, -81, -81, -82, -89, -92, 
-92, -95, -95, -97, -99],
 This list has been sorted for 2495 iterations """

random_list = [random.randint(-100, 100) for _ in range(1000)]

# print(timeit("decr_bubble_sort(random_list[:])", globals=globals(), number=1000))
# print(timeit("decr_bubble_sort_modify(random_list[:])", globals=globals(), number=1000))
# print(decr_bubble_sort_modify(random_list))

"""
213.986287 
233.44219349999997
[100, 100, 100, 100, 100, 99, 99, 98, 98, 98, 98, 98, 98, 97, 97, 97, 97, 97, 96, 
96, 96, 96, 95, 95, 95, 95, 95, 95, 95, 94, 94, 94, 93, 93, 93, 93, 93, 92, 92, 92, 91, 91, 91, 91, 91, 91, 91, 90, 
90, 90, 90, 90, 89, 89, 89, 89, ... , -100, -100], 
This list has been sorted for 251591 iterations 

Выводы:
Модификация алгоритма (если за проход по списку не совершается ни одной сортировки, то завершение) в данной задаче 
бесполезна, так как входной массив у нас создается случайным образом, вероятность идеального случая стремится к нулю 
при увеличении длины списка. Разница во времени обусловлена случайной величиной проходов по списку, то есть разница
незнаительна.
"""
