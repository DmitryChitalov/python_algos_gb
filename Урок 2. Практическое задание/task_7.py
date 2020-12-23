"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

import sys

sys.setrecursionlimit(10000)


# Переменную i использую для того, чтобы значение left result оставалось постоянным
# Не могу понять, за счет чего у меня переполняется стек
def check_equality(n, right_result=0, left_result=1, i=0):
    i += 1
    if right_result == left_result:
        print(f'{right_result} = {left_result}')
    else:
        i += 1
        return check_equality(n - 1, right_result + n, (n + i) * (n + i + 1) / 2)


print(check_equality(3))
print(check_equality(4))
