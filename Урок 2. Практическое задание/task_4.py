"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
def line_sum(h = 1, summ = 0, n = int(input('Введите количество элементов '))):

    if n < 1:
        return summ
    else:
        summ = summ + h
        h = -(h / 2)
        return summ + line_sum(h,n=n-1)
print(line_sum())