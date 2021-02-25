"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random


def merge(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_lst = lst[:mid]
        right_lst = lst[mid:]

        merge(left_lst)
        merge(right_lst)

        i = 0
        j = 0
        k = 0
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i = i + 1
            else:
                lst[k] = right_lst[j]
                j = j + 1
            k = k + 1

        while i < len(left_lst):
            lst[k] = left_lst[i]
            i = i + 1
            k = k + 1

        while j < len(right_lst):
            lst[k] = right_lst[j]
            j = j + 1
            k = k + 1


n = int(input("Input number of elements: "))
v_lst = [random.random() * 50 for i in range(n)]

print(f"Initial list - {v_lst}")
merge(v_lst)
print(f"Sorted list - {v_lst}")
