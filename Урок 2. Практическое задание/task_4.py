"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def rec_sum(i, n, value, sum_n):
    if i == n:  # условие завершения
        return sum_n
    elif i < n:  # иначе делаем и опять запускаем
        i += 1
        sum_n += value
        value *= -0.5
        return rec_sum(i, n, value, sum_n)


u_input = input('Enter a num of elements: \n')
if u_input.isnumeric():
    print('Result:', rec_sum(0, int(u_input), 1, 0))
else:
    print('You must enter a number')
