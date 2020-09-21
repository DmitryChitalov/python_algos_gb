"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_number(number_zero, number, count, sum_n):
    if number_zero == count:
        return print(f'Количество элементов - {count}, их сумма - {sum_n}')
    elif number_zero < count:
        number_zero += 1
        sum_n += number
        sum_number(number_zero, number / 2 * - 1, count, sum_n)


try:
    count = int(input("Введите число: "))
    sum_number(0, 1, count, 0)
except ValueError:
    print(f"Вы ввели не число, пожалуйста, введите число ")