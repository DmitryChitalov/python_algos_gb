"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def create_many(number):
    if number == 1:
        return 1
    else:
        return number + create_many(number - 1)


def check_eq(number):
    first = create_many(number)
    second = number * (number + 1) / 2
    return first == second


print(create_many(3))
print(check_eq(3))
