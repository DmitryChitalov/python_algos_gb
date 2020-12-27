"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def left_sum(n, start, result):
    if start > n:
        return result
    else:
        result += start
        return left_sum(n, start + 1, result)


def right_sum(n):
    return n * (n + 1) / 2


def check_form(n):
    left = left_sum(n, 1, 0)
    right = right_sum(n)
    if left == right:
        print('Левая и правая части равны')
    else:
        print('Левая и правая части неравны')


check_form(10)
