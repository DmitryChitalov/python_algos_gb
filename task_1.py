"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""

"""
Доработка алгоритма заключается в добавлении флага на проверку изменения последовательности.
Скорость выполнения модифицированного алгоритма значительно выросла, и стала лишь в два (примерно) раза медленее 
встроенной функции sorted. Оъяснить эту магию я не смог.
"""

import timeit
import random


def buble_sort(lst):
    count = 1
    while count < len(lst):
        for i in range(len(lst) - count):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        count += 1
    return lst


def buble_sort_mod(lst):
    count = 1
    flag = False
    while count < len(lst):
        for i in range(len(lst) - count):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                flag = True
        if flag == False:
            return lst
        count += 1
    return lst


arr = [random.randint(-100, 100) for _ in range(100)]
print(arr)
print(buble_sort(arr))
print(timeit.timeit('buble_sort(arr)', globals=globals(), number=1000))

arr = [random.randint(-100, 100) for _ in range(100)]
print(arr)
print(buble_sort_mod(arr))
print(timeit.timeit('buble_sort_mod(arr)', globals=globals(), number=1000))

arr = [random.randint(-100, 100) for _ in range(100)]
print(arr)
print(sorted(arr, reverse=True))
print(timeit.timeit('sorted(arr)', globals=globals(), number=1000))
