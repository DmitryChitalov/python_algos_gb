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


def bubble_sort(lst_obj):
    """Функция сортировки 'пузырьком' """
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:   # Для убывания поменяли знак на <
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort_smart(lst_obj):
    n, change = 1, 1
    while n < len(lst_obj) and change == 1:     # Включена проверка изменений
        change = 0
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                change = 1      # Фиксация изменений
        n += 1
    return lst_obj


test_list = [random.randint(-10000, 10000) for _ in range(300)]
test_list1 = test_list.copy()

print(test_list)
# print(bubble_sort(test_list))
print(test_list1)
# print(bubble_sort_smart(test_list1))

print('Функция простая время*1000 ', (timeit.timeit("bubble_sort(test_list)", \
    setup="from __main__ import bubble_sort, test_list", number=1)*1000))
print("Функция 'умная' время*1000", (timeit.timeit("bubble_sort_smart(test_list1)", \
    setup="from __main__ import bubble_sort_smart, test_list1", number=1)*1000))

print(test_list)
print(test_list1)
""" Функция 'smart' прерывает работу если при проходе по элементам не происходит изменений в сортируемом массиве
По замерам изменения времени работы функций минимальны
'smart' функция эффективна если массив отсортирован, близок к этому"""