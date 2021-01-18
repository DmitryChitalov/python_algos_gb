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

import timeit
import random


def bubble_sort_reverse(lst_obj):
    #print('Исходный список: ', lst_obj)
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    #print('Итоговый список: ', lst_obj)
    return lst_obj

def bubble_sort_reverse2(lst_obj):
    #print('Исходный список: ', lst_obj)
    n = 1
    flag = True
    while n < len(lst_obj) and flag == True:
        for i in range(len(lst_obj)-n):
            flag = False
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                flag = True
        n += 1
    #print('Итоговый список: ', lst_obj)
    return lst_obj




orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print('Оригинальная функция: ', timeit.timeit("bubble_sort_reverse(orig_list)", \
    setup="from __main__ import bubble_sort_reverse, orig_list", number=1))


orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print('Оригинальная функция: ', timeit.timeit("bubble_sort_reverse(orig_list)", \
    setup="from __main__ import bubble_sort_reverse, orig_list", number=1))

orig_list = [random.randint(-100, 100) for _ in range(10000)]

# замеры 10000
print('Оригинальная функция: ', timeit.timeit("bubble_sort_reverse(orig_list)", \
    setup="from __main__ import bubble_sort_reverse, orig_list", number=1))


orig_list = [random.randint(-100, 100) for _ in range(100)]
print()
# замеры 100
print('Доработанная функция: ', timeit.timeit("bubble_sort_reverse2(orig_list)", \
    setup="from __main__ import bubble_sort_reverse2, orig_list", number=1))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print('Доработанная функция: ', timeit.timeit("bubble_sort_reverse2(orig_list)", \
    setup="from __main__ import bubble_sort_reverse2, orig_list", number=1))

orig_list = [random.randint(-100, 100) for _ in range(10000)]

# замеры 10000
print('Доработанная функция: ', timeit.timeit("bubble_sort_reverse2(orig_list)", \
    setup="from __main__ import bubble_sort_reverse2, orig_list", number=1))

orig_list = [x for x in range(10000, 0, -1)]

print()
print('Оригинальная функция в отсортированном списке: ', timeit.timeit("bubble_sort_reverse(orig_list)", \
    setup="from __main__ import bubble_sort_reverse, orig_list", number=1))

print('Доработанная функция в отсортированном списке: ', timeit.timeit("bubble_sort_reverse2(orig_list)", \
    setup="from __main__ import bubble_sort_reverse2, orig_list", number=1))

# Результаты тестов

'''Оригинальная функция:  0.0004521999999999998
Оригинальная функция:  0.05209069999999999
Оригинальная функция:  5.187055300000001

Доработанная функция:  0.00010560000000037206
Доработанная функция:  0.04553399999999996
Доработанная функция:  5.3980954

Оригинальная функция в отсортированном списке:  2.739151400000001
Доработанная функция в отсортированном списке:  0.0005756999999988466


Как видно из тестов преимущество доработанной функции невелико и всегда меняется 
при проведении новых замеров. Зато в отсортированном 
заранее списке, результаты отличаются более чем в 1000 раз.Это объясняется тем, что
доработанная функция в отсортированном списке делает только один проход'''