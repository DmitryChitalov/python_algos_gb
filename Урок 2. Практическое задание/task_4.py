"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_series(length):
    if not isinstance(length, int) or length <= 0:
        return 'Нужно ввести целое положительное число'
    number = 1
    coefficient = (-0.5) ** (length - 1)
    if length == 1:
        return number
    elif length == 2:
        return number + (number * coefficient)
    else:
        return sum_series(length - 1) + (number * coefficient)


print(sum_series(11))
