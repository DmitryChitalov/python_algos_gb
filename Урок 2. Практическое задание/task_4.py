"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_of_row():
    number = None
    summ = 1

    def number_input():
        nonlocal number
        inp = input('Введдите количество элементов: ')
        if inp.isdigit():
            number = inp
            return
        else:
            print('Вы вместо числа ввели строку (((. Исправьтесь')
            number_input()

    def summator(n):
        nonlocal summ
        if n == 1:
            return 1
        else:
            a = summator(n-1) / -2
            summ += a
            return a

    number_input()
    number = int(number)
    summator(number)

    print(f'Количество элементов - {number}, их сумма - {summ}')


if __name__ == '__main__':

    sum_of_row()
