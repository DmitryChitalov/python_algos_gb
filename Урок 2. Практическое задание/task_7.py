"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import sys


MAXN = sys.getrecursionlimit() - 3


def arith_sum(n, s=0):
    if n == 0:
        return s
    return arith_sum(n-1, s+n)


def exact_sum(n):
    return n * (n+1) // 2


while True:
    try:
        n = int(input(f"Введите число от 1 до {MAXN}: "))
    except ValueError:
        continue
    if n >= 1 and n <= MAXN:
        break

print(f"Считаем сумму {n} членов арифметической прогресии")
print("Непосредственно: ", arith_sum(n))
print("По формуле: ", exact_sum(n))
