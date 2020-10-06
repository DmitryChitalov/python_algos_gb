"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def substant(n, left_part=0, right_part=1):
    if left_part == right_part:
        print('Равенство верно')
    elif left_part < right_part:
        right_part = (n + 1) / 2
        substant(n, left_part + 1, right_part)


n = int(input('Введите любое натуральное число: '))
substant(n)
