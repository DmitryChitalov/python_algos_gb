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

from random import randint
from timeit import timeit



def bubble_sort(lst):
    n = 1

    while n < len(lst):
        count = 0

        for i in range(len(lst) - 1 - (n - 1)):
            # print((len(lst) - 1 - (n - 1)))

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1

        if count == 0:
            break

        n += 1


# Замеры:

array = [randint(-100, 100) for _ in range(10)]

print(f'Массив до сортировки: {array}')
bubble_sort(array)
print(f'Массив после сортировки: {array}')

# замеры 10
print(f'Замеры 10: {timeit("bubble_sort(array[:])", globals=globals(), number=1000)}')

array = [randint(-100, 100) for _ in range(100)]
print(f'Массив до сортировки: {array}')
bubble_sort(array)
print(f'Массив после сортировки: {array}')

# замеры 100
print(f'Замеры 100: {timeit("bubble_sort(array[:])", globals=globals(), number=1000)}')

array = [randint(-100, 100) for _ in range(1000)]
print(f'Массив до сортировки: {array}')
bubble_sort(array)
print(f'Массив после сортировки: {array}')

# замеры 1000
print(f'Замеры 1000: {timeit("bubble_sort(array[:])", globals=globals(), number=1000)}')

print(f'\n___________________________________без доработки__________________________________________\n')


def bubble_sort(lst):
    n = 1

    while n < len(lst):

        for i in range(len(lst) - 1 - (n - 1)):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

        n += 1


# Замеры:

array = [randint(-100, 100) for _ in range(10)]
print(f'Массив до сортировки: {array}')
bubble_sort(array)
print(f'Массив после сортировки: {array}')

# замеры 10
print(f'Замеры 10: {timeit("bubble_sort(array[:])", globals=globals(), number=1000)}')

array = [randint(-100, 100) for _ in range(100)]
print(f'Массив до сортировки: {array}')
bubble_sort(array)
print(f'Массив после сортировки: {array}')

# замеры 100
print(f'Замеры 100: {timeit("bubble_sort(array[:])", globals=globals(), number=1000)}')

array = [randint(-100, 100) for _ in range(1000)]
print(f'Массив до сортировки: {array}')
bubble_sort(array)
print(f'Массив после сортировки: {array}')

# замеры 1000
print(f'Замеры 1000: {timeit("bubble_sort(array[:])", globals=globals(), number=1000)}')

"""
Замеры с доработкой:
Если за проход по списку не совершается ни одной сортировки, массив считается отсортированным 
и лишних действий не соврешается. 

Замеры 10: 0.0017928470000000002
Замеры 100: 0.009679753999999999
Замеры 1000: 0.10166877299999999


Замеры без доработки:

Замеры 10: 0.007588240999999996
Замеры 100: 0.7900359160000001
Замеры 1000: 49.263451687

"""
