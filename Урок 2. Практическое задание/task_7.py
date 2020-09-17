"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


# n = 5
# сумма
# s_1 = 0
# for el in range(1, n+1):
#     s_1 += el
# print(s_1)
# сумма правой части
# s_2 = n*(n+1)/2
# print(s_2)

import random
m = random.randint(2, 99)
print(f'число- {m}')


def equality_check_1(n):
    if n == 0:
        return 0
    else:
        return n + equality_check_1(n-1)


def equality_check_2(n):
    s = n * (n + 1) / 2
    return s


print(equality_check_1(m))
print(equality_check_2(m))

if equality_check_2(m) == equality_check_2(m):
    print('Доказано!')
else:
    print('Что- то пошло не так!')
    