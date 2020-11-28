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
from random import sample
import timeit
N = 25
my_list_no_sort = sample(range(-100, 100), N)
print(f'Не отсортированный массив - {my_list_no_sort}')


def bubble_sort_de(no_sort_list, N):
    a = no_sort_list.copy()
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


def bubble_sort_de_1(no_sort_list, N):
    a = no_sort_list.copy()
    for i in range(N-1):
        replacements = False
        for j in range(N-i-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                replacements = True
        if not replacements:
            break
    return a

print(f'Отсортированный массив без оптимизации - {bubble_sort_de(my_list_no_sort, N)}')
print(f'Отсортированный массив с оптимизации - {bubble_sort_de_1(my_list_no_sort, N)}')


print(f'Время выполнения без оптимизации - '
      f'{timeit.timeit("bubble_sort_de(my_list_no_sort, N)",setup="from __main__ import bubble_sort_de, my_list_no_sort, N", number=10000)}')
print(f'Время выполнения с оптимизацией - '
      f'{timeit.timeit("bubble_sort_de_1(my_list_no_sort, N)",setup="from __main__ import bubble_sort_de_1, my_list_no_sort, N", number=10000)}')
'''
Не отсортированный массив - [-83, -97, 14, -95, 83, 75, 94, -54, 76, -85, 66, -64, -29, 30, 28, -80, 73, -100, -40, -30, 19, -59, -11, -34, -70]
Отсортированный массив без оптимизации - [94, 83, 76, 75, 73, 66, 30, 28, 19, 14, -11, -29, -30, -34, -40, -54, -59, -64, -70, -80, -83, -85, -95, -97, -100]
Отсортированный массив с оптимизации - [94, 83, 76, 75, 73, 66, 30, 28, 19, 14, -11, -29, -30, -34, -40, -54, -59, -64, -70, -80, -83, -85, -95, -97, -100]
Время выполнения без оптимизации - 1.0337347000000001
Время выполнения с оптимизацией - 0.9171487999999999

Вариант когда оптимизация не помогла 
Не отсортированный массив - [65, -61, -65, 15, 11, -18, -76, -25, 5, -34, 34, 54, -12, 41, 96, 50, -23, -16, -70, 55, -57, 76, 18, 2, 57]
Отсортированный массив без оптимизации - [96, 76, 65, 57, 55, 54, 50, 41, 34, 18, 15, 11, 5, 2, -12, -16, -18, -23, -25, -34, -57, -61, -65, -70, -76]
Отсортированный массив с оптимизации -    [96, 76, 65, 57, 55, 54, 50, 41, 34, 18, 15, 11, 5, 2, -12, -16, -18, -23, -25, -34, -57, -61, -65, -70, -76]

Время выполнения без оптимизации - 1.1524764
Время выполнения с оптимизацией - 1.2056325999999997


Оптимизация дает выйгрыш в количестве шагов в цикле, ведь мы останавливаем цикл если не происходит замены, а вариант
без оптимизации продолжает перебирать дальше. Но как ясно из описания такое происходит не всегда, результаты разнятся. 
Но т.к время когда цикл не останавливается не слишком сильно отличается от времени цикла без оптимизации, то оптимизации имеет место быть
'''