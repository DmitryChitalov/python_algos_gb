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
from timeit import timeit
from random import randint


# Пузырьковая сортировка по убыванию
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


# Пузырьковая сортировка по убыванию с доработкой
def bubble_sort_2(lst_obj):
    n = 1
    while n < len(lst_obj):
        flag = False
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
        if flag == False:
            break
        n += 1
    return lst_obj


num_list = [randint(-100, 100) for i in range(100)]
print(f'Исходный массив {num_list}')
print(f'Отсортированный массив с помощью функции bubble_sort: {bubble_sort(num_list[:])}')
print(f'Отсортированный массив с помощью функции bubble_sort_2: {bubble_sort_2(num_list[:])}')
print(f"Затраченное время функции bubble_sort: "
      f"{timeit('bubble_sort(num_list[:])','from __main__ import bubble_sort, num_list', number=1000)}")
print(f"Затраченное время функции bubble_sort_2: "
      f"{timeit('bubble_sort_2(num_list[:])', 'from __main__ import bubble_sort_2, num_list', number=1000)}")
print()
# Проверка на почти отсортированном массиве
num_list = [i for i in range(100, 0, -1)]
num_list[0], num_list[1] = num_list[1], num_list[0]
print(f'Исходный массив {num_list}')
print(f'Отсортированный массив с помощью функции bubble_sort: {bubble_sort(num_list[:])}')
print(f'Отсортированный массив с помощью функции bubble_sort_2: {bubble_sort_2(num_list[:])}')
print(f"Затраченное время функции bubble_sort: "
      f"{timeit('bubble_sort(num_list[:])','from __main__ import bubble_sort, num_list', number=1000)}")
print(f"Затраченное время функции bubble_sort_2: "
      f"{timeit('bubble_sort_2(num_list[:])', 'from __main__ import bubble_sort_2, num_list', number=1000)}")

"""
Рандомный массив 100 элементов (от -100 до 100)
Затраченное время функции bubble_sort 1.4986357
Затраченное время функции bubble_sort_2 1.4008893999999998



Почти отсортированный массив 100 элементов (первые 2 элемента поменял местами)
Затраченное время функции bubble_sort 0.7340479000000002
Затраченное время функции bubble_sort_2 0.028506399999999932


Как мы видим сортировка с доработкой работыет намного быстрее, в случае если массив почти отсортирован

П.С. были случаи когда обычная сортировка отрабатывала быстрее, чем с доработкой на доли секунды, такое может быть?
"""