"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


from random import randint


def left(n, now=1):
    if n == now:
        return f'+{now}'
    return f'+{now}' + left(n, now+1)


print('Доказательство равенства - 1+2+...+n = n(n+1)/2')
number = randint(3, 50)
print(f'Пусть n = {number}, тогда левая чать равенства:')
left_part = left(number)[1:]
print(f'{left_part} = {eval(left_part)}')
print('А левая:')
print(f'n(n+1)/2 = {(number*(number+1))/2}')
print(f'{eval(left_part)} = {(number*(number+1))/2}')