"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def row_sum(n, elements_sum=0, start_elem=1):
    try:
        if n == 0:
            return elements_sum
        else:
            return row_sum(n - 1, elements_sum + start_elem, start_elem / -2)
    except RecursionError:
        print('Вы ввели некорректное число, введите целое число')


print(row_sum(3))
