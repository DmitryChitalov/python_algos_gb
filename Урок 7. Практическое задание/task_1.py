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
а по убыванию.
Нужно отдавать копию списка в подсчет времени, а не исходный список
"""
from random import randint
from timeit import timeit


def bubbleSort(list):
    m = 0
    for i in range(len(list)-1,0,-1):
        for i in range(i):
            if list[i] < list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                m = 1
        if m == 0:
            break
    return list


def bubbleSort_pro(list):
    m = 0
    for i in range(len(list)-1,0,-1):
        for i in range(i):
            if list[i] < list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
                m = 1
        if m == 0:
            break
    return list


orig_list = [randint(-100, 100) for _ in range(100)]
print(orig_list)
bubbleSort(orig_list)
print(orig_list)

orig_list = [randint(-100, 100) for _ in range(100)]

print(timeit("bubbleSort(orig_list[:])", \
    setup="from __main__ import bubbleSort, orig_list", number=1000))


print(timeit("bubbleSort_pro(orig_list[:])", \
    setup="from __main__ import bubbleSort_pro, orig_list", number=1000))


'''
0.920986611
0.885456861 - с break

Остановка работы скрипта с помощью break ничего не улучшает
'''