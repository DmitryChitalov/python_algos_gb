"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_series_numbers(amount_elem, cnt=0, num=1.0, total=0.0):
    if cnt == amount_elem:
        print(f'Количество элементов = {amount_elem} их сумма = {total}')
    elif cnt < amount_elem:
        return sum_series_numbers(amount_elem, cnt + 1, num / 2 * -1, total + num)
    else:
        print('Что-то пошло не так')


user_in = int(input('Введите количество элементов: '))
sum_series_numbers(user_in)
