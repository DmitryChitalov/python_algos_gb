"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
import sys


def numbers_sum(number):
    if number == 1:
        return number
    else:
        return number + numbers_sum(number - 1)


def proof(n):
    if n == 0:
        return
    if numbers_sum(n) != n * (n + 1) / 2:
        print(f"Гипотеза неверна для n= {n}!!!")
    else:
        # print(f"Гипотеза верна для n= {n}")
        proof(n - 1)


try:
    n = int(input("Введите число (до 998):  "))
except ValueError:
    print("Вы ввели не число!")
    exit()
sys.setrecursionlimit(n + 3)
proof(n)
print(f"Проверка проведена для n в диапазоне [1,{n}]")
