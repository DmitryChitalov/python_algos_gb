"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_numbers(n):
    try:
        sum_numbers.i += 1
    except AttributeError:
        sum_numbers.i = 1
        sum_numbers.n = 1
        sum_numbers.s = 1
    if sum_numbers.i == n:
        return sum_numbers.s
    else:
        sum_numbers.n /= - 2
        sum_numbers.s += sum_numbers.n
        return sum_numbers(n)


while True:
    try:
        num_elems = int(input('Введите количество элементов: '))
    except ValueError:
        num_elems = 0
    if num_elems > 0:
        break
    else:
        print('Нужно ввести целое положительное число больше нуля!')
print(f'Количество элементов - {num_elems}, их сумма - {sum_numbers(num_elems)}')
