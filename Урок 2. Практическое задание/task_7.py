"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def prove_this(number, first=True):
    if first:
        return number * (number + 1) / 2 == number + prove_this(number - 1, False)
    if number:
        return number + prove_this(number - 1, False)
    return number


print(prove_this(50))
