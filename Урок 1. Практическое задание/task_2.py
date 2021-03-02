"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""


# (N**2) квадратичная сложность, плохой алгоритм
import random


def searchMinN2 (sourcelst):

    sourcelstCopy = sourcelst
    minVal = sourcelst[0]

    for i in range(len(sourcelst)):                                             # n**2
        for j in range(len(sourcelstCopy)):                                     #
            if sourcelst[i] > sourcelstCopy[j]:                                 # 1
                break                                                           # 1
            elif sourcelst[i] <= sourcelstCopy[j] and sourcelst[i] <= minVal:   # 1
                minVal = sourcelst[i]                                           # 1
    return minVal                                                               # 1


# O(N) - линейная сложность
def searchMinN (sourceLst):

    minVal = sourceLst[0]               #(1)

    for i in range(1, len(sourceLst)):  #(n)
        if sourceLst[i] < minVal:       #(1)
            minVal = sourceLst[i]       #(1)
    return minVal                       #(1)


lst1 = [1, 1, 0, 4, 6, 0, 0, 0, 10, -40, -40, 1000, 1, 0, -3]


print(searchMinN(lst1))
print(searchMinN2(lst1))



