"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def count_nat(num, sum_part=0, mul_part=1):
    if sum_part == mul_part:
        return f' {sum_part == mul_part}'
    elif sum_part < mul_part:
        return count_nat(num, sum_part + 1, num*(num + 1)//2)


print(count_nat(3));


#def

