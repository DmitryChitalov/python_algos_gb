"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def enter():
    num = input('Введите натуральное число: ')
    if not num.isdigit():
        print('Некорректный ввод.')
        return enter()
    return int(num)

def sum_nat(n: int):
    if n <= 1:
        return n
    else:
        return n + sum_nat(n - 1)

def check(n: int):
    if n * (n + 1) / 2 == sum_nat(n):
        print(f'Равенство 1+2+...+n = n(n+1)/2 справедливо для n = {n}.')
    else:
        print(f'Равенство 1+2+...+n = n(n+1)/2 несправедливо для n = {n}.')

if __name__ == '__main__':
    check(enter())