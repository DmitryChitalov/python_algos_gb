"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def summ_func(count, numb, numb_count, numb_summ):
    if count == numb_count:
        print(f'Количество элементов {numb_count}, сумма элементов: {numb_summ}')

    if count < numb_count:
        count += 1
        numb = (numb/2) * (-1)
        numb_summ += numb
        return summ_func(count, numb, numb_count, numb_summ)


numbers_count = int(input('Введите количество элементов:'))
first_number = 1
counter = 0
numb_summ = 0


summ_func(counter, first_number, numbers_count, numb_summ)