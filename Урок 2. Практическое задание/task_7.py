"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

##############################################################################################
import sys


def check_equation_f(length):
    """
    функция проверяет равентство 1+2+...+n = n(n+1)/2 для всех натуральных чисел
    """
    if length == 0:
        return

    print(sum([x for x in range(length + 1)]) == (length * (length + 1)) / 2)
    check_equation_f(length - 1)


sys.setrecursionlimit(10000)
check_equation_f(6000)
