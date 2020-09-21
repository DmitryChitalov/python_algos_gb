"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_calculate(user_num, start=1, my_sum=0):
    if user_num == start:
        my_sum += start
        formula = int(user_num * (user_num + 1) / 2)
        if my_sum == formula:
            return True
        else:
            return False
    else:
        my_sum += start
        return sum_calculate(user_num, start + 1, my_sum)


print(sum_calculate(20))
