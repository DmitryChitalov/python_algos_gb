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


def bubble_sort_original(lst_obj):
    """ 'оригинальный' пример из урока """
    n = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-1, n, -1):
            if lst_obj[i] < lst_obj[i-1]:
                lst_obj[i], lst_obj[i-1] = lst_obj[i-1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_recursion(lst_obj, n=0, flag = True):
    """ рекурсия """
    if n == len(lst_obj):
        return lst_obj
    else:
        for i in range(len(lst_obj)-1, n, -1):
            if lst_obj[i] < lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
                flag = flag and False
        if flag:
            return lst_obj
        return bubble_sort_recursion(lst_obj, n+1, flag)


def bubble_sort_modify(lst_obj):
    """ модифицированный вариант """
    for n in range(0, len(lst_obj) - 1):
        flag = True
        for i in range(len(lst_obj)-1, n, -1):
            if lst_obj[i] < lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
                flag = flag and False
        if flag:
            del n, flag
            return lst_obj
    del n, flag
    return lst_obj


def original(test_list):
    return bubble_sort_original(test_list)


def recursion(test_list):
    return bubble_sort_recursion(test_list)


def modify(test_list):
    return bubble_sort_modify(test_list)


my_list = [randint(-100, 100) for x in range(10)]
my_list2 = sorted(my_list)  # отсортированный массив
print(f'Изначальный массив {my_list}')


print(f'результат: {original(my_list[:])} (оригинал): ', end="")
print(timeit("original(my_list[:])", setup="from __main__ import original, my_list", number=100))

print(f'результат: {recursion(my_list[:])} (рекурсия): ', end="")
print(timeit("recursion(my_list[:])", setup="from __main__ import recursion, my_list", number=100))

print(f'результат: {modify(my_list[:])} (улучшенный): ', end="")
print(timeit("modify(my_list[:])", setup="from __main__ import modify, my_list", number=100))

print(f'\nОтсортированный {my_list2}')

print(f'результат: {original(my_list2)} (оригинал): ', end="")
print(timeit("original(my_list2)", setup="from __main__ import original, my_list2", number=100))

print(f'результат: {recursion(my_list2)} (рекурсия): ', end="")
print(timeit("recursion(my_list2)", setup="from __main__ import recursion, my_list2", number=100))

print(f'результат: {modify(my_list2)} (улучшенный): ', end="")
print(timeit("modify(my_list2)", setup="from __main__ import modify, my_list2", number=100))


""" Изначальный массив [37, -18, 88, 1, 63, 59, -48, -20, 27, 10]
    результат: [-48, -20, -18, 1, 10, 27, 37, 59, 63, 88] (оригинал):   0.00292
    результат: [-48, -20, -18, 1, 10, 27, 37, 59, 63, 88] (рекурсия):   0.00315
    результат: [-48, -20, -18, 1, 10, 27, 37, 59, 63, 88] (улучшенный): 0.00203 <-
    
    Отсортированный [-48, -20, -18, 1, 10, 27, 37, 59, 63, 88]
    результат: [-48, -20, -18, 1, 10, 27, 37, 59, 63, 88] (оригинал):   0.00144
    результат: [-48, -20, -18, 1, 10, 27, 37, 59, 63, 88] (рекурсия):   0.00021 <-
    результат: [-48, -20, -18, 1, 10, 27, 37, 59, 63, 88] (улучшенный): 0.00027
    
    Вывод: установив условие, "завершить вычисления, если за полный проход по элементам перестановок не было",
    мы можем существенно сократить количество итераций, что в свою очередь уменьшит временные затрады на вычисления.
    Следовательно, условия, обеспечивающие досрочный выход из цикла - мощный инструмент оптимизации.
    
    Из-за временных затрат на вызов стека рекурсия выполняется дольше всех.
    Быстрее всех она отработает с уже упорядоченным списком, что не имеет смысла в данной задаче.
"""



