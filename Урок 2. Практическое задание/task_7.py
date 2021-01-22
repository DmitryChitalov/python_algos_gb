"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def check(num):
    if num == 1:
        return num
    else:
        return check(num - 1) + num


def check_2(num):
    return num * (num + 1) / 2


number = 4
print(check(number))
print(check_2(number))
print(check(number) == check_2(number))


def check_3(num, s=0, m=1):
    print(s)
    if s == m:
        print(f'равны {s == m}')
    elif s < m:
        return check_3(num, s+1, num*(num+1)/2)


check_3(number)
