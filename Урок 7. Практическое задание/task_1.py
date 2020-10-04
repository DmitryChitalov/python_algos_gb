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


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    print(lst_obj)

def bubble_2(lst_obj):
    for i in range(len(lst_obj)-1):
        if lst_obj[i] > lst_obj[i+1]:
            break
        for j in range(len(lst_obj)-i-1):
            if lst_obj[j] < lst_obj[j+1]:
                lst_obj[j], lst_obj[j+1] = lst_obj[j+1], lst_obj[j]
    print(lst_obj)

my_list = [randint(-100, 100) for _ in range(15)]
#my_list = [99, 87, 76, 73, 70, 68, 63, 61, 45, 35, 21, 5]
print(my_list)
bubble_sort(my_list)
bubble_2(my_list)
print(timeit('bubble_sort', setup='from __main__ import bubble_sort, my_list'))
print(timeit('bubble_2', setup='from __main__ import bubble_2, my_list'))

#У меня получилось, что вторая функция(bubble_2) отрабатывает быстрее первой(bubble_sort)
#в обоих случаях(рандомный список / и отсортированный)
#[69, 33, -33, -12, -60, -56, -98, 95, -57, -91, 68, 90, 92, 17, -25]
#[95, 92, 90, 69, 68, 33, 17, -12, -25, -33, -56, -57, -60, -91, -98]
#[95, 92, 90, 69, 68, 33, 17, -12, -25, -33, -56, -57, -60, -91, -98]
#0.031086799999999998
#0.029687100000000008