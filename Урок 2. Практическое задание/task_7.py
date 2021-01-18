"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def check(n, summ, count):
    if n == 0:
        if summ == count * (count + 1) / 2:
            return print('Равенство верно')
        else:
            return print('Равенство неверно')
    else:
        return check(n - 1, summ + n, count + 1)


check(int(input('Для какова кол-ва чисел проверим равенство? ')), 0, 0)
