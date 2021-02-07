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
import timeit

# Функция взята из урока для проведения замеров

def bubble_sort_1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj

# Функция из урока доработана

def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        was_changed = False
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                was_changed = True
        if not was_changed:
            break
        else:
            n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]

print('Исходный массив (10): ',orig_list)
print('Отсортированный массив (10): ',bubble_sort_2(orig_list))

print('Замер bubble_sort_1 (10): ',
      timeit.timeit("bubble_sort_1(orig_list[:])", globals=globals(), number=1000))

print('Замер bubble_sort_2 (10): ',
      timeit.timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

print('Замер bubble_sort_1 (100): ',
      timeit.timeit("bubble_sort_1(orig_list[:])", globals=globals(), number=1000))

print('Замер bubble_sort_2 (100): ',
      timeit.timeit("bubble_sort_2(orig_list[:])", globals=globals(), number=1000))

"""
Результаты замеров:
Замер bubble_sort_1 (10):  0.007691299999999998
Замер bubble_sort_2 (10):  0.0013231000000000007
Замер bubble_sort_1 (100):  0.9859242
Замер bubble_sort_2 (100):  1.048932
Оптимизация дала положительный результат, но только в случае, 
если исходный массив приближен к уже отсортированному (как в примере с массивом 10)
Если массив, не приближен к отсортированному (как в примере 100), 
то в функции 2 наблюдается увеличение времени. 
"""


