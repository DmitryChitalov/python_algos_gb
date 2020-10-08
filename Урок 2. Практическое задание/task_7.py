"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def doc(n):
    f = '({0}**2 + {1})/2 = {2}'.format(n, n, n*(n+1)/2)
    print(f)
    if n == 1:
        return 1
    return doc(n-1) + n


if __name__ == '__main__':
    a = 10
    print(doc(a))