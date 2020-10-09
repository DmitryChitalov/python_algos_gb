#! /bin/python3
"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def progress(n):
    if n > 0:
        return n + progress(n - 1)
    else:
        return 0


num = int(input('Введите число элементов прогрессии: '))
print('Сумма элементов "В лоб":    ' + str(progress(num)))
print('Сумма элементов по формуле: ' + str(num * (num + 1) // 2))
