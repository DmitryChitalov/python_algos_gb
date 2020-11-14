"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def equal(user_number, l = 0, r = 1):

    if l == r:
        print(f'The equality would be {l == r}')
    elif l < r:
        return equal(user_number, l + 1, (user_number * (user_number + 1)) // 2)

try:
    user_number = int(input('Enter your integer: '))
    equal(user_number)
except ValueError:
    print("Try an integer instead!")