"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def rec(number, sum=0, q=-0.5, count=0):
    if number == 0:
        return f'Количество элементов - {count}, их сумма - {sum}'
    else:
        return rec(number - 1, sum + q**(number - 1), q, count + 1)


print(rec(int(input('Введите количество элементов: '))))