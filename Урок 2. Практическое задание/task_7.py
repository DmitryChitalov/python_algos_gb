"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
from random import randint

def check(n, res=0):
    if n == 0:
        return res
    else:
        return check(n-1, res+n)


n = randint(0, 1000)
print(check(n) == n*(n+1)/2)
