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
import copy

""" 1  """
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
new_list = copy.copy(orig_list)
print(orig_list, bubble_sort(new_list))

""" 2 """
def bubble_sort_dop(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1):
            if lst_obj[i] > lst_obj[i+1]:
                break
            elif lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]      
        n += 1
    return lst_obj


check_list = [52, 34, 25, -6, -25, -28, -29, -34, -74, -88]
orig_lists = [random.randint(-100, 100) for _ in range(10)]
new_lists = copy.copy(check_list)
new_list_3 = copy.copy(orig_lists)
print(check_list, bubble_sort_dop(new_lists))
print(orig_lists, bubble_sort_dop(orig_lists))

""" Функция bubble_sort(lst_obj) """
# замеры 10
orig_list = [random.randint(-100, 100) for _ in range(10)]
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1))  #1.882699999999904e-05

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1)) #0.15547799899999998

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list)", \
    setup="from __main__ import bubble_sort, orig_list", number=1)) #0.126101099

""" Функция bubble_sor_dop(lst_obj) """
# замеры 10
orig_lists = [random.randint(-100, 100) for _ in range(10)]

print(timeit.timeit("bubble_sort_dop(orig_lists)", \
    setup="from __main__ import bubble_sort_dop, orig_lists", number=1)) #8.8820000000156e-06

orig_lists = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort_dop(orig_lists)", \
    setup="from __main__ import bubble_sort_dop, orig_lists", number=1)) #4.6258999999992945e-05

orig_lists = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort_dop(orig_lists)", \
    setup="from __main__ import bubble_sort_dop, orig_lists", number=1)) #0.0006986349999999752



""" По результатам замеров двух функций можно увидеть, что доработанный вариант функции, выполняет действие намного дольше. """


