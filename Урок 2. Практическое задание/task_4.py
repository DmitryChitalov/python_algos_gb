"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def summ(n):
    if n == 0:
        return 0
    else:
        return 1 + summ(n - 1) / -2

num = int(input('Введите количество элементов: '))
print(f'Количество элементов {num}, их сумма - {summ(num)}')