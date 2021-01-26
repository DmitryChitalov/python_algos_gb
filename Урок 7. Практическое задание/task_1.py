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


orig_list = [random.randint(-100, 100) for _ in range(10)]


def bubble_sort_elaborated(lst_obj):
    n = 1
    count = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
            else:
                count += 1
        if count != 0:
            break
        n += 1
    return lst_obj


def bubble_reverse_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(1, len(lst_obj)):
            if lst_obj[-i] > lst_obj[-i-1]:
                lst_obj[-i], lst_obj[-i-1] = lst_obj[-i-1], lst_obj[-i]
        n += 1
    return lst_obj


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


print(timeit.timeit("bubble_reverse_sort(orig_list[:])", \
     setup="from __main__ import bubble_reverse_sort, orig_list", number=1000))

print(f"Исходный массив {orig_list}")
print(f"Он же отсортированный по убыванию {bubble_reverse_sort(orig_list)}")

test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Время доработанного:",timeit.timeit("bubble_sort_elaborated(test_list[:])", \
     setup="from __main__ import bubble_sort_elaborated, test_list", number=1000),
      bubble_sort_elaborated(test_list[:]))

print("Время без доработки:",timeit.timeit("bubble_sort(test_list[:])", \
     setup="from __main__ import bubble_sort, test_list", number=1000),
      bubble_sort(test_list[:]))

"""
Метод сортировки был доработан добавлением проверки на наличие сортировок, 
время до доработки составило 0.008442010000000007,
время после 0.0018044139999999972.
Доработанный метод справляется быстрее
"""
