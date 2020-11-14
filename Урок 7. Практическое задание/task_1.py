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

import random, timeit

original_lst = [random.randint(-100,100) for _ in range(100)]
print(original_lst)

# вариант без выхода
def bubble_sort(oLst, n=0):
    if n != len(oLst)-1:
        for i in range(len(oLst)-1):
            #print(i)
            if oLst[i] < oLst[i+1]:
                oLst.insert(i+1, oLst.pop(i))
                #print(oLst)
        n+=1
        bubble_sort(oLst, n)
    return oLst

# вариант с выходом
def bubble_sort_two(oLst, n=0):
    if n != len(oLst)-1:
        for i in range(len(oLst)-1):
            #print(i)
            if oLst[i] < oLst[i+1]:
                oLst.insert(i+1, oLst.pop(i))
                #print(oLst)
            else:
                #print('no sorting')
                break
        n+=1
        bubble_sort_two(oLst, n)
    return oLst

# сначала отсортируем список, т.к. сравнивать две функции на неотсортированном списке нет смысла
print(bubble_sort(original_lst))

# теперь можно сделать замеры
print('10 -- def#1', timeit.timeit('bubble_sort(original_lst[:])', \
                   setup='from __main__ import bubble_sort, original_lst', \
                    number=10))
print('10 -- def#2', timeit.timeit('bubble_sort_two(original_lst[:])', \
                   setup='from __main__ import bubble_sort_two, original_lst', \
                    number=10))

print('100 -- def#1', timeit.timeit('bubble_sort(original_lst[:])', \
                   setup='from __main__ import bubble_sort, original_lst', \
                    number=100))
print('100 -- def#2', timeit.timeit('bubble_sort_two(original_lst[:])', \
                   setup='from __main__ import bubble_sort_two, original_lst', \
                    number=100))

# динамика такая, что при увеличении проходов в 10 раз,
# разница между алгоритмами увеличивается минимум в 10 раз
# и с увеличением проходов растёт в некоторой прогресии.
# Вообще, это не сильно похоже на улучшение, скорее это обработка исключения