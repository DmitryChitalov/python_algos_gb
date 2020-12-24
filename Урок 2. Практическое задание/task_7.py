"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


# Переменную i использую для того, чтобы значение left result оставалось постоянным
def check_equality(n, right_result=0, left_result=1, i=-1):
    i += 1
    if right_result == left_result:
        print(f'{right_result} = {left_result}')
    else:
        return check_equality(n - 1, right_result + n, (n + i) * (n + i + 1) / 2, i)


print(check_equality(15))
